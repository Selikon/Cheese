from atexit import register
from django import template 

from database.models import номенклатура

register= template.Library()

@register.simple_tag()
def get_номенклатура():
    return номенклатура.objects.all()
    