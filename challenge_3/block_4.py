from block_3 import verify_path
from block_2 import StockInssufisantError
import csv

def lire_fichier_securise(chemin):
    try:
        f = open(chemin, 'r', encoding='utf-8')
        print('Contenu du fichier renvoye sous forme de liste de lignes.')
    except FileNotFoundError:
        print(f'[-] Erreur : le fichier "{chemin}" n\’existe pas.')
    finally:
        if f:
            f.close()

def calculer_moyenne_csv(chemin):
    if not verify_path(chemin):
        print('[-] Le chemin est invalide')
        return
    with open(chemin, 'r') as f:
        data = csv.reader(f)
        valide_notes = 0
        total_notes = 0
        for row in data:
            if row[0] != 'nom':
                try:
                    total_notes += int(row[1])
                    valide_notes += 1
                except ValueError:
                    print(f'Attention : note invalide pour "{row[0]}" ("{row[1]}"), ligne ignoree.')
        if total_notes > 0:
            print(f'Moyenne calculee ({valide_notes} notes valides) : {(total_notes / 3):.2f}')

def app(stock, commands):
    with open('journale.txt', 'w+', encoding='utf-8') as f:
        for command in commands:
            product_name, quantity = command.split(',')
            try:
                try:
                    quantity = int(quantity)
                except ValueError:
                    print(f'[-] La quantite "{stock[product_name]}" pour le produit "{product_name}" est invalide')
                    f.write(f'\n[ERREUR] {product_name} : quantite invalide ("{stock[product_name]}")')
                    continue
                quantity_in_stock = int(stock[product_name])
                if quantity_in_stock < quantity:
                    f.write(f'\n[ERREUR] {product_name} : stock insuffisant (demande {quantity}, dispo {quantity_in_stock})')
                    continue
                stock[product_name] -= quantity
                f.write(f'\n[OK] {product_name} : -{quantity} (reste {stock[product_name]})')
            except KeyError:
                print(f"[-] Le produit {product_name} n'exist pas dans le stock")
                f.write(f'\n[ERREUR] {product_name} : produit inconnue')

stock = {"pommes": 20, "bananes": 4, "oranges": 15}
commandes_brutes = [
    "pommes,5",
    "bananes,10",
    "kiwis,2",
    "oranges,abc",
    "oranges,5",
]


app(stock, commandes_brutes)