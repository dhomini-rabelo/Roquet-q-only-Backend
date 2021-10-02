# this module
from .exceptions import TypeNotFoundError, EqualTypeError

def type_validation(initial_type:str, new_type:str):
    possible_types = ['str', 'int', 'decimal', 'bool', 'date', 'email',
                      'float', 'NoneType', 'slug']
    if initial_type not in possible_types:
        raise TypeNotFoundError(f'{initial_type} type not identified')
    elif new_type not in possible_types:
        raise TypeNotFoundError(f'{new_type} type not identified')


def adapt_form_errors(form_errors: dict):
    list_errors = []
    for name in form_errors['invalid_fields']:
        list_errors.append([name,f'Este campo é inválido'])
    for name in form_errors['none_fields']:
        list_errors.append([name, f'Este campo é obrigatório'])
    for error in form_errors['other_errors']:
        if error[0] == 'unique':
            list_errors.append([error[1], f'Este {error[1]} já está em uso'])
        elif error[0] == 'email':
            list_errors.append([error[1], f'Email inválido'])
        elif error[0] == 'caracters':
            list_errors.append([error[1], f'Você inseriu caracters inválidos'])
        elif error[0] == 'min_length':
            list_errors.append([error[1], f'Este campo deve ter no mínimo {error[2]} dígitos'])
        elif error[0] == 'equal_length':
            list_errors.append([error[1], f'Este campo deve ter exatamente {error[2]} dígitos'])
        elif error[0] == 'max_length':
            list_errors.append([error[1], f'Este campo deve ter no máximo {error[2]} dígitos'])
    return list_errors 


def adapt_list_of_post_form(post_form_list: list):
    new_list = []
    for form_list in post_form_list:
        if len(form_list) == 4:
            new_list.append(form_list)
        elif len(form_list) == 3:
            model = form_list[:]
            model.append([])
            new_list.append(model)
        else:
            new_list.append(form_list)
    return new_list
