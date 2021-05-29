import random

"""Word Finder: finds random words from a dictionary."""


        

class WordFinder:
    """
    Reads a word file and generates a list of words
    randomly returns one word in the list
    """


    def __init__(self, path = 'words.txt'):
        """reads file and generates new starting list 
        prints number of words read"""
        self.words = self.read_file(path)

    def random(self):
        """Returns random word in the list"""
        return (random.choice(self.words))
    
    @staticmethod
    def read_file(path):
        """Reads word file and generates a list of words
        prints number of words read"""
        words = []
        word_file = open(path)
        for line in word_file:
            words.append(line.strip('\n'))
        print(f'{len(words)} words read')
        word_file.close()
        return words

class SpecialWordFinder(WordFinder):
    """reads word file and generates list of words while omitting comments and empty lines
    prints number of words read"""
    @staticmethod
    def read_file(path):
        words = []
        word_file = open(path)
        for line in word_file:
            if line.strip() and not line.startswith("#"):
                words.append(line.strip('\n'))
        print(f'{len(words)} words read')
        word_file.close()
        return words
