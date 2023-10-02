from collections import defaultdict
from pprint import pprint
import string
import re

conversation = open('conversation.txt').read().rstrip('\n').split('\n')
games = []

cur_game = []
for c in conversation:
    cur_game.append(c)
    if len(c) > 1 and '_' not in c:
        games.append(cur_game)
        cur_game = []

for g in games:
    assert all(len(x) == 1 for x in g[1::2])
    assert len(g) % 2 == 1
    assert len(set(g[1::2])) == len(g[1::2])

wordlist = open('word-list.txt').read().rstrip('\n').split('\n')
sorted_words = sorted(wordlist, key=lambda w: len(w))

len_word_map = defaultdict(list)
for word in sorted_words:
    len_word_map[len(word)].append(word)

bad = []

for game in games:
    charset = set(string.ascii_lowercase)
    word_len = len(game[0])
    all_pos_words = len_word_map[word_len]

    for i, guess in enumerate(game[1::2]):
        li = i*2
        guess_re = f"^{game[li].replace('_','.')}$"

        pos_words = [word for word in all_pos_words if re.search(guess_re, word)]
        prob_map = {}
        for c in charset:
            prob_map[c] = len([x for x in pos_words if c in x])

        probabilities = sorted(prob_map.items(), key=lambda t: -t[1])
        for c in string.ascii_lowercase:
            if (c, 0) in probabilities:
                probabilities.remove((c, 0))

        #print(probabilities)
        index = probabilities.index((guess, prob_map[guess]))
        print(index, guess, prob_map[guess], f"Best: {prob_map[guess] == probabilities[0][1]}")

        if not prob_map[guess] == probabilities[0][1]:
            if prob_map[guess] == probabilities[-1][1]:
                bad.append(True)
            else:
                bad.append(False)

        charset.remove(guess)

    print('-------------------')

print(''.join(['1' if x else '0' for x in bad]))
print(''.join(['0' if x else '1' for x in bad]))
print(f"{len(games)} games played")
