def get_min_max(notes):
    min = notes[0] ; max = notes[0]
    for note in notes:
        if note > max:
            max = note
        elif note < min:
            min = note
    print(f'[+] Note Max: {max}')
    print(f'[+] Note Min: {min}')

def notes_au_dessus(notes, seuil):
    output = []
    for note in notes:
        if note >= seuil:
            output.append(note)
    print(output)

def comptage(fruits):
    output = {}
    for fruit in fruits:
        try:
            output[fruit] = output[fruit] + 1
        except KeyError:
            output[fruit] = 1
    if len(output) > 0:
        for element in output:
            print(element)
    else:
        print('[-] Please provide a list')

def reverse_list(input_list):
    output_list = []
    if len(input_list) > 0:
        for i in range(len(input_list) - 1, 0):
            output_list.append(input_list[i])
        print(output_list)
    else:
        print('[-] Please provide a list')

def fusion_lists(list_one, list_two):
    output = set()
    min = len(list_one)
    list_one_is_small = True
    max = len(list_two)
    if max < min:
        tmp = min
        min = max
        max = min
        list_one_is_small = False
    rest = max - min
    for i in range(min):
        if list_one[i] < list_two[i]:
            output.add(list_one[i]) ; output.add(list_two[i])
        elif list_one[i] > list_two[i]:
            output.add(list_two[i]) ; output.add(list_one[i])
        else:
            output.add(list_two[i])
    big_list = list_two if list_one_is_small else list_one
    for i in range(min, max):
        output.add(big_list[i])
    print(list(output))

def comprehension(notes):
    output_list = []
    for note in notes:
        if note % 2 == 0:
            output_list.append(note*note)
    print(output_list)

liste_a = [1, 4, 7]
liste_b = [2, 3, 8, 9]

fusion_lists(liste_a, liste_b)