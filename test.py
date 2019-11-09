from sentiment import *



tiny = open("tiny.txt", 'r')
statement = tiny.readline()
kss = {'brando': [2], 'is': [3], 'the': [2]}
print(statement_pss(statement, kss))
