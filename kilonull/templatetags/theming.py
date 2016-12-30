from django import template
# from kilonull.conf import BlogConf
from kilonull.models import Menu, MenuItem
from kilonull.settings import SETTINGS
import re

register = template.Library()


@register.simple_tag
def blog_title():
    return SETTINGS['BLOG_TITLE']


# Generate HTML for the header menu.
# Use a regex (path) to check if the current page is in the menu. If it is,
# apply the active class.
@register.simple_tag
def get_menu(menu_slug, curr_page):
    html = ""
    menu_items = MenuItem.objects.filter(menu__slug=menu_slug) \
        .order_by("order")
    path = re.compile("%s(.*)" % SETTINGS['BLOG_SITE_URL'])
    for item in menu_items:
        html += "<li"
        match = path.match(item.link_url)
        print(curr_page)
        print(match)
        if match and match.group(1) == curr_page:
            html += " class='active'"
        html += "><a href='%s'>%s</a></li>" % (item.link_url, item.link_text)
    return html
