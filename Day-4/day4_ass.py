"""Pylint Example"""
import sys
from collections import Counter
import re
import uuid
import logging
import config as cf
#pylint: disable=too-few-public-methods


def function_palindrome(word):
    """Palindrome Finding"""
    return word == word[::-1]


def writefile(word):
    """Writing into file"""
    unique_file = str(uuid.uuid1())
    with open(unique_file, 'w') as file2:
        file2.write(word)
    logger.info("Unique write file is created")


class Base:
    """Base Class"""
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file1_read:
                logger.info("Input file is opened in read mode")
                self.text = file1_read.read()
            logger.info("Input file is converted to list")
            self.text = self.text.replace('.', ' ')
            self.text = self.text.replace("'s", '')
            file1_read.close()
        except IOError:
            print("File not found")
            logger.error("File is not found")
            sys.exit()


class Derived1(Base):
    """Derived Clss"""
    def __init__(self, filename):
        super().__init__(filename)
        self.dict1 = {}
        self.result = []
        self.palindrome_words = []
        self.max_value = []
        self.count_suffix = 0
        self.count_prefix = 0
        self.str = list(self.text.split(' '))
        logger.info("Derived class init method is executed")

    def prefix_and_suffix(self):
        """Prefix and Suffix"""
        for wor in self.str:
            if wor.startswith("To") and len(wor) > 2:
                self.count_prefix += 1
        logger.info("prefix count is found")
        for wor in self.str:
            if wor.endswith("ing"):
                self.count_suffix += 1
        logger.info("suffix count is found")

    def maximum_repeat(self):
        """Maximum repeating words"""
        counter = Counter(self.str)
        dictionary1 = {}
        dictionary1.update(counter)
        max_count = max(dictionary1, key=dictionary1.get)
        self.max_value.append(max_count)
        logger.info("Maximum repeated element is found")

    def palindrome(self):
        """Palindrome"""
        for wor in self.str:
            if function_palindrome(wor):
                self.palindrome_words.append(wor)
        logger.info("palindromic words are found")

    def function_unique(self):
        """Unique words in text"""
        for wor in self.str:
            wor = wor.lower()
            if wor not in self.result:
                self.result.append(wor)
        logger.info("Unique word in the input file is found")

    def dictionary(self):
        """Dictionary conversion"""
        for wor in enumerate(self.str):
            self.dict1.update({wor})
        logger.info("text file is converted into dictionary")

    def print_result(self):
        """Result Printing"""
        print("Prefix words:", self.count_prefix)
        print("Suffix words:", self.count_suffix)
        print("Maximum repeated words:", self.max_value)
        print("Palindromic word:", self.palindrome_words)
        print("Unique words:", self.result)
        print("Dictionary words:", self.dict1)
        logger.info("Results are printed")

    def function(self):
        """Writing into file"""
        answer = re.split('a |e|i|o|u|A|E|I|O|U', self.text)
        while '' in answer:
            answer.remove('')
        count = 1
        solution = []
        for ans in answer:
            if len(ans) > 2 and ans[2] != '-':
                ans = ans[0:2] + ans[2].upper() + ans[3:]
            if count % 5 == 0:
                ans = ans.upper()
            count += 1
            ans = ans.replace(' ', '-')
            ans = ans.replace('\n', ';')
            solution.append(ans)
        logger.info("New functions to be written in unique file is ready to write")
        sol = ' '.join(solution)
        writefile(sol)
        logger.info("Required result is written into the file")


if __name__ == '__main__':
    logging.basicConfig(filename="msg.log", format="%(asctime)s %(message)s", filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("Derived class is called")
    FILE_FROM_CFG = cf.names["inputfile"]
    print(FILE_FROM_CFG)
    d = Derived1(FILE_FROM_CFG)
    d.prefix_and_suffix()
    d.maximum_repeat()
    d.palindrome()
    d.function_unique()
    d.dictionary()
    d.print_result()
    d.function()
    logger.info("Program is executed successfully")
