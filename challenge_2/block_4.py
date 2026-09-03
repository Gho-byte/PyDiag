def sells_analytics(sells_list):
    products = []
    prices = []
    for sell in sells_list:
        try:
            id = products.index(sell['produit'])
            prices[id] += sell['montant']
        except ValueError:
            products.append(sell['produit'])
            prices.append(sell['montant'])
    out_dict = {k:v for k,v in zip(products, prices)}
    max_sells = max(prices)
    print(f'[+] Total par produit : {out_dict}')
    print(f'[+] Meilleur produit : {products[prices.index(max_sells)]} ({max_sells})')
    print(f'[+] Produits distincts : {products}')

def fusionner_inventaires(inv1, inv2):
    products = []
    numbers = []
    for product_name in inv1:
        try:
            existIn = products.index(product_name)
            numbers[existIn] += inv1[product_name]
        except ValueError:
            products.append(product_name)
            numbers.append(inv1[product_name])
    for product_name in inv2:
        try:
            existIn = products.index(product_name)
            numbers[existIn] += inv2[product_name]
        except ValueError:
            products.append(product_name)
            numbers.append(inv2[product_name])
    out_dict = {k:v for k,v in zip(products, prices)}
    print(out_dict)

def mini_challenge(studnets_data):
    names = []
    notes = []
    materials = set()
    materials_data = [] # name, note, how much duplicated
    for student in studnets_data:
    #     try:
    #         existIn = names.index(student['nom'])
    #         notes[existIn] = (notes[existIn] + notes[existIn]) / how_much_material[existIn]
    #     except ValueError:
        names.append(student['nom'])
        materials_notes_sum = 0
        for material_name in student['matieres']:
            materials.add(material_name)
            materials_notes_sum += student['matieres'][material_name]
            found = False
            for material in materials_data:
                try:
                    material.index(material_name)
                    material[1].append(student['matieres'][material_name])
                    material[2] = sum(material[1]) / len(material[1])
                    found = True
                except ValueError:
                    pass
            if not found:
                materials_data.append([
                    material_name,
                    [student['matieres'][material_name]],
                    student['matieres'][material_name]
                ])
        notes.append(materials_notes_sum / len(student['matieres']))
    print('Moyenne par etudiant :\n')
    for id, name in enumerate(names):
        print(f'\t[+] {name}: {notes[id]:.2f}')
    print(f'\n[+] Matieres enseignees (set) : {materials}')
    print(f'\nNotes par matiere :\n')
    for material in materials_data:
        print(f'\t[+] {material[0]} : {material[1]}')
    best_material = [materials_data[0][0], materials_data[0][2]]
    for i in range(1, len(materials_data)):
        if materials_data[i][2] > best_material[1]: best_material = [materials_data[i][0], materials_data[i][2]]
    print(f'[+] Meilleure matiere (moyenne globale) : {best_material[0]} ({best_material[1]:.2f})')

mini_challenge([
{"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
{"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
{"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
])
