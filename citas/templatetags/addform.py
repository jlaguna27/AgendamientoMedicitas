import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def add(html_input, properties):
    """
    Inserta propiedades en un campo html.

    Uso: {{ form.field_name|add:'class="form-control" placeholder="Placeholder here"' }}
    """
        
    pattern = r'(\s\/>|>)'
    regex = re.compile(pattern, re.IGNORECASE)
    replace = u' {0}>'.format(properties)
    html = regex.sub(replace, str(html_input))
    return mark_safe(html)