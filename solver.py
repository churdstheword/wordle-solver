#! /usr/bin/python3

import sys

class WordleSolver:

    def __init__(self):
        self.letters = set()
        self.words = self.getWords()
        self.globals = self.determineGlobalFrequency()
        self.positional = self.determinePositionalFrequency()

    def getWords(self):
        words = []
        with open('dictionary.txt') as f:
            words = [line.rstrip() for line in f]

        return words

    def determineGlobalFrequency(self):

        globals = {}
    
        # Count the letters in all words
        for word in self.words:
            for i in range(len(word)):
                letter = word[i]
                if letter not in globals:
                    globals[letter] = 1
                else:
                    globals[letter] = globals[letter] + 1
        
        # Sort the global letter counts
        globals = {k: v for k, v in sorted(
            globals.items(), key=lambda value: value[1], reverse=True
        )}

        return globals

    def determinePositionalFrequency(self):

        positional = [{}, {}, {}, {}, {}]

        # Count the letters as they appear in each position
        for word in self.words:
            for i in range(len(word)):
                letter = word[i]
                # Track frequency of each letter in each position
                if letter not in positional[i]:
                    positional[i][letter] = 1
                else:
                    positional[i][letter] = positional[i][letter] + 1


        # Sort the positional letter counts
        for position in range(5):
            positional[position] = {k: v for k, v in sorted(
                positional[position].items(), key=lambda value: value[1], reverse=True
            )}

        return positional

    def getWordScore(self, word):
        wordScore = 0
        usedletters = set()
        for i in range(len(word)):
            letter = word[i]
            hasBeenUsed = int(not letter in self.letters and not letter in usedletters)
            wordScore = wordScore + (hasBeenUsed * ( self.positional[i][word[i]] + self.globals[word[i]]))
            usedletters.add(letter)
        return wordScore

    def makeBlindGuess(self):

        # Score each word in the dictionary based on the letter position and frequency
        scores = {}
        for word in self.words:
            scores[word] = self.getWordScore(word)

        # Sort the scores
        scores = sorted(scores.items(), key=lambda value: value[1], reverse=True)

        # Choose the highest ranked word, mark it, and return it
        word = scores[0][0]
        for i in range(len(word)):
            self.letters.add(word[i])

        return word


def main() -> int:
    solver = WordleSolver()
    for i in range(3):
        guess = solver.makeBlindGuess()
        print(guess)
    return 0


if __name__ == "__main__":
    sys.exit(main())
