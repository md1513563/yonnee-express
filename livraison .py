print("=== Yonnee Express : saisie des livraisons ===")
TARIFS = {
    "MEDINA": 1000,
    "Plateau": 1500,
    "Yoff": 2000,
    "Parcelles": 2000,
    "Pikine": 2500,
}
SUPPLEMENT_LOURD = 500
POIDS_LOURD = 5
MONTANT_MIN = 500
MONTANT_MAX = 500_000

def lire_entier(question, minimum, maximum):
    while True:
        texte = input(question)
        try:
            valeur = int(texte.strip())
        except ValueError:
            print(f"{texte} n'est pas un entier valide. Veuillez réessayer.")
            continue
        if minimum <= valeur <= maximum:
            return valeur
        print(f"Veuillez entrer un entier entre {minimum} et {maximum}.")

nb = lire_entier("Nombre de colis (1 à 20) : ",1,20)
print("Colis à livrer :", nb)
