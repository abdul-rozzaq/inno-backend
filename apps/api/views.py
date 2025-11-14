from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.api.serializers import HomePageSerializer
from apps.pages.models import HomePage


class HomePageAPIView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        homepage = HomePage.objects.first()
        if not homepage:
            # Return an empty, typed payload rather than erroring
            empty = {
                "header_title": "",
                "header_subtitle": "",
                "header_video_link": None,
                "header_image": None,
                "about_title": "",
                "about_subtitle": "",
                "about_text": "",
                "about_image": None,
                "features_title": "",
                "features_subtitle": "",
                "features_text": "",
                "services_title": "",
                "services_text": "",
                "offers_badge": "",
                "offers_title": "",
                "offers_toggle_left": "",
                "offers_toggle_right": "",
                "testimonials_title": "",
                "testimonials_text": "",
                "footer_title": "",
                "footer_text": "",
                "skills": [],
                "features": [],
                "services": [],
                "pricing": [],
                "testimonials": [],
            }
            return Response(empty, status=status.HTTP_200_OK)

        serializer = HomePageSerializer(homepage)
        return Response(serializer.data)
