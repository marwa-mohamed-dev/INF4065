import hashlib
import sys
import random
from verification import verification_sha1 
from verification import verification_MD5 
from Modifierdico import modifier

def dico(type_hash, mdp):

    reponse = input("Voulez-vous rentrer des informations personnelles pour préciser la recherche ?\nTapez 1 si oui ou 0 pour non:")
    if reponse == '1':
        modifier()
        print("Merci pour ces informations")
      #on verifie pour chaque mot de liste créée avec les info personnelles, si le hash est le même 
        with open("test.txt", "r") as testfile:
            if type_hash == 'sha1':
                print("Vérification en cours")
                for line in testfile:
                    word = line.strip()
                    verification_sha1(mdp, word)
                if line not in testfile:
                      print("Le mot de passe n'est pas dans la liste")

            else:
                print("Vérification en cours")
                for line in testfile:
                    word = line.strip()
                    verification_MD5(mdp, word)
                if line not in testfile:
                      print("Le mot de passe n'est pas dans la liste")
             
             
    #on verifie pour chaque mot du dico si le hash est le même
    with open("password.txt", "r") as dico_file:
        print("Vérification en cours")
        if type_hash == 'sha1':
            for line in dico_file:
                word = line.strip()
                verification_sha1(mdp, word)
            if line not in dico_file:
                      print("Le mot de passe n'est pas dans la liste")
        else:
            print("Vérification en cours")
            for line in dico_file:
                word = line.strip()
                verification_MD5(mdp, word)
            if line not in dico_file:
                      print("Le mot de passe n'est pas dans la liste")
