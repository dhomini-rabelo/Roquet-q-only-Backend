# django
from django.core.validators import validate_slug, validate_unicode_slug 
# this module
from .validators import validate_for_email, validate_unique, validate_caracters
from .utils import get_type
from .support import type_validation, adapt_form_errors
# others
from string import digits
from decimal import Decimal
from datetime import datetime


def convert_validation(obj, new_type: str):
    if new_type == 'pass': return 'valid'
    initial_type = get_type(obj)
    type_validation(initial_type, new_type)
    if initial_type == 'str':
        if new_type == 'str': 
            return 'valid'
        elif new_type == 'int':
            try: 
                return int(obj)
            except:
                return 'convert_error'
        elif new_type == 'float':
            try: 
                return float(obj)
            except:
                return 'convert_error'
        elif new_type == 'decimal':
            try: 
                return Decimal(obj)
            except:
                return 'convert_error'
        elif new_type == 'bool':
            try:
                return bool(obj)
            except:
                return 'convert_error'
        elif new_type == 'date':
            try:
                date_check = datetime.strptime(obj, '%Y-%m-%d').date()
                return obj
            except:
                return 'convert_error'
        elif new_type == 'slug':
            try:
                validate_slug(obj)
                validate_unicode_slug(obj)
                return obj
            except:
                return 'convert_error'        
        elif new_type == 'email':
            condition = validate_for_email(obj)
            return obj if condition else 'convert_error'
    elif initial_type is None:
        return 'initial_type_error'
      
        
def get_post_form_errors(Model, fields: list):
    """
    Model list fields
    [[fields(example: name), variable_for_convert_validation, name_field_for_error_messages,
    specific_list_validation_with_tuples(example)[('unique', 'argument: slug')]
    ],]
    variable_for_convert_validation = 'pass' if field don't return str field
    """
    invalid_fields = []
    none_fields = []
    repeated_fields = []
    other_errors = []
    type_more_validations = ['unique', 'email', 'caracters']
    
    for field, convert_var, name_for_error, more_validations in fields:
        validation = convert_validation(field, convert_var)
        if str(validation) == 'convert_error':
            invalid_fields.append(name_for_error)
        elif str(validation) == 'initial_type_error':
            none_fields.append(name_for_error)        
        else:
            for other_validation in more_validations:
                if other_validation[0] == 'unique':
                    if not validate_unique(Model, other_validation[1]):
                        repeated_fields.append(name_for_error)
                if other_validation[0] == 'email':
                    if not validate_for_email(field):
                        other_errors.append(f'O campo {name_for_error} não informa email válido')
                if other_validation[0] == 'caracters':
                    if not validate_caracters(field, other_validation[1]):
                        other_errors.append( f'O campo {name_for_error} possui caracteres inválidos')
    
    form_errors = {'invalid_fields': invalid_fields, 'none_fields': none_fields,
                   'repeated_fields': repeated_fields, 'other_errors': other_errors}
    form_errors = adapt_form_errors(form_errors)
    
    return form_errors if form_errors != [] else None 
    
    
def get_password_error(password, confirm_password):
    if not password == confirm_password:
        return 'As senhas nonvas senhas não são iguais'
    elif not validate_caracters(password, False, False):
        return 'A senha possui caracteres inválidos'
    elif len(password) < 8:
        return 'A senha é muito curta'
    return None


def change_password(user, current_password, new_password, new_password_confirm):
    errors_list = list()
    if current_password is None:
        errors_list.append('O campo senha atual não foi informado')
    if new_password is None:
        errors_list.append('O campo de nova senha não foi informado')
    if new_password_confirm is None:
        errors_list.append('O campo de confirmação de nova senha não foi informado')
    if errors_list == []:
        if not user.check_password(current_password):
            errors_list.append('A senha atual não está correta')
        else:
            error_password = get_password_error(new_password, new_password_confirm)
            if error_password is None:
                user.set_password(new_password)
                user.save()
            errors_list.append(error_password)
    return errors_list if errors_list != [] else None
    



class Session:
    def __init__(self, request, name, initial_value):
        self.name = name
        self.request = request
        self.edit(initial_value)
        self.value = request[name]
    
    def edit(self, value):
        self.request[self.name] = value
        
    def delete(self):
        self.request[self.name] = None