from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return round(value * arg, 2)

@register.inclusion_tag('translate.html')
def google_translate(type="simple",language="en"):
    return {
        "language":language,
        "type":type
    }