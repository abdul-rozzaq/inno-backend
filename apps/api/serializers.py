from rest_framework import serializers


from apps.pages.models import HomePage


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = [
            "header_title",
            "header_subtitle",
            "header_video_link",
            "header_image",
            "about_title",
            "about_subtitle",
            "about_text",
            "about_image",
            # Features section texts
            "features_title",
            "features_subtitle",
            "features_text",
            # Services section texts
            "services_title",
            "services_text",
            # Offers section texts
            "offers_badge",
            "offers_title",
            "offers_toggle_left",
            "offers_toggle_right",
            # Testimonials section texts
            "testimonials_title",
            "testimonials_text",
            "footer_title",
            "footer_text",
            "skills",
            "features",
            "services",
            "pricing",
            "testimonials",
        ]
        depth = 1
