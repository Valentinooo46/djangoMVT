from django import template

register = template.Library()

@register.filter
def classname(obj):
    """Повертає назву класу об'єкта"""
    return obj.__class__.__name__