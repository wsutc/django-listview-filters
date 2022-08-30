from django.conf import settings


def get_setting(setting_name: str, default):
    string = (
        getattr(settings, setting_name) if hasattr(settings, setting_name) else default
    )
    return string
