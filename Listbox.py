import tkinter as tk
from tkinter import ttk

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exercices Tkinter – Cybersécurité")
fenetre.geometry("600x500")

onglets = ttk.Notebook(fenetre)
onglets.pack(expand=True, fill='both')

# =================== Exercice 1 – Listbox ===================
cadre1 = ttk.Frame(onglets)
onglets.add(cadre1, text="Exercice 1 – Concepts")

liste = tk.Listbox(cadre1, selectmode=tk.MULTIPLE)
concepts = ["Hameçonnage", "Logiciel malveillant", "Pare-feu", "Chiffrement", "VPN"]
for c in concepts:
    liste.insert(tk.END, c)
liste.pack(pady=10)

def afficher_concepts():
    selection = [liste.get(i) for i in liste.curselection()]
    print("Sélection :", selection)

tk.Button(cadre1, text="Afficher", command=afficher_concepts).pack()

# =================== Exercice 2 – Combobox + Text ===================
cadre2 = ttk.Frame(onglets)
onglets.add(cadre2, text="Exercice 2 – Confidentialité")

def afficher_niveau(event):
    texte.delete("1.0", tk.END)
    if niveau.get() == "Public":
        texte.insert(tk.END, "Aucune restriction")
    elif niveau.get() == "Confidentiel":
        texte.insert(tk.END, "Accès restreint au personnel autorisé")
    elif niveau.get() == "Très Secret":
        texte.insert(tk.END, "Accès limité, autorisation spéciale requise")

niveau = ttk.Combobox(cadre2, values=["Public", "Confidentiel", "Très Secret"])
niveau.bind("<<ComboboxSelected>>", afficher_niveau)
niveau.pack(pady=10)

texte = tk.Text(cadre2, height=4, width=50)
texte.pack()

# =================== Exercice 3 – Nom ===================
cadre3 = ttk.Frame(onglets)
onglets.add(cadre3, text="Exercice 3 – Nom")

champ_nom = tk.Entry(cadre3)
champ_nom.pack(pady=5)

label_nom = tk.Label(cadre3, text="")
label_nom.pack()

def afficher_nom():
    nom = champ_nom.get()
    label_nom.config(text=f"Bonjour, {nom} ! Bienvenue dans le monde de la cybersécurité.")

tk.Button(cadre3, text="Afficher", command=afficher_nom).pack()

# =================== Exercice 4 – Calculatrice ===================
cadre4 = ttk.Frame(onglets)
onglets.add(cadre4, text="Exercice 4 – Calculatrice")

entree1 = tk.Entry(cadre4)
entree2 = tk.Entry(cadre4)
entree1.pack()
entree2.pack()

label_resultat = tk.Label(cadre4, text="")
label_resultat.pack()

def calculer(op):
    try:
        a = float(entree1.get())
        b = float(entree2.get())
        if op == "+":
            resultat = a + b
        elif op == "-":
            resultat = a - b
        elif op == "*":
            resultat = a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError
            resultat = a / b
        label_resultat.config(text=f"Résultat : {resultat}")
    except ValueError:
        label_resultat.config(text="Erreur : veuillez entrer des nombres.")
    except ZeroDivisionError:
        label_resultat.config(text="Division par zéro interdite.")

for symbole in ["+", "-", "*", "/"]:
    tk.Button(cadre4, text=symbole, command=lambda s=symbole: calculer(s)).pack(side=tk.LEFT, padx=5, pady=10)

# =================== Exercice 5 – Mode sécurisé ===================
cadre5 = ttk.Frame(onglets)
onglets.add(cadre5, text="Exercice 5 – Mode sécurisé")

etat_securise = tk.BooleanVar()
check = tk.Checkbutton(cadre5, text="Activer le mode sécurisé", variable=etat_securise)
check.pack(pady=10)

label_securite = tk.Label(cadre5, text="")
label_securite.pack()

def verifier_mode():
    if etat_securise.get():
        label_securite.config(text="Mode sécurisé activé")
    else:
        label_securite.config(text="Mode standard activé")

tk.Button(cadre5, text="Vérifier", command=verifier_mode).pack()

# =================== Exercice 6 – Méthode de chiffrement ===================
cadre6 = ttk.Frame(onglets)
onglets.add(cadre6, text="Exercice 6 – Chiffrement")

methode = tk.StringVar(value="César")
for m in ["César", "Inversion", "ROT13"]:
    tk.Radiobutton(cadre6, text=m, variable=methode, value=m).pack(anchor='w')

label_chiffrement = tk.Label(cadre6, text="")
label_chiffrement.pack()

def confirmer_methode():
    label_chiffrement.config(text=f"Vous avez choisi la méthode : {methode.get()}")

tk.Button(cadre6, text="Confirmer", command=confirmer_methode).pack(pady=10)

# =================== Exercice 7 – Zone d'alerte ===================
cadre7 = ttk.Frame(onglets)
onglets.add(cadre7, text="Exercice 7 – Alerte")

zone_texte = tk.Text(cadre7, height=6, width=50)
zone_texte.pack(pady=10)

def afficher_alerte():
    contenu = zone_texte.get("1.0", tk.END).strip()
    print("Alerte :", contenu)

tk.Button(cadre7, text="Afficher l’alerte", command=afficher_alerte).pack()

# =================== Exercice 8 – Menu Effacer / Quitter ===================
cadre8 = ttk.Frame(onglets)
onglets.add(cadre8, text="Exercice 8 – Menu")

zone_menu = tk.Text(cadre8, height=10, width=60)
zone_menu.pack(pady=10)

def effacer():
    zone_menu.delete("1.0", tk.END)

def quitter():
    fenetre.quit()

# Menu principal
menu_principal = tk.Menu(fenetre)
menu_fichier = tk.Menu(menu_principal, tearoff=0)
menu_fichier.add_command(label="Effacer", command=effacer)
menu_fichier.add_command(label="Quitter", command=quitter)
menu_principal.add_cascade(label="Fichier", menu=menu_fichier)

fenetre.config(menu=menu_principal)

# Boucle principale
fenetre.mainloop()
