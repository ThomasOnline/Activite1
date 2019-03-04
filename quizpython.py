answer = input("Quel usage a principalement le language python? ")
print("Tu as répondu", answer)

if answer == "BDD":
    print("Tu as bien répondu a la question, Bravo.")
elif answer == "robot":
    print("Tu as bien répondu a la question, Bravo")
elif answer == "Web":
    print("Tu as bien répondu a la question, Bravo")
else:
    print("Tu t'es trompé, recommence!")
