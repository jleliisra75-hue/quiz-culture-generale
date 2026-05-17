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
    # Thèmes : Sciences & Sport

def questions_sciences():
    global score
    print("\n--- 🔬 Sciences ---")
    score += poser_question(
        "Quelle planète est la plus proche du soleil ?",
        "Mercure",
        ["Vénus", "Mercure", "Mars", "Terre"]
    )
    score += poser_question(
        "Combien d'os a le corps humain adulte ?",
        "206",
        ["150", "206", "312", "98"]
    )

def questions_sport():
    global score
    print("\n--- ⚽ Sport ---")
    score += poser_question(
        "Combien de joueurs dans une équipe de football ?",
        "11",
        ["9", "10", "11", "12"]
    )
    score += poser_question(
        "Dans quel pays ont eu lieu les JO 2024 ?",
        "France",
        ["Japon", "USA", "France", "Espagne"]
    )

    def afficher_regles():
    print("\n📋 Règles du jeu :")
    print("  - Répondez en tapant le numéro de votre choix")
    print("  - 9 questions au total")
    print("  - 1 point par bonne réponse")
    print("  - Bonne chance !\n")

# Lancement du quiz
print("🎯 Bienvenue dans le Quiz Culture Générale !")
print("=" * 45)
afficher_regles()

questions_geographie()
questions_sciences()
questions_sport()

print("\n" + "=" * 45)
print(f"🏆 Votre score final : {score} / 9")
if score >= 7:
    print("Excellent ! Vous êtes un(e) champion(ne) !")
elif score >= 4:
    print("Pas mal ! Continuez à apprendre !")
else:
    print("Courage, réessayez !")