from Django import TEMPLATES
import datetime
register= template.library()
@register.simple_tag(name="get_date")
def get_date():
    now= datetime.datetime.now()
    return now
