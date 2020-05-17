from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import (
    UserSerializer,
    TestListSerializer,
    TestDetailsSerializer,
    QuestionsListSerializer,
    QuestionDetailsSerializer,
    TestResultsListSerializer,
    TestResultDetailsSerializer,
    TestResultCreateSerializer,
    QuestionResultCreateSerializer,
)
from tests.models import Test, TestResult


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'username': user.username,
        })


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class TestsListApiView(ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TestListSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-created_date')


class TestRetrieveApiView(RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TestDetailsSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        return self.model.objects.prefetch_related('questions').get(id=self.kwargs['test_id'])


class QuestionsListApiView(ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = QuestionsListSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(test__id=self.kwargs['test_id'])
        return queryset.order_by('-created_date', 'id')


class QuestionRetrieveApiView(RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = QuestionDetailsSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        return self.model.objects.prefetch_related('answers').get(id=self.kwargs['question_id'])


class NextQuestionRetrieveApiView(RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = QuestionDetailsSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        test_result = TestResult.objects.filter(user__id=self.request.user.id).get(id=self.kwargs['result_id'])
        answered_questions = test_result.question_results.values_list('question__id', flat=True)
        return test_result.test.questions.exclude(id__in=answered_questions).first()


class TestResultsListApiView(ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TestResultsListSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        queryset = self.model.objects.filter(user__id=self.request.user.id)
        return queryset.order_by('-created_date')


class TestResultRetrieveApiView(RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TestResultDetailsSerializer
    model = serializer_class.Meta.model

    def get_object(self):
        return self.model.objects.filter(user__id=self.request.user.id)\
                                 .prefetch_related('question_results', 'test_stat_results')\
                                 .get(id=self.kwargs['result_id'])


class TestResultCreateApiView(CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TestResultCreateSerializer
    model = serializer_class.Meta.model

    def get_serializer_context(self):
        try:
            test_id = self.kwargs['test_id']
            test = Test.objects.get(id=test_id)
        except Test.DoesNotExist:
            raise Http404("Test with such id wasn't found")

        context = super().get_serializer_context()
        context['user'] = self.request.user
        context['test'] = test
        return context


class QuestionResultCreateApiView(CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = QuestionResultCreateSerializer
    model = serializer_class.Meta.model

    def get_serializer_context(self):
        try:
            result_id = self.kwargs['result_id']
            test_result = TestResult.objects.get(id=result_id)
        except TestResult.DoesNotExist:
            raise Http404("Test result with such id wasn't found")

        if test_result.user != self.request.user:
            raise ValidationError("You can't answer another user's test!")

        context = super().get_serializer_context()
        context['user'] = self.request.user
        context['test_result'] = test_result
        return context

