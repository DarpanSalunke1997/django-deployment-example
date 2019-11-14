# this code cuts the passed value , it is custome cut method

from django import template

register = template.Library()

# this line filter the template using decoreters
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """

    return value.replace(arg,'')

# this line filter the template, it is defalt method
# register.filter('cut',cut)