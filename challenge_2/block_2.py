def vendre(stock, product, quantity):
    try:
        stock_quantity = stock[product]
        if stock_quantity >= quantity:
            stock[product] = stock_quantity - quantity
            print(f'Vente Enregistree: {quantity} {product}')
        elif stock_quantity < quantity:
            print(f'Stock insuffisant pour {product} (disponible : {stock_quantity})')
    except KeyError:
        print("Le produit que ve voulez acheter n'existe pas")

def produits_epuises(stock):
    output_list = []
    for product_name in stock:
        if stock[product_name] == 0: output_list.append(product_name)
    print(output_list)

def total_per_client(commands):
    names = [] ; quantities = []
    for command in commands:
        try:
            id = names.index(command['client'])
            quantities[id] += command['quantite']
        except ValueError:
            names.append(command['client'])
            quantities.append(command['quantite'])
    for id, name in enumerate(names):
        print(f'[+] {name}: {quantities[id]}')

def reverse_dict(input_dict):
    print({v: k for k, v in input_dict.items()})

def dict_comprehension(input_dict):
    print({k: v for k, v in [(element, len(element)) for element in input_dict]})

def nested_dict(input_dict):
    for departement in input_dict:
        print(f'[+] {departement} : {len(input_dict[departement])} employe(s)')

entreprise = {
"IT": ["Ali", "Sara", "Omar"],
"RH": ["Lina"],
"Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
}

nested_dict(entreprise)