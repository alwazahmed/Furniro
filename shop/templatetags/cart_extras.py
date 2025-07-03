from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    print("Running multiply:", value, arg)
    try:
        result = float(value) * float(arg)
        return result
    except (ValueError, TypeError):
        return 'Hello'
