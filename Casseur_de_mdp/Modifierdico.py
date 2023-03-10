import random
#On crée un dictionnaire avec toutes les variations possibles de chaque lettre
rand_dict = {
    "A": ["@", "a", "A"],
    "B": ["b", "3", "B"],
    "C": ["c", "(", "C"],
    "D": ["D", "d", "6"],
    "E": ["E", "e", "3"],
    "F": ["F", "f"],
    "G": ["6", "G", "g", "9"],
    "H": ["h", "H"],
    "I": ["I", "i", "!","1"],
    "J": ["J", "j"],
    "K": ["k", "K"],
    "L": ["l", "L", "1"],
    "M": ["m", "M"],
    "N": ["n", "N"],
    "O": ["O", "o", "0"],
    "P": ["p", "P"],
    "Q": ["Q", "q"],
    "R": ["R", "r"],
    "S": ["s", "S", "$"],
    "T": ["T", "t"],
    "U": ["U", "u"],
    "V": ["v", "V", "<"],
    "W": ["w", "W"],
    "X": ["x", "X"],
    "Y": ["Y", "y"],
    "Z": ["z", "Z"],
    "!": ["!"],
    "$": ["$"],
    "-": ["-"],
    "_": ["_"],
    "@": ["@"],
    ".": ["."],
    "'": ["'"],
    "/": ["/"],
    "+": ["+"],
    "#": ["#"],
    "(": ["("],
    ")": [")"],
    "1": ["1"], "2": ["2"], "3": ["3"], "4": ["4"], "5": ["5"], "6": ["6"], "7": ["7"], "8": ["8"], "9": ["9"],
    "0": ["0"],
}

#On vérifie si il y a des doublons dans la liste créee à partir des informations personelles. Si oui, on les supprime
def checkdouble():
    print("Vérification des doublons")
    ls = []
    try:
        with open("test.txt", 'r') as file:

            for line in file:
                if line not in ls:
                    ls.append(line)

        with open("test.txt", 'w') as file:
            for line in ls:
                file.write(line)
            

    except IOError as err:
        print('Code de l\'erreur : ', err)
        print('Le fichier n\'existe probablement pas')

    #input('')

def modifier():
    info = '1'
    while info != '0':
      info=input("Rentrez des informations personnelles. Tapez 0 pour arrêter:")
      with open("perso1.txt", "a") as perso:
      #On imprime l'input de l'user dans le fichier texte perso1
          if info != '0':
              perso.write(info + "\n")

    with open("perso1.txt", "r") as infoinput:
        with open("motnombre.txt", 'a') as dico_file:
            for line in infoinput:
                word = line.strip()
                dico_file.write("\n" + word)
                #On crée 100 versions du mot avec un nombre à la suite (ex1, ex2, ex3...)
                for i in range(0, 101):
                    motchiffre = (word + "%d" % i)
                    dico_file.write("\n" + motchiffre)
    with open("motnombre.txt", "r") as infoinput:
        with open("test.txt", 'a') as dico_file:
          for line in infoinput:
                word = line.strip()
                for i in range(1,150):
                    bar = []
                    for i in list(word.upper()):
                        random.shuffle(rand_dict[i], random.random)
                        bar.append(rand_dict[i][0])
                    nouveaumot = ''.join(str(elem) for elem in bar)
                    #On imprime le nouveau mot dans le fichier texte test
                    dico_file.write("\n" + nouveaumot)
    checkdouble()
