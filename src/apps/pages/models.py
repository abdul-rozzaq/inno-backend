from django.db import models


class HomePage(models.Model):
    # Header uchun
    header_title = models.CharField(max_length=255, default="We target the audience with our ideas.")
    header_subtitle = models.TextField(default="Advertising is relied upon to impact the states of mind, expectations and conduct of the customer’s clients and in this way increment.")
    header_video_link = models.URLField(blank=True, null=True)
    header_image = models.ImageField(upload_to="home/header/", blank=True, null=True)

    # About Section
    about_title = models.CharField(max_length=255, default="ABOUT US")
    about_subtitle = models.CharField(max_length=255, default="Transforming brands with creativity")
    about_text = models.TextField(default="As a rule the organization settles on the inventive and media choices. Regularly it supplies supporting statistical surveying too, and may even be associated.")
    about_image = models.ImageField(upload_to="home/about/", blank=True, null=True)

    # Features section headings/texts
    features_title = models.CharField(max_length=255, default="FEATURES")
    features_subtitle = models.CharField(max_length=255, default="We have impressive Template Features")
    features_text = models.TextField(default=("Advertising office is a business that helps promoters in all phases of the advertising " "procedure – from record administration and intending to message creation."))

    # Services section headings/texts
    services_title = models.CharField(max_length=255, default="Our best services to solve Your problems.")
    services_text = models.TextField(default=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Auctor tincidunt neque " "vulputate vel sit ornare in ac. Aenean integer amet viverra sed gravida."))

    # Offers (pricing) section headings/texts
    offers_badge = models.CharField(max_length=255, default="THE BEST OFFERS")
    offers_title = models.CharField(max_length=255, default="OUR PRICING PLAN")
    offers_toggle_left = models.CharField(max_length=100, default="Yearly Billing")
    offers_toggle_right = models.CharField(max_length=100, default="Monthly billing")

    # Testimonials section headings/texts
    testimonials_title = models.CharField(max_length=255, default="See what our clients say!")
    testimonials_text = models.TextField(default=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Varius semper velit non nulla " "adipiscing nisl vel mi elementum."))

    # Footer statik bo‘ladi
    footer_title = models.CharField(max_length=255, default="INNOVATED")
    footer_text = models.TextField(default="Advertising office is a business that helps promoters in all phases of the advertising procedure – from record administration.")

    def __str__(self):
        return "Home Page"


# ===========================
# About Skills (Web Design, UI & UX, etc.)
# ===========================
class AboutSkill(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=100)
    percent = models.IntegerField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ===========================
# Features Section
# ===========================
class Feature(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="features")
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="home/features/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ===========================
# Services Section
# ===========================
class Service(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="services")
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="home/services/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ===========================
# Pricing Plans
# ===========================
class PricingPlan(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="pricing")
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    disk_space = models.CharField(max_length=50)
    support = models.CharField(max_length=50)
    domains = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ===========================
# Testimonials
# ===========================
class Testimonial(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name="testimonials")
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    comment = models.TextField()
    avatar = models.ImageField(upload_to="home/testimonials/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
