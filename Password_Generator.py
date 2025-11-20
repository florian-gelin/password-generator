from hashlib import sha256
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('La longueur du mot de passe devrait être au moins de 6')
        val = False
        
    elif len(passwd) > 20:
        print('La longueur du mot de passe devrait être inférieur à 20')
        val = False

    elif not any(char.isdigit() for char in passwd):
        print('Le mot de passe doit comporter au moins un chiffre')
        val = False

    elif not any(char.isupper() for char in passwd):
        print('Le mot de passe doit comporter au moins une lettre majuscule')
        val = False

    elif not any(char.islower() for char in passwd):
        print('Le mot de passe doit comporter au moins une minuscule')
        val = False

    elif not any(char in SpecialSym for char in passwd):
        print('Le mot de passe doit comporter au moins un symbole $@#%')
        val = False

    return val

def main():
    passwd = input("Veuillez saisir un mot de passe: ")
    if password_check(passwd):
        print("Votre mot de passe est validé !")
        mdp_crypt = sha256(passwd.encode('utf-8')).hexdigest()
        print(mdp_crypt)
    else:
        print("Erreur de mot de passe")
        return main()

main()