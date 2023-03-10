import hashlib

def verification_sha1 (hash, mdp) :
  if(hashlib.sha1(mdp.encode()).hexdigest() == hash) :
    print("Le mot de passe est : ", mdp)
    quit()

def verification_MD5 (hash, mdp) :
  if(hashlib.md5(mdp.encode()).hexdigest() == hash) :
    print("Le mot de passe est : ", mdp)
    quit() 