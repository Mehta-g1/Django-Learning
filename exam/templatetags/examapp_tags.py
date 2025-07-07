import datetime
from django import template

register = template.Library()

@register.simple_tag(name="today")
def get_date():
    return datetime.datetime.now()

@register.filter(name='quotes')
def quotes(value):
    return '"'+str(value)+'"'