# teacher/templatetags/custom_filters.py

from django import template

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
