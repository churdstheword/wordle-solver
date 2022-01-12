#! /usr/bin/python3

import sys

def main() -> int:
    data = [{}, {}, {}, {}, {}]

    with open('dictionary.txt') as f:
        words = [line.rstrip() for line in f]

    # Count the letters as they appearn in each position
    for word in words:
        for i in range(len(word)):
            letter = word[i]
            if letter not in data[i]:
                data[i][letter] = 1
            else:
                data[i][letter] = data[i][letter] + 1

    # Sort the letter counts for each position
    for position in range(5):
        data[position] = {k: v for k, v in sorted(
            data[position].items(), key=lambda value: value[1], reverse=True
        )}

    # Score each word in the dictionary based on the letter position and frequency
    scores = {}
    for word in words:
        scores[word] = 0
        for i in range(len(word)):
            scores[word] = scores[word] + (data[i][word[i]] / len(words))

    # Output the top 10 scores
    scores = sorted(scores.items(), key=lambda value: value[1], reverse=True)
    for k, v in scores[:25]:
        print('Word: "{:s}", Score: {:f}'.format(k, v))

    return 0


if __name__ == "__main__":
    sys.exit(main())
