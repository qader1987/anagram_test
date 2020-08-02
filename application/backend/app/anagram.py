from collections import Counter


class Anagram:
    @staticmethod
    def return_anagrams(letters: str) -> list:

        with open('words.txt', 'r') as f:
            dictionary = f.read()

        dictionary = [x.lower() for x in dictionary.split('\n')]

        assert isinstance(letters,
                          str), 'Scrambled letters should only be of type string.'

        letters = letters.lower()

        letters_count = Counter(letters)

        anagrams = set()
        for word in dictionary:
            # Check if all the unique letters in word are in the
            # scrambled letters
            if not set(word) - set(letters):
                check_word = set()
                # Check if the count of each letter is less than or equal
                # to the count of that letter in scrambled letter input
                for k, v in Counter(word).items():
                    if v <= letters_count[k]:
                        check_word.add(k)
                # Check if check_words is exactly equal to the unique letters
                # in the word of dictionary
                if check_word == set(word):
                    anagrams.add(word)

        anagrams.remove('')

        return sorted(list(anagrams), key=lambda x: len(x))