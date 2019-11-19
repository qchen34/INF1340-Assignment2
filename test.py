from sentiment import *
from sentiment_explore import *



#print(is_word('\'re'))
#print(word_kss('brando', kss))
#print(statement_pss('1 Brando is Brando , but for this one it \'s not enough .', extract_kss(tiny)))
#print(most_extreme_words(count, min_occ, extract_kss(small), pos))
# print(statement_pss('Marlon Brando is incredible as the patriarch of the family .', extract_kss(small)))
#print(get_word_list('A terrible , 1970s mess of true-crime nonsense from writer/director Shyamalan .'))


# absolute(pss_model-score_origin)
tiny = open('tiny.txt', 'r')
print(most_extreme_words(3, 1, extract_kss(tiny), False))
