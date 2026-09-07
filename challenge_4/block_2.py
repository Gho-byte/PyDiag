def presenter(nom, age):
    return f"{nom} a {age} ans"

def somme(*numbers):
    args = locals()
    output = 0
    for value in args['numbers']:
        output += value
    return output

# somme(1, 2, 3, 4)

def construire_fiche(**infos):
    args = locals()['infos']
    for arg in args:
        print(f'{arg}: {args[arg]}')

# construire_fiche(nom="Ali", age=25, ville="Casablanca")

