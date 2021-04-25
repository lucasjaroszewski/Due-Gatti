from django import template

register = template.Library()

@register.filter
def format_comma(value):
    return value.replace(".", ",")
