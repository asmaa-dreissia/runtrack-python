def moyenne (note1, note2, note3):
    return((note1 + note2 + note3) / 3)

note1 = float(input("Entrez la note 1:"))
note2 = float(input("Entrez la note 2:"))
note3 = float(input("Entrez la note 3:"))

moyenne_etudiant= moyenne(note1, note2, note3)

if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
    print("Trés bon élève, votre moyenne est de", moyenne_etudiant)

if moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
    print("Bon élève, votre moyenne est de", moyenne_etudiant)

if moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
    print("Elève Moyen, votre note est de", moyenne_etudiant)

if moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
    print("Elève devant faire des efforts votre moyenne est de", moyenne_etudiant)





