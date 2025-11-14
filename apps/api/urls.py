from django.urls import path

from apps.api.views import HomePageAPIView


urlpatterns = [
    path("homepage/", HomePageAPIView.as_view(), name="homepage-api"),
]
