import wordleWords
import time

type = input("Enter language PL or EN\n")
words = wordleWords.pl if type == "PL" else wordleWords.eng
greens = []
yellows = []
greys = []


def does_match(word, greens, yellows, greys):
    for green in greens:
        if word[green[1]] != green[0]:
            return False
    for yellow in yellows:
        if yellow[0] not in word or word[yellow[1]] == yellow[0]:
            return False
    for grey in greys:
        if grey in word:
            return False
    return True


while 1:
    word = input("Enter word\n").lower()
    pattern = input("Enter given answer in format N - grey color, G - green color, Y - Yellow color\n")
    for i in range(5):
        if pattern[i] == "Y":
            yellows.append((word[i], i))
        elif pattern[i] == "G":
            greens.append((word[i], i))
        else:
            greys.append(word[i])
    for word in words[:]:
        if not does_match(word, greens, yellows, greys):
            words.remove(word)
    if len(words) > 30:
        print("Enter more info")
    else:
        print(words)
