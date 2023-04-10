from django.urls import path

from .views import NetworkAPIView

urlpatterns = [
    path("", NetworkAPIView.as_view(), name="network")
    ]