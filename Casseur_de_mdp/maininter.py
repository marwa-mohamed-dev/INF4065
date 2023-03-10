# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter as tk
from tkinter import ttk
from tkinter import font
import tkinter.font as font
from dictionnaire import dico
from dictionnaire import info_perso
from brute_force import bf

root = tk.Tk()
root.withdraw()


open('motnombre.txt', 'w').close()
open('perso1.txt','w').close()
open('test.txt','w').close()

myFont =font.Font(family ="Comic Sans MS",size = 100)

def Close(window):
    window.destroy()


def menu(window):
    btn_retour = tk.Button(window, text="Menu",command=lambda: [w_accueil(), Close(window)])
    btn_retour.pack(pady=10)


def w_accueil():
    accueil = tk.Tk()
    accueil.title("KAH_RA")
    accueil.geometry("2048x1780")
    kahra = tk.Label(accueil, text="Bienvenue sur KAH-RA!", font=myFont, background='#642080')
    kahra.pack()
    accueil.config(background='#642080')
    btn_instru = tk.Button(accueil,text="Aide", font = myFont, command=lambda: [w_aide(), Close(accueil)])
    btn_instru['font']=myFont
    btn_code = tk.Button(accueil, text="Décrypter", command=lambda: [w_code(), Close(accueil)])
    btn_instru.pack(pady=10)
    btn_code.pack(pady=10)
    w_quitter(accueil)


def w_code():
    crack = tk.Tk()
    crack.title("KAH-RA")
    crack.geometry("2048x1780")
    kahra = tk.Label(crack, text="Savez-vous quel algorithme de hashage a été utilisé?", background = '#642080',font=myFont)
    #bla = label(crack, text="connaissez vous l'algorithme du hash\nque vous souhaiez casser?", font=("Arial", 25))
    kahra.pack()
    #bla.pack()
    crack.config(background='#642080')
    kahra.configure(font=myFont)
    btn_oui = tk.Button(crack, text="Oui", command=lambda: [choix_hash(), Close(crack)])
    btn_non = tk.Button(crack, text="Non", command=lambda: [w_erreur(), Close(crack)])
    btn_oui.pack(pady=10)
    btn_non.pack(pady=10)
    menu(crack)
    w_quitter(crack)


def w_aide():
    Aide = tk.Tk()
    Aide.title("KAH-RA")
    Aide.geometry("2048x1780")
    kahra = tk.Label(Aide, text="Aide\n", background = '#642080',font=("Arial", 30))
    force = tk.Label(Aide, text="Force brute:\n", background = '#642080',foreground = 'white',font=("Arial", 25))
    dico = tk.Label(Aide, text="Dictionnaire:\n", background = '#642080',foreground = 'white',font=("Arial", 25))
    plaintxt = tk.Label(Aide,
                     text="Nous allons créer des combinaisons de lettres. Chacune de ces\n combinaisons sera transformée en hash et le hash obtenu sera\n comparé au hash que vous avez rentré. Si les deux correspondent\n nous avons trouvé votre mot de passe.",
                     background = '#642080',font=("Arial", 20))
    plntxt = tk.Label(Aide,
                   text="Nous allons comparer votre hash avec une liste de mots couramment utilisés, ceux-ci seront\ntransformés en hash et comparés au hash que vous avez rentré.\nSi ils sont semblables, nous aurons réussi à le casser.\nAfin d'augmenter nos chances de réussite, nous demanderons aussi des informations personnelles\nsur le propriétaire du hash afin d'adapter nos recherches.\nDes mots de passe seront créés basés sur ces informations et seront les premiers à être vérifiés.\n",
                   background = '#642080',font=("Arial", 20))
    kahra.pack()
    force.pack()
    plaintxt.pack()
    dico.pack()
    plntxt.pack()

    Aide.config(background='#642080')
    menu(Aide)
    w_quitter(Aide)


