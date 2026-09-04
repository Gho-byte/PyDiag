def devision_securesee(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('[-] Erreur : division par zero impossible.')

def convertir_entier(input):
    try:
        return int(input)
    except ValueError:
        print(f'[-] Erreur : "{input}"' + "n’est pas un entier valide.")

def acceder_element(notes, index):
    try:
        return notes[index]
    except IndexError:
        print(f'[-] Erreur : index {index} hors limites (taille de la liste : {len(notes)}).')

def acceder_cle(dict, key):
    try:
        return dict[key]
    except KeyError:
        print(f'[-] Erreur : la cle "{key}"' + "n’existe pas.")

def traiter_valeur(number):
    try:
        print(f'[+] Conversion reussie : {int(number)}')
    except ValueError:
        print(f'[-] Erreur : "{number}"' + "n’est pas un entier valide.")
    finally:
        print('Traitement termine.')