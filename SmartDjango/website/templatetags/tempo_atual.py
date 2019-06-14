import datetime
from django import template


register = template.Library()


@register.simple_tag
def tempo_atual():
    return datetime.datetime.now().strftime('%d-%m-%y %X')

