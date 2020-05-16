from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('django.contrib.auth.urls')),
    url(r'^api/', include(('api.urls', 'api'), namespace='api')),
    url(r'^health-check/?$', views.HealthCheckAPIView.as_view(), name='health-check'),
]
