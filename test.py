from sentiment import *

tiny = open("tiny.txt", 'r')
small = open("small.txt", 'r')
count = 10
min_occ = 1
pos = True



#print(is_word('\'re'))
#print(word_kss('brando', kss))

#print(statement_pss('1 Brando is Brando , but for this one it \'s not enough .', extract_kss(tiny)))

#print(most_extreme_words(count, min_occ, extract_kss(small), pos))
print(extract_kss(tiny))