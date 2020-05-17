from rest_framework import serializers
from django.contrib.auth.models import User

from tests.models import (
    Test,
    Question,
    Answer,
    TestResult,
    TestStat,
    TestStatResult,
    QuestionResult
)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        if validated_data.get('email'):
            user.email = validated_data['email']
        user.save()

        return user

    class Meta:
        model = User
        fields = ("id", "username", "email", "password",)


class TestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("id", "name", "description", "created_date", "modified_date")


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "name", "description", "created_date", "modified_date")


class AnswersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "name", "description", "created_date", "modified_date")


class TestResultsListSerializer(serializers.ModelSerializer):
    test = TestListSerializer()

    class Meta:
        model = TestResult
        fields = ("id", "test", "is_finished", "created_date", "modified_date")


class TestStatsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStat
        fields = ("id", "name", "description", "created_date", "modified_date")


class QuestionResultsListSerializer(serializers.ModelSerializer):
    question = QuestionsListSerializer()
    answer = AnswersListSerializer()

    class Meta:
        model = QuestionResult
        fields = ("id", "question", "answer", "created_date", "modified_date")


class TestStatResultsListSerializer(serializers.ModelSerializer):
    test_stat = TestStatsListSerializer()

    class Meta:
        model = TestStatResult
        fields = ("id", "test_stat", "points", "created_date", "modified_date")


class TestDetailsSerializer(serializers.ModelSerializer):
    questions = QuestionsListSerializer(many=True)

    class Meta:
        model = Test
        fields = ("id", "name", "description", "questions", "created_date", "modified_date")


class QuestionDetailsSerializer(serializers.ModelSerializer):
    answers = AnswersListSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "name", "description", "answers", "created_date", "modified_date")


class TestResultDetailsSerializer(serializers.ModelSerializer):
    test = TestListSerializer()
    question_results = QuestionResultsListSerializer(many=True)
    test_stat_results = TestStatResultsListSerializer(many=True)

    class Meta:
        model = TestResult
        fields = ("id", "test", "is_finished", "question_results", "test_stat_results", "created_date", "modified_date")


class TestResultCreateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    test = TestListSerializer(read_only=True)
    is_finished = serializers.BooleanField(read_only=True)
    created_date = serializers.DateTimeField(read_only=True)
    modified_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        test_result = TestResult.objects.create(user=self.context['user'],
                                                test=self.context['test'])
        for test_stat in self.context['test'].test_stats.all():
            TestStatResult.objects.create(test_stat=test_stat,
                                          test_result=test_result)
        return test_result

    class Meta:
        model = TestResult
        fields = ("id", "test", "is_finished", "created_date", "modified_date")


class QuestionResultCreateSerializer(serializers.ModelSerializer):
    question_id = serializers.CharField(write_only=True)
    answer_id = serializers.CharField(write_only=True)
    question = QuestionsListSerializer(read_only=True)
    answer = AnswersListSerializer(read_only=True)

    def create(self, validated_data):
        test_result = self.context['test_result']
        try:
            question = Question.objects.get(id=validated_data['question_id'])
        except Question.DoesNotExist:
            raise ValueError('Question with such id doesn\'t exist.')
        try:
            answer = Answer.objects.filter(question=question).get(id=validated_data['answer_id'])
        except Answer.DoesNotExist:
            raise ValueError('Question with such id doesn\'t exist.')
        question_result = QuestionResult.objects.create(question=question,
                                                        answer=answer,
                                                        test_result=test_result)
        if answer.is_correct:
            test_stat_result = test_result.test_stat_results.get(test_stat__id=question.test_stat.id)
            test_stat_result.points += question.points
            test_stat_result.save()
        if test_result.question_results.count() == test_result.test.questions.count():
            test_result.is_finished = True
            test_result.save()
        return question_result

    class Meta:
        model = QuestionResult
        fields = ("id", "question_id", "answer_id", "question", "answer", "created_date", "modified_date")
        read_only_fields = ("id", "question", "answer", "created_date", "modified_date")
