# teacher/templatetags/custom_filters.py

from django import template
from django.forms.widgets import Widget

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def default_if_none(value, default=""):
    return value if value is not None else default

@register.filter
def attr(obj, attr_name):
    return getattr(obj, attr_name, "")

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    """
    Adds a CSS class to a form field.
    """
    if isinstance(value, Widget):
        return value.as_widget(attrs={"class": css_class})
    else:
        return value
