from django import template
register=template.Library()

@register.filter(name='remove_spacial')
def remove_chars(value,arg):
    print("The Value",value)
    print("The Arguement",arg)
    for charecter in arg:
        value=value.replace(charecter,"")
        print("The Charecter",charecter)
    return value   
