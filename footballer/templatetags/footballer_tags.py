from django import template

from footballer.models import Footballer, Position


register = template.Library()

@register.simple_tag()
def get_positions():
    return Position.objects.all()