def w_credits():
    Credits = tk.Tk()
    Credits.title("KAH_RA")
    Credits.geometry("2048x1780")
    Test = tk.Label(Credits, text="Credits",background = '#642080', font=("Arial",30))
    cred = tk.Label(Credits, text="Ce programme a été réalisé dans le cadre des PST2 2020-2021 par EL ADA Hana, ESCHYLLE Annaly, MAILLOT Chloé, \nOUBRHAM Cyrine, RABENANDRASNA Riana et TREBLA Alycia.Nous remercions nos suiveurs FOURNIER Manon\n et BRIERE Alexandre pour leur aide et leur soutien.\n\n", background = '#642080',font=("Arial",15))
    djkhaled =  tk.Label(Credits, text="Merci d'avoir utilisé KAH-RA à bientôt :)\n",background = '#642080', font=("Arial", 25))
    anotherone= tk.Label(Credits, text="They hide it,\nwe break it !",background = '#642080',font=("Arial",15))
    Test.pack()
    cred.pack()
    djkhaled.pack()
    menu(Credits)
    w_exit(Credits)
    anotherone.pack()
    Credits.config(background='#642080')

def value_choice(value):
    global TYPE_HASH
    TYPE_HASH = value

def choix_hash():
    Choix = tk.Tk()
    Choix.title("KAH-RA")
    Choix.geometry("2048x1780")
    Choix.config(background='#642080')
    lab_typehash= tk.Label(Choix, text = "Quel est l'algorithme de hashage utlisé ?", background ='#642080', foreground = 'white', font = ("Courier New",30))
    btn_SHA1 = tk.Button(Choix, text="SHA1", command=lambda: [value_choice(1),h_input(),Close(Choix)])
    btn_MD5 = tk.Button(Choix, text="MD5", command=lambda: [value_choice(2),h_input(), Close(Choix)])
    lab_typehash.pack()
    btn_SHA1.pack(pady=10)
    btn_MD5.pack(pady=10)
    menu(Choix)
    w_quitter(Choix)


def h_input():
    w_hash = tk.Tk()
    w_hash.title("KAH_RA")
    w_hash.geometry("2048x1780")
    w_hash.config(background='#642080')
    global var_hash
    var_hash = tk.StringVar(w_hash)
    BOX_input_hash = tk.Entry(w_hash, textvariable=var_hash)
    BOX_input_hash.pack()
    valider = tk.Button(w_hash, text="Valider", command=lambda: [fonction(), Close(w_hash)])
    valider.pack(pady=10)
    menu(w_hash)
    w_quitter(w_hash)


def fonction():
    w_fonction = tk.Tk()
    w_fonction.title("KAH_RA")
    w_fonction.geometry("2048x1780")
    w_fonction.config(background='#642080')
    global input_hash
    input_hash = var_hash.get()
    btn_dico = tk.Button(w_fonction, text="Dictionnaire", command=lambda: [info(), Close(w_fonction)])
    btn_brute = tk.Button(w_fonction, text="Force brute", command=lambda: [resultat_bf(TYPE_HASH,input_hash), Close(w_fonction)])
    btn_brute.pack(pady=10)
    btn_dico.pack(pady=10)
    menu(w_fonction)
    w_quitter(w_fonction)


def info():
    w_info = tk.Tk()
    w_info.title("KAH-RA")
    w_info.geometry("2048x1780")
    w_info.config(background='#642080')
    label_info = tk.Label(w_info, text="Voulez-vous rentrer des informations personelles ?",background = '#642080',font=("Arial", 30))
    btn_oui = tk.Button(w_info, text="Oui", command=lambda: [info_input(), Close(w_info)])
    btn_non = tk.Button(w_info, text="Non", command=lambda: [resultat_dico(TYPE_HASH, input_hash), Close(w_info)])
    label_info.pack(pady=10)
    btn_oui.pack(pady=10)
    btn_non.pack(pady=10)
    menu(w_info)
    w_quitter(w_info)

def delete(input):
    input.delete(0, "end")


def Stock_info(w_info_input, BOX_input_info) :
    Fichier = open ("perso1.txt", 'a+')
    input_info = var_word.get()
    print("mot =", var_word.get())
    Fichier.write(input_info)
    Fichier.write("\n")
    Fichier.close()

def info_input():
    w_info_input = tk.Tk()
    w_info_input.title("KAH-RA")
    w_info_input.geometry("2048x1780")
    global var_word
    var_word=tk.StringVar(w_info_input)
    global input_info
    BOX_input_info = tk.Entry(w_info_input,textvariable=var_word)
    valider = tk.Button(w_info_input, text="Valider",
                     command=lambda: [Stock_info(w_info_input, BOX_input_info), resultat_perso(TYPE_HASH, input_hash),Close(w_info_input)])
    suivant = tk.Button(w_info_input, text="Suivant",
                     command=lambda :[Stock_info(w_info_input, BOX_input_info), delete(BOX_input_info)])
    BOX_input_info.pack()
    w_info_input.config(background='#642080')
    suivant.pack(pady=10)
    valider.pack(pady=10)
    menu(w_info_input)
    w_quitter(w_info_input)


def resultat_dico(algo, hash):
    
    mdp=dico(algo,hash)
    if(mdp == '1') :
        Error()
    else:
        w_res = tk.Tk()
        w_res.title("KAH-RA")
        w_res.geometry("2048x1780")
        Label_res = tk.Label(w_res, text="Le mot de passe est: ", background = '#642080',font=("Arial", 40))
        affi_res = tk.Label(w_res, text=mdp,background = '#642080', font=("Arial", 40))
        Label_res.pack()
        affi_res.pack()
        Label_res.config()
        w_res.config(background='#642080')
        menu(w_res)
        w_quitter(w_res)
    

def resultat_perso(algo, hash):
    
    mdp=info_perso(algo,hash)
    if(mdp == '1') :
        Error()
    else:
        w_res = tk.Tk()
        w_res.title("KAH-RA")
        w_res.geometry("2048x1780")
        Label_res = tk.Label(w_res, background='#642080', text="Le mot de passe est: ", font=("Arial", 40))
        affi_res = tk.Label(w_res, text=mdp, font=("Arial", 40))
        Label_res.pack()
        affi_res.pack()
        Label_res.config()
        w_res.config(background='#642080')
        menu(w_res)
        w_quitter(w_res)


def resultat_bf(algo,hash):
    w_res = tk.Tk()
    w_res.title("KAH-RA")
    w_res.geometry("2048x1780")
    Label_res = tk.Label(w_res, background = '#642080',text="Afficher resultat")
    mdp = bf(algo,hash)
    print("final mdp=", mdp)
    affi_hash = tk.Label(w_res, background = '#642080',text=mdp)
    Label_res.pack()
    affi_hash.pack()
    w_res.config(background='#642080')
    menu(w_res)
    w_quitter(w_res)

def Error():
    error = tk.Tk()
    error.title("KAH_RA")
    error.geometry("2048x1780")
    lbl = tk.Label(error, text="Veuillez nous excuser mais votre mot de passe n'est pas dans la liste prédéfinie, désolé.",background = '#642080',font=("Arial",20))
    lbl.pack()
    error.config(background='#642080')
    menu(error)
    w_quitter(error)

def delete(input):
    input.delete(0, "end")

def w_erreur():
    erreur = tk.Tk()
    erreur.title("KAH_RA")
    erreur.geometry("2048x1780")
    lbl = tk.Label(erreur,background = '#642080', text="Veuillez nous excuser mais nous ne sommes pas encore en mesure \nde proposer une détection d'algorithme pour l'instant.",font=("Arial",20))
    lbl.pack()
    erreur.config(background='#642080')
    menu(erreur)
    w_quitter(erreur)


def w_quitter(window):
    btn_quitter = tk.Button(window, text="Quitter", command=lambda: [w_credits(), Close(window)])
    btn_quitter.pack(pady=10)


def w_exit(window):
    btn_exit = tk.Button(window, text="Quitter", command=quitter)
    btn_exit.pack(pady=10)


def quitter():
    quit()


w_accueil()
# mainloop, runs infinitely
tk.mainloop()
