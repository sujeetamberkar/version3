# student/templatetags/youtube_filters.py
from django import template
import re

register = template.Library()

@register.filter
def youtube_id(value):
    """Extracts and returns the YouTube video ID from a URL."""
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', value)
    return match.group(1) if match else ''
