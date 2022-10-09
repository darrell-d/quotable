from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag()
def debug_object_dump(var):
    return vars(var)

# @register.simple_tag()
# def get_author_from_quote(var):
#     return vars(var)

# @register.simple_tag()
# def get_quote_text(var):
#     return vars(var)