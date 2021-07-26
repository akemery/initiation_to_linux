#!/bin/python3
import sys

filename = sys.argv[1]
texts = [ "Linux ou GNU/Linux est une famille de systèmes d'exploitation open source de type Unix fondé sur le noyau Linux, créé en 1991 par Linus Torvalds",  "De nombreuses distributions Linux ont depuis vu le jour et constituent un important vecteur de popularisation du mouvement du logiciel libre", "Si à l'origine, Linux a été développé pour les ordinateurs compatibles PC, il n'a jamais équipé qu'une très faible part des ordinateurs personnels", "Mais le noyau Linux, accompagné ou non des logiciels GNU, est également utilisé par d'autres types de systèmes informatiques, notamment les serveurs, téléphones portables, systèmes embarqués ou encore superordinateurs", "Le système d'exploitation pour téléphones portables Android qui utilise le noyau Linux mais pas GNU, équipe aujourd'hui 85 % des tablettes tactiles et smartphones" ]

for i in range(100):
     print(texts[i%5], file=open(filename, "a"))