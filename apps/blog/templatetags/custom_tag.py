from random import randint
from django import template

register = template.Library()


@register.simple_tag()
def random_num():
    return randint(1, 10)
