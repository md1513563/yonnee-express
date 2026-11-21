from datetime import date, datetime
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

# nb = lire_entier("Nombre de colis (1 à 20) : ",1,20)
# print("Colis à livrer :", nb)
def verifier_montant(montant):
    if not (MONTANT_MIN <= montant <= MONTANT_MAX):
       raise ValueError(f"Le montant doit être compris entre {MONTANT_MIN} et {MONTANT_MAX}.")
    return montant
def lire_montant(question):
    while True:
        texte = input(question).replace(" ", "")
        try:
            montant = int(texte)
            return verifier_montant(montant)
        except ValueError as e:
            print(f"Montant refusé ({e})")

# montant_valide = lire_montant("Montant à envoyer (500 à 500 000 F) : ")
# print(f"{montant_valide} est accepté")

def lire_poids(question):
    while True:
        texte = input(question).strip().replace(",", ".")
        try:
            poids = float(texte)
        except ValueError:
            print(f"« {texte} » n'est pas un poids.")
            continue
        if poids <= 0:
            print("Le poids doit être positif.")
            continue
        return poids

# poids_colis = lire_poids("Poids du colis (kg) : ")
# print(f"{poids_colis} kg est accepté")

def lire_date(question):
    while True:
        texte = input(question).strip()
        try:
            jour = datetime.strptime(texte, "%d/%m/%Y").date()
        except ValueError:
            print(f"« {texte} » n'est pas une date valide (format attendu : jj/mm/aaaa).")
            continue
        if jour > date.today():
            print("La date ne peut pas être dans le futur.")
            continue
        return jour

# date_colis = lire_date("Date d'expédition (JJ/MM/AAAA) : ")
# print(f"Date acceptée : {date_colis.strftime('%d/%m/%Y')}")

def lire_quartier(question):
    quartiers_possibles = ", ".join(TARIFS.keys())
    while True:
        saisie = input(question).strip().lower()
        for quartier in TARIFS:
            if quartier.lower() == saisie:
                return quartier
        print(f"Quartier inconnu. Quartiers possibles : {quartiers_possibles}")

def frais_livraison(quartier, poids):
    if poids <= 0:
        raise ValueError("le poids doit être positif")
    if quartier not in TARIFS:
        raise KeyError(f"quartier non desservi : {quartier}")

    total = TARIFS[quartier]
    if poids > POIDS_LOURD:
        total += SUPPLEMENT_LOURD
    return total

def saisir_livraison():
    d = lire_date("Date (JJ/MM/AAAA) : ")
    quartier = lire_quartier("Quartier : ")
    poids = lire_poids("Poids (kg) : ")
    montant = lire_montant("Valeur du colis (F) : ")
    frais = frais_livraison(quartier, poids)
    return {
        "date": d,
        "quartier": quartier,
        "poids": poids,
        "montant": montant,
        "frais": frais,
    }


def afficher(livraison: dict) -> None:
    print(
        f"{livraison['date']:%d/%m/%Y} | "
        f"{livraison['quartier']:<9} | "
        f"{livraison['poids']:>5.1f} kg | "
        f"{livraison['montant']:>7} F | "
        f"Frais : {livraison['frais']:>5} F"
    )


def main() -> None:
    nb = lire_entier("Nombre de livraisons (1 à 20) : ", 1, 20)
    livraisons = []

    for i in range(1, nb + 1):
        print(f"\n--- Livraison {i}/{nb} ---")
        livraisons.append(saisir_livraison())

    print("\n=== Récapitulatif ===")
    total_frais = 0
    for livraison in livraisons:
        afficher(livraison)
        total_frais += livraison["frais"]

    print(f"Total des frais : {total_frais} F")


if __name__ == "__main__":
    main()