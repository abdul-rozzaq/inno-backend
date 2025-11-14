from pathlib import Path

from environs import Env

env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env.str("SECRET_KEY", default="weak-secret-key-for-dev")

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["*"] if DEBUG else env.list("ALLOWED_HOSTS", default=[])

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


EXTERNAL_APPS = [
    "rest_framework",
    "corsheaders",
]

LOCAL_APPS = [
    "apps.pages.apps.PagesConfig",
    "apps.api.apps.ApiConfig",
]


INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + LOCAL_APPS


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# CORS for frontend dev server
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS") + [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================
# Jazzmin Admin Configuration
# ==========================
JAZZMIN_SETTINGS = {
    "site_title": "Inno Admin",
    "site_header": "INNOVATED",
    "site_brand": "INNOVATED Admin",
    "welcome_sign": "Welcome to INNOVATED admin",
    "show_sidebar": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": [
        "pages",
        "auth",
    ],
    "icons": {
        "pages.HomePage": "fas fa-home",
        "pages.AboutSkill": "fas fa-percent",
        "pages.Feature": "fas fa-star",
        "pages.Service": "fas fa-cogs",
        "pages.PricingPlan": "fas fa-tags",
        "pages.Testimonial": "fas fa-comments",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"app": "pages"},
        {"name": "Frontend", "url": "http://localhost:5173", "new_window": True},
    ],
    "related_modal_active": True,
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",  # flatly, darkly, cyborg, etc.
    "navbar": "navbar-dark",
    "navbar_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "footer_fixed": False,
    "actions_sticky_top": True,
}
