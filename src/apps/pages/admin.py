from django.contrib import admin
from .models import HomePage, AboutSkill, Feature, Service, PricingPlan, Testimonial


class AboutSkillInline(admin.StackedInline):
    model = AboutSkill
    max_num = 4
    sortable_field_name = "order"


class FeatureInline(admin.StackedInline):
    model = Feature
    extra = 1
    sortable_field_name = "order"


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 1
    sortable_field_name = "order"


class PricingPlanInline(admin.StackedInline):
    model = PricingPlan
    max_num = 3
    sortable_field_name = "order"


class TestimonialInline(admin.StackedInline):
    model = Testimonial
    extra = 1
    sortable_field_name = "order"


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ("header_title",)
    inlines = [
        AboutSkillInline,
        FeatureInline,
        ServiceInline,
        PricingPlanInline,
        TestimonialInline,
    ]
