# django
from django.core.validators import validate_email
# others
from string import ascii_letters, digits


def validate_caracters(text: str, with_accents=True, spaces=True, length=None):
    accents = 'áàéèíìóòúùâêîôûãõ' if with_accents else ''
    space = ' ' if spaces else ''
    symbols = "@.+-_"
    alloweds = symbols + digits + ascii_letters + accents + space
    for letter in text.lower():
       if letter not in alloweds:
           return False
    if not (length is None):
        return False if len(text) < length else True
    return True


def validate_for_email(email: str):
    try:
        validate_email(email)
        return True
    except:
        return False
    
    
def validate_unique(Model, field: str):
    fields = list(item[0] for item in Model.objects.values_list(field))
    if field in fields:
        return False
    return True
    


    