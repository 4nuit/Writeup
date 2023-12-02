def genere_question_reponse():
    mystery_number = random.randint(BEG_RAND, END_RAND - 2)
    liste = []
    arnaque_les_probas = 20
    for j in range(3):
        liste.append(random.randint(0, mystery_number - 1 - arnaque_les_probas))
    listed2 = sorted(liste)
    maxi = listed2[-1]

    if mystery_number - maxi < END_RAND - mystery_number:
        Q = random.randint(maxi + 1, mystery_number - 1)
    else:
        Q = random.randint(mystery_number + 1, END_RAND - 1)

    if random.randint(0,1) == 0:
        Q = 2 * mystery_number - Q

    return [liste, Q, mystery_number]
