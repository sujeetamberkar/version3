from django import template
from django.forms.widgets import Widget

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to a form field.
    """
    if not isinstance(value, Widget):
        return value
    return value.as_widget(attrs={"class": arg})
