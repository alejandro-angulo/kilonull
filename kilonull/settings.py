"""
Settings for the blog are namespaced in the BLOG setting.
For exmaple your project's `settings.py` file might looks like this:

BLOG = {
    'BLOG_TITLE': 'My Blog',
}
"""

from django.conf import settings as project_settings

DEFAULTS = {
    'BLOG_TITLE': 'My Blog',
    'BLOG_SITE_URL': 'http://localhost',
}

# Check if a setting is applied in the Django project settings.py,
#   if not use the default.
SETTINGS = {}
for setting_name, setting_default in DEFAULTS.items():
    try:
        SETTINGS[setting_name] = project_settings.BLOG[setting_name]
    except (AttributeError, KeyError):
        SETTINGS[setting_name] = DEFAULTS[setting_name]
