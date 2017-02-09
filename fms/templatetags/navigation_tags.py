from django import template
import re

register = template.Library()

@register.simple_tag
def active(request, pattern):
    pattern = r'^%s$' % pattern
    if re.search(pattern, request.path):
        return "nav-link active"
    return "nav-link"

@register.simple_tag
def active_sub(request, pattern):
    if re.search(pattern, request.path):
        return "nav-link active bg-info ml-3"
    return "nav-link text-info ml-3"
