from datetime import datetime, timedelta


def simplification(obj_name: str):
    simplification = {'decimal.Decimal': 'decimal', 'datetime.date': 'date'}
    simplified_name = simplification.get(obj_name)
    if simplified_name is None:
        return obj_name
    else:
        return simplified_name


def get_type(obj):
    str_type = str(type(obj))
    initial_position = str_type.find("'")
    end_position = str_type[initial_position+1:].find("'") + len(str_type[: initial_position+1])
    class_name = str_type[initial_position+1:end_position]
    return simplification(class_name)


def filters(string: str, new_type: str):
    alloweds_new_types = ['strip', 'name', 'only_numbers', 'money_br']
    if new_type == 'strip':
        return string.strip()
    elif new_type == 'name':
        string = string.strip().title()
        repeated_spaces = []
        spaces = 0
        for letter in string:
            if spaces == 0 and letter == " ":
                spaces += 1
            elif letter != " ":
                spaces = 0
            else:
                spaces += 1
                repeated_spaces.append(spaces)
        organized_repeated_spaces =  sorted(list(set(repeated_spaces)), reverse=True)
        for number in organized_repeated_spaces:
            string = string.replace(" "*number, " ")
        return string
    elif new_type == 'only_numbers':
        new_string = ''
        for letter in string:
            if letter in list('0123456789'):
                new_string += letter
        return new_string
    elif new_type == 'money_br':
        new_string = ''
        for letter in string:
            if letter in list('0123456789,'):
                new_string += letter
        return new_string.replace(',', '.')        
            

def get_age(date: str):
    input_date = datetime.strptime(date, '%Y-%m-%d') 
    today_date = datetime.now()
    difference = today_date - input_date
    return int(difference.days/365.25)
    
