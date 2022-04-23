from django import template

register = template.Library()

@register.filter
def round_distance(value):
    """ Function for rounding 'distance' in 'findride' to whole number """
    print(type(value))
    value = round(value, 2)
    return value

# register.filter('round_distance', round_distance)
