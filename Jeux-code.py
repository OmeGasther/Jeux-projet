import random
import time
import sys

class personnage:
    def __init__(self, nom, points_de_vie, force, mana, CA, Classe, dext, inte, cha):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force
        self.mana = mana
        self.CA = CA
        self.classe = Classe
        self.dext = dext
        self.inte = inte
        self.cha = cha
# demander au joueur les charateristique de sont personnage
nom_confirmed = False
while not nom_confirmed:
    # Demander au joueur de choisir le nom de son personnage
    nom = input("Choisissez le nom de votre personnage : ")
    
    # Demander confirmation du nom
    reponse_nom = input(f"Tu as choisi le nom '{nom}', est-ce correct ? (Y/N) : ").upper()

    # Si le joueur confirme avec 'Y', on sort de la boucle
    if reponse_nom == 'Y':
        nom_confirmed = True
        print(f"Le nom '{nom}' est confirmé !")
    elif reponse_nom == 'N':
        print("Recommençons, choisis un autre nom.")

# Une fois le nom confirmé, on continue avec les autres caractéristiques

import random

# Entrée de la classe
Classe = input("Choisissez votre classe entre Paladin, Mage, Voleur et Barde : ").capitalize()

# Attributions aléatoires des caractéristiques
points_de_vie = random.randint(50, 100)
force = random.randint(-5, 5)
mana = random.randint(0, 100)
inte = random.randint(-5, 5)
dext = random.randint(-5, 5)
cha = random.randint(-5, 5)

  # Définition de la CA (classe d'armure) en fonction de la classe
if Classe == 'Paladin':
        force = 4
        CA = 15
        items = {'Bouclier': {'PV': 5}, 'Potion de soin': {'PV': 10}}
elif Classe == 'Voleur':
        dext = 4
        CA = 12
        items = {'Dague': {'DGT': 4}, 'Potion de furtivité': {'DGT': 0}}
elif Classe == 'Mage':
        mana += 50
        inte = 4
        CA = 8
        items = {'Bâton magique': {'DGT': 3}, 'Potion de mana': {'Mana': 20}}
elif Classe == 'Barde':
        cha = 4
        CA = 12
        items = {'Luth': {'Charisme': 5}, 'Potion de charme': {'Charisme': 10}}
else:
        print("Classe inconnue. Utilisation des valeurs par défaut.")
        CA = 10
        items = {'Objet basique': {'DGT': 1}}

    # Initialisation des caractéristiques du personnage
points_de_vie = random.randint(50, 100)
force = random.randint(-5, 5)
mana = random.randint(0, 100)
inte = random.randint(-5, 5)
dext = random.randint(-5, 5)
cha = random.randint(-5, 5)

print(f"Vos caractéristiques sont : Classe - {Classe}, PV - {points_de_vie}, Force - {force}, Mana - {mana}, CA - {CA}, Dextérité - {dext}, Intelligence - {inte}, Charisme - {cha} !")

