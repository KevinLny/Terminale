while True:
    try:
        open(input("Le nom du fichier :"), "r")
        break
    except ValueError:
        print("Le fichier n'existe pas...")