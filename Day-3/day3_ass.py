import sys
from collections import Counter
import re
import uuid
import logging


def palin(w):
    return w == w[::-1]


class Base:
    def __init__(self):
        try:
            file = sys.argv[1]
            self.f = open(file, 'r')
            logger.info("Input file is opened in read mode")
        except IOError:
            print("File not found")
            logger.error("File is not found")
            exit()

    def readfile(self):
        self.text = self.f.read()
        logger.info("Input file is converted to list")
        self.text = self.text.replace('.', ' ')
        self.text = self.text.replace("'s", '')
        self.f.close()

    def writefile(self):
        unique_file = str(uuid.uuid1())
        self.f1 = open(unique_file, 'w')
        logger.info("Unique write file is created")


class Derived1(Base):
    def __init__(self):
        logger.info("Base class is inherited")
        super().__init__()
        super().readfile()
        super().writefile()
        logger.info("Base class methods are inherited")
        self.answer = re.split('a |e|i|o|u|A|E|I|O|U', self.text)
        while '' in self.answer:
            self.answer.remove('')
        self.solution = []
        self.str = list(self.text.split(' '))
        self.count_prefix = 0
        self.count_suffix = 0
        self.max_value = []
        self.palinwords = []
        self.result = []
        self.dict1 = {}
        logger.info("Derived class init method is executed")

    def prefix(self):
        for w in self.str:
            if w.startswith("To") and len(w) > 2:
                self.count_prefix += 1
        logger.info("prefix count is found")

    def suffix(self):
        for w in self.str:
            if w.endswith("ing"):
                self.count_suffix += 1
        logger.info("suffix count is found")

    def maximumrepeat(self):
        counter = Counter(self.str)
        d1 = {}
        d1.update(counter)
        max_count = max(d1, key=d1.get)
        self.max_value.append(max_count)
        logger.info("Maximum repeated element is found")

    def palindrome(self):
        for w in self.str:
            if palin(w):
                self.palinwords.append(w)
        logger.info("palindromic words are found")

    def uniquewords(self):
        for w in self.str:
            w = w.lower()
            if w not in self.result:
                self.result.append(w)
        logger.info("Unique word in the input file is found")

    def dictionary(self):
        for w in enumerate(self.str):
            self.dict1.update({w})
        logger.info("text file is converted into dictionary")

    def print_result(self):
        print("Prexfix words:", self.count_prefix)
        print("Suffix words:", self.count_suffix)
        print("Maximum repeated words:", self.max_value)
        print("Palindromic word:", self.palinwords)
        print("Unique words:", self.result)
        print("Dictionary words:", self.dict1)
        logger.info("Results are printed")

    def function(self):
        count = 1
        for ans in self.answer:
            if len(ans) > 2 and ans[2] != '-':
                ans = ans[0:2] + ans[2].upper() + ans[3:]
            if count % 5 == 0:
                ans = ans.upper()
            count += 1
            ans = ans.replace(' ', '-')
            ans = ans.replace('\n', ';')
            self.solution.append(ans)
        logger.info("New functions to be written in unique file is ready to write")
        sol = ' '.join(self.solution)
        self.f1.write(sol)
        logger.info("Required result is written into the file")


if __name__ == '__main__':
    logging.basicConfig(filename="msg.log", format="%(asctime)s %(message)s", filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("Derived class is called")
    d = Derived1()
    d.prefix()
    d.suffix()
    d.maximumrepeat()
    d.palindrome()
    d.uniquewords()
    d.dictionary()
    d.print_result()
    d.function()
    logger.info("Program is executed successfully")
