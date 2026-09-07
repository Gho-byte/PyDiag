import os

def verify_path(path):
    return os.path.exists(path)

def ecrire_liste_courses(chemin, articles):
    if not verify_path(chemin) or len(articles) == 0: return
    with open(chemin, 'w', encoding='utf-8') as f:
        f.writelines(articles)

def ecrire_liste_courses(chemin, articles):
    if not verify_path(chemin) or len(articles) == 0: return
    with open(chemin, 'w', encoding='utf-8') as f:
        f.writelines(articles)

def ajouter_article(chemin, article):
    if not verify_path(chemin) or len(article) == 0: return
    with open(chemin, 'a', encoding='utf-8') as f:
        f.write(f'\n{article}')

# ajouter_article("courses.txt", "oeufs")

def lire_fichier(chemin):
    if not verify_path(chemin): return
    try:
        f = open(chemin, 'r', encoding='utf-8')
        print(f.readlines())
    except Exception as e:
        print(f'[-] Exception Happend: {e}')
    finally:
        if f:
            f.close()

def compter_lignes(chemin):
    if not verify_path(chemin): return
    with open(chemin, 'r', encoding='utf-8') as f:
        print(f'Nombre de lignes: {len(f.readlines())}')

modes_a_identifier = ["r", "w", "a", "x", "rb", "r+"]
[
    'read a file'
    'write data to file, and this will remove the old data if exist'
    'append data to the exist data in the file'
    'it mean create the file if do not exist, if exist it will cause an error',
    'read the binary of the file'
    'read + write'
]