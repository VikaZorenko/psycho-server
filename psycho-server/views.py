from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPIView(APIView):
    def get(self, request):
        return Response(data={'status': 'OK'}, status=200)