#situation test
print("vous entée dans une taverne il y'a un bar une femme lavant des verre et un homme a capuche assie au font que fait vous ?")
femme_points_de_vie = random.randint(30, 50)
femme_force = random.randint(-5, 5)
femme_mana = random.randint(-5, 5)
femme_CA = 12
femme_dext = random.randint(-5, 5)
femme_inte = random.randint(-5, 5)
femme_cha = random.randint(-5, 5)
while True:
    time.sleep(2)
    reponse_taverne = input("Entrez votre réponse (allez voir la femme, allez voir l'homme ou fouiller la taverne) : ").strip().lower()
    time.sleep(2)

    if reponse_taverne == 'femme':
        print("Femme : Bienvenue dans mon humble taverne, voyageur. Comment puis-je vous aider ?")
        reponse_femme = input("Que faites-vous ? (act, fight) : ").strip().lower()
        time.sleep(2)

        if reponse_femme == 'act':
            print("Femme : Que voulez-vous savoir ?")
            femme_act = input("Les prix de la bière, qui est le monsieur, vous êtes libre ce soir ? ").strip().lower()
            time.sleep(2)

            if femme_act == 'les prix de la bière':
                print("Femme : Toutes nos bières sont à 3 pièces de cuivre.")
                time.sleep(2)
                continue
            
            elif femme_act == 'qui est le monsieur':
                print("Femme : Je ne sais pas, il est arrivé ici il y a environ 1 heure sans rien commander. Pour le savoir, vous devriez aller lui parler.")
                time.sleep(2)
                continue
            
            elif femme_act == 'vous êtes libre ce soir':
                resultat_Fact = random.randint(1, 20) + cha
                print(f"Résultat du jet : {resultat_Fact}")
                time.sleep(2)

                if resultat_Fact >= 10:
                    print("Femme : Viens me voir ce soir à 20h30 derrière la taverne.")
                    print("Fin 1")
                    SystemExit  

                elif resultat_Fact < 10:
                    print("Femme : Salopard ! (-5 HP)")
                    points_de_vie -= 5
                    print(f"Vos HP sont maintenant de : {points_de_vie}")
                    time.sleep(2)
                    continue
    

           # Début du combat
    
    print("Entrée en mode combat")

    tour = 1  # Initialisation du compteur de tours

    while True:
        print(f"\nTour {tour}")  # Affichage du tour actuel

        # Le joueur choisit son action parmi les options disponibles
        Fmod = input("Que faites-vous ? (punch, check, item, fuir, sort) : ").strip().lower()

        if Fmod == 'punch':
            # Jet d'attaque du joueur
            resultat_FF = random.randint(1, 20) + force
            if resultat_FF >= femme_CA:
                # Si l'attaque réussit
                resultat_dgt = random.randint(1, 4)
                femme_points_de_vie -= resultat_dgt  # Réduction des PV de la femme
                print(f"Vous avez infligé {resultat_dgt} points de dégâts à la femme.")
                print(f"Il lui reste {femme_points_de_vie} points de vie.")
            else:
                print("Votre attaque a échoué.")

        elif Fmod == 'check':
            # Action pour vérifier l'état de l'ennemi
            print(f"La femme a encore {femme_points_de_vie} points de vie.")

        elif Fmod == 'item':
            # Affichage des objets et utilisation d'un objet
            print("Vous avez les objets suivants :")
            for item, stats in items.items():
                print(f"{item} (PV: {stats.get('PV', 0)}, DGT: {stats.get('DGT', 0)}, Charisme: {stats.get('Charisme', 0)})")
            item_choisi = input("Quel objet souhaitez-vous utiliser ? ").strip()

            if item_choisi in items:
                if 'PV' in items[item_choisi]:
                    points_de_vie += items[item_choisi]['PV']  # Soigne le joueur
                    print(f"Vous avez utilisé {item_choisi}. Vous avez récupéré {items[item_choisi]['PV']} points de vie.")
                elif 'DGT' in items[item_choisi]:
                    # Lancer une attaque avec l'objet
                    resultat_dgt = items[item_choisi]['DGT']
                    femme_points_de_vie -= resultat_dgt
                    print(f"Vous avez infligé {resultat_dgt} points de dégâts avec votre {item_choisi}.")
                elif 'Charisme' in items[item_choisi]:
                    cha += items[item_choisi]['Charisme']
                    print(f"Vous avez utilisé {item_choisi}. Votre charisme est maintenant de {cha}.")
            else:
                print("Objet non reconnu.")

        elif Fmod == 'sort' and Classe == 'Mage':
            # Utilisation des sorts du Mage
            sort_choisi = input("Quel sort souhaitez-vous utiliser ? (boule de feu, éclaire) : ").strip().lower()
            if sort_choisi == 'boule de feu':
                resultat_dgt = random.randint(6, 10)  # Dégâts de la boule de feu
                femme_points_de_vie -= resultat_dgt
                print(f"Vous avez lancé une boule de feu, infligeant {resultat_dgt} points de dégâts à la femme.")
            elif sort_choisi == 'éclaire':
                resultat_dgt = random.randint(4, 8)  # Dégâts de l'éclaire
                femme_points_de_vie -= resultat_dgt
                print(f"Vous avez lancé un éclaire, infligeant {resultat_dgt} points de dégâts à la femme.")
            else:
                print("Sort non reconnu.")

        elif Fmod == 'fuir':
            # Si le joueur choisit de fuir, le combat se termine
            print("Vous avez décidé de fuir le combat.")
            print("Fin du combat.")
            sys.exit()  # Termine le jeu si le joueur fuit

        # Vérification si la femme est vaincue
        if femme_points_de_vie <= 0:
            print("La femme est vaincue.")
            cha -= 5  # Réduction du charisme
            print(f"-5 à votre charisme. Votre charisme est maintenant de {cha}.")
            break  # Le combat est terminé

        # L'ennemi (la femme) attaque automatiquement après chaque tour du joueur
        if Fmod != 'fuir':  # Vérifie que le joueur n'a pas fui avant d'attaquer
            resultat_femme = random.randint(1, 20) + femme_force
            if resultat_femme >= CA:  # Jet d'attaque contre le joueur
                femme_dgt = random.randint(1, 6)  # Dégâts de la femme
                points_de_vie -= femme_dgt
                print(f"La femme vous attaque et inflige {femme_dgt} points de dégâts.")
                print(f"Il vous reste {points_de_vie} points de vie.")
            else:
                print("L'attaque de la femme a échoué.")

        # Vérification des points de vie du joueur
        if points_de_vie <= 0:
            print("Vous avez été vaincu. Game Over.")
            sys.exit()  # Termine le jeu en cas de défaite

        # Incrémentation du compteur de tours
        tour += 1