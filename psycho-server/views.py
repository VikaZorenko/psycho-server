from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response(data={'status': 'OK'}, status=200)


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
