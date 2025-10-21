#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def creat_horse(nb) :
	"""
	Creation des chevaux
	:param nb:
	:return:
	"""
	horse = []
	for i in range(nb) :
		horse.append({
			"nom": f"Cheval {i+1}",
			"vitesse": 0,
			"distance":0,
			"disqualifie": False
		})
	return horse

def dice_roll():
	"""Renvoie un nombre 'int' de dé aleatoire entre 1 et 6"""
	return random.randint(1,6)

def speed_evolution(speed, roll) :
	"""

	:param speed (int): Vitesse actuelle du cheval (0 à 6).
	:param roll (int): Résultat du dé (1 à 6)
	:return:
		Retourne la nouvelle vitesse selon le tableau donner ou None si disqualification.
	"""

	table = {
		0: [0, +1, +1, +1, +2, +2],
		1: [0, 0, +1, +1, +1, +2],
		2: [0, 0, +1, +1, +1, +2],
		3: [-1, 0, 0, +1, +1, +1],
		4: [-1, 0, 0, 0, +1, +1],
		5: [-2, -1, 0, 0, 0, +1],
		6: [-2, -1, 0, 0, 0, "DQ"],
	}
	variation = table[speed][roll-1]
	if variation == "DQ" :
		return None 	# disqualification
	return max(0, speed + variation) # on renvoie la nouvelle vitesse, sans descendre sous 0.

def distance_traveled(speed):
	"""
	Retourne la distance parcourue selon la vitesse.

	:param speed:
	:return:
	"""
	table = [0, 23, 46, 69, 92, 115, 138]
	return table[speed]

def race_tour(horses):
	"""
	Effectue un tour de course pour chaque cheval.

	:param horses:
	:return:
	"""
	for horse in horses:
		if horse["disqualifie"]:
			continue

		roll = dice_roll()
		new_speed = speed_evolution(horse["vitesse"], roll)

		if new_speed is None:
			horse["disqualifie"] = True
			print(f"{horse['nom']} is disqualified !")
			continue

		horse["vitesse"] = new_speed
		horse["distance"] += distance_traveled(horse["vitesse"])

def race_simulator(nb_horses, race_type):
	"""

	:param nb_horses:
	:param race_type:
	:return:
	"""
	horses = creat_horse(nb_horses)
	arrival = 2400
	time = 0

	print("\n--- Début de la course ---\n")

	while any(not h["disqualifie"] and h["distance"] < arrival for h in horses):
		input("Appuyez sur Entrée pour lancer le tour suivant...")
		time += 10

		race_tour(horses)


		ranking = sorted(
			[h for h in horses if not h["disqualifie"]],
			key=lambda  x: x["distance"],
			reverse=True
		)

		print(f"\n--- Tour {time // 10} (total times : {time}s) ---\n" )
		for H in ranking:
			barre = "=" * (H["distance"] // 50)
			print(f"{H['nom']:10} | {barre:50} | {H['distance']:4.0f} m ({H['vitesse']})")

	print("\n--- Fin de la course ---\n")
	print("Classement final :")
	final_ranking = sorted(horses, key=lambda x: x["distance"], reverse=True,)
	for i, h in enumerate(final_ranking[:race_type]):
		print (f"{i+1}. {h['nom']} - {h['distance']:.0f} m")


if __name__ == "__main__":
	nb = int(input("Nombre de chevaux (12 à 20) : "))
	race_type = int(input("Type de course (3=tiercé, 4=quarté, 5=quinté) : "))
	race_simulator(nb, race_type)

	"""test = creat_horse(15)
	print(len(test))
	for h in test:
		print(h["nom"])"""


