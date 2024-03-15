from django import template
from django.contrib.auth.models import User
import re
 
from django.utils.html import format_html
from aprajitaretails import settings
from ui.utils import get_menu_items
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import (PAGE_VAR)
# from myapp.models import UserLog  # assuming you have a UserLog model

register = template.Library()
assignment_tag = register.assignment_tag if hasattr(register, 'assignment_tag') else register.simple_tag

# @register.simple_tag
# def get_user_log(limit, user):
#      return UserLog.objects.filter(user=user).order_by('-timestamp')[:limit]

@register.simple_tag
def app_title():
    return "Aprajita Retails"

@register.simple_tag
def app_name():
    return "Aprajita Retails-Network"

numeric_test = re.compile("^\d+$")
register = template.Library()

def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""

    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif numeric_test.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return settings.TEMPLATE_STRING_IF_INVALID

register.filter('getattribute', getattribute)

# @register.filter
# def get_attr(obj, val):
#     return getattr(obj, val)
# #register.filter('get_attr', get_attr)

# @register.filter
# def getattr (obj, args):
#     """ Try to get an attribute from an object.

#     Example: {% if block|getattr:"editable,True" %}

#     Beware that the default is always a string, if you want this
#     to return False, pass an empty second argument:
#     {% if block|getattr:"editable," %}
#     """
#     (attribute, default) = args.split(',')
#     try:
#         return obj.__getattribute__(attribute)
#     except AttributeError:
#          return  obj.__dict__.get(attribute, default)
#     except:
#         return default
    
# #register.filter('getattr', getattr)