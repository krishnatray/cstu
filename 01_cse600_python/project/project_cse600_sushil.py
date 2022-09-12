# _*_ coding: utf-8 _*_
"""
    CSE600 Python for AI -- Project
    Sushil Kumar Sharma
    Sun, 14 Aug 2022 
"""

try:
    import PyPDF2
    from pattern.text.en import singularize
except Exception as e:
    print(e)
    exit(1)

class WordAnalysis:
    """
    
    """ 

    def __init__(self):
        self.__removed=[]
        self.__dictWords = dict()

    def __str__(self):
        pass

    def AddRemovedWords(self, word):
        pass
    
    def DelRemovedWords(self, text):
        pass

    def ExtractWords(self, text):
        """
            1). Strips off all punctuations, numbers, and symbols, only words are kept, and tries to
                remove non-words as much for example, single letter words.
            2). Converts the plurals to singular words, and converts the capitalized words to lowercase
                words. 
            3)  Counts the frequency of the words, and save them in a dictionary
        """
        pass

    def Show(self, freq):
        pass



if __name__ == "__main__":
    pass
