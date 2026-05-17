score = 0

def poser_question(question, reponse_correcte, choix):
    print("\n" + question)
    for i, c in enumerate(choix, 1):
        print(f"  {i}. {c}")
    reponse = input("Votre réponse (numéro) : ")
    if choix[int(reponse) - 1].lower() == reponse_correcte.lower():
        print("✅ Bonne réponse !")
        return 1
    else:
        print(f"❌ Mauvaise réponse. La bonne réponse était : {reponse_correcte}")
        return 0

def questions_geographie():
    global score
    print("\n--- 🌍 Géographie ---")
    score += poser_question(
        "Quelle est la capitale de l'Australie ?",
        "Canberra",
        ["Sydney", "Melbourne", "Canberra", "Brisbane"]
    )
    score += poser_question(
        "Quel est le plus grand océan du monde ?",
        "Pacifique",
        ["Atlantique", "Indien", "Pacifique", "Arctique"]
    )
    score += poser_question(
        "Dans quel pays se trouve le Machu Picchu ?",
        "Pérou",
        ["Mexique", "Pérou", "Brésil", "Colombie"]
    )