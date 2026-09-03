def intersection_union_difference(python_data, java_data):
    union = set()
    only_python = set()
    for id in range(len(python_data)):
        try:
            result = python_data.index(java_data[id])
            union.add(java_data[id])
        except ValueError:
            pass
    for python_student in python_data:
        try:
            id = java_data.index(python_student)
        except ValueError:
            only_python.add(python_student)
    print(f'[+] Inscrits aux deux ateliers : {union}')
    print(f'[+] Inscrits a au moins un atelier : {set(python_data + java_data)}')
    print(f'[+] Uniquement Python :{only_python}')

def detection_des_doublons(input_list):
    for item in input_list:
        if input_list.count(item) > 1: return True
    return False

def unique_set(nested_list):
    output_set = set()
    for sub_list in nested_list:
        output_set.add(sub_list)
    return output_set