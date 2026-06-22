from django import template

register = template.Library()


@register.filter
def linebreak_title(value):
    if not value:
        return ''
    return value.replace(' ', '<br>').replace('\n', '<br>')
