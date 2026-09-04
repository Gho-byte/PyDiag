def verifier_age(age):
    if age < 0:
        raise ValueError(f"l’age ne peut pas etre negatif ({age}).")
    print(f'[+] Age valide : {age}')

def traiter_liste_de_valeurs(input_list):
    output_list = []
    for item in input_list:
        try:
            output_list.append(int(item))
        except ValueError:
            print(f'Log : valeur "{item}" invalide, exception relancee.')
            raise

class StockInssufisantError(Exception):
    def __init__(self, message):
        super().__init__(message)

def retirer_stock(stock, product_name, quantity):
    for product in stock:
        if product == product_name:
            if stock[product_name] < quantity:
                raise StockInssufisantError(f'stock insuffisant pour "{product_name}"\n(demande : {quantity}, disponible : {stock[product_name]})')
            else:
                stock[product_name] -= quantity
                print(f'[+] Retrait effectue : {product_name} {quantity}')
                return
    print('[-] Ce produit n\'existe pas dans le stock')
