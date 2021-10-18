from random import randint, shuffle



# support functions
def select_3_items(obj: list):
    selecteds = []
    
    while len(selecteds) < 3:
        selected = randint(0, len(obj) - 1)
        if selected not in selecteds:
            selecteds.append(selected)
    
    return [obj[number] for number in selecteds]
        



# main functions
def draw_questions(sets_of_questions):
    if sets_of_questions is None:
        return None
    new_sets = []

    for set_questions in list(sets_of_questions):
        if len(set_questions) > 3:
            new_sets.append(select_3_items(set_questions))
        else:
            new_sets.append(set_questions)
    
    return new_sets    