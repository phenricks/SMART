from django import template
from django.template.defaultfilters import stringfilter
import hashlib

register = template.Library()

@register.filter
@stringfilter
def id(value):
    hash_object = hashlib.md5(value.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig[0:7]
