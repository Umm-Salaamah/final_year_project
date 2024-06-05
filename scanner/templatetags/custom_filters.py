# scanner/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='header_class')
def header_class(status):
    return 'header-present' if status == 'Present' else 'header-missing'
