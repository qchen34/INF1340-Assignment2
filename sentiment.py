from typing import TextIO, List, Union, Dict, Tuple
from collections import Counter
from operator import itemgetter

# PART I: File I/O, strings, lists


def is_word(token: str) -> bool:
    '''Return True IFF token is an alphabetic word optionally containing
    forward slashes or dashes.
    
    >>> is_word('Amazing')
    True
    >>> is_word('writer/director')
    True
    >>> is_word('true-to-life')
    True
    >>> is_word("'re")
    False
    >>> is_word("1960s")
    False
    >>> is_word("/re")
    True
    '''
    for char in token:
        if not char.isalpha() and char != '/' and char != '-':
            return False

    return True


def get_word_list(statement: str) -> List[str]:
    '''Return a list of words contained in statement, converted to lowercase. 
    Use is_word to determine whether each token in statement is a word.
    
    >>> get_word_list('A terrible , 1970s mess of true-crime nonsense from writer/director Shyamalan .')
    ['a', 'terrible', 'mess', 'of', 'true-crime', 'nonsense', 'from', 'writer/director', 'shyamalan']
    '''
    
    split_statement = statement.lower().split()
    return_list = []
    for char in split_statement:
        if is_word(char):
            return_list.append(char)
    return return_list


def judge(score: float) -> str:
    '''Return 'negative' if score is 1.5 or less.
    Return 'positive' if score is 2.5 or more.
    Return 'neutral' otherwise.
    >>> judge(1.3)
    'negative'
    >>> judge('1.8')
    'neutral'
    >>> judge('3.4')
    'positive'
    '''

    score = float(score)
    if score <= 1.5:
        return 'negative'
    elif score >= 2.5:
        return 'positive'
    else:
        return 'neutral'


def word_kss_scan(word: str, file: TextIO) -> Union[None, float]:
    '''Given file composed of rated movie reviews, return the average score
    of all occurrences of word in file. If word does not occur in file, return None.
    [examples not required]
    '''
    ratings = []
    sum_rating = 0
    occurrences = 0

    for line in file:
        for item in get_word_list(line):
            if item == word:
                ratings.append(float(line[0]))
                occurrences += 1
    if occurrences == 0:
        return None

    for rating in ratings:
        sum_rating += rating

    return sum_rating / occurrences

# PART II: Dictionaries 


def extract_kss(file: TextIO) -> Dict[str, List[int]]:
    '''Given file composed of rated movie reviews, return a dictionary
    containing all words in file as keys. For each key, store a list
    containing the total sum of review scores and the number of times
    the key has occurred as a value, e.g., { 'a' : [12, 4] }
    [examples not required]
    '''
    '''
    for each line and for each word in the line:
        if the word is already in the dictionary:
            add the current review score to the review score asscoiated with the word (find it in dict)
            add the occurrence by one
        else:
            create a new word in the dictionary and append the current review score and set the occurrence 
            as 1
    '''
    dictionary = {}

    for line in file:
        for item in get_word_list(line):
            if item in dictionary:
                dictionary[item] = [dictionary.get(item)[0] + int(line[0]), dictionary.get(item)[1] + 1]
            else:
                dictionary[item] = [int(line[0]), 1]

    return dictionary


# word_kss('brando', extract_kss(tiny))
def word_kss(word: str, kss: Dict[str, List[int]]) -> Union[float, None]:
    '''Return the Known Sentiment Score of word if it appears in kss. 
    If word does not appear in kss, return None.
    [examples not required]
    '''    
    if word in kss:
        return kss.get(word)[0] / kss.get(word)[1]
    else:
        return None
             
             
def statement_pss(statement: str, kss: Dict[str, List[int]]) -> Union[float, None]:
    '''Return the Predicted Sentiment Score of statement based on
    word Known Sentiment Scores from kss.
    Return None if statement contains no words from kss.'''
    kss_sum = 0
    word_count = 0
    for word in get_word_list(statement):
        if word in kss:
            kss_sum += word_kss(word, kss)
            word_count += 1
        else:
            kss_sum += 0
    if word_count > 0:
        return kss_sum / word_count
    else:
        return None


# PART III: Word Frequencies
def score(item: Tuple[str, List[int]]) -> float:
    '''Given item as a (key, value) tuple, return the
    ratio of the first and second integer in value
    '''

    return item[1][0] / item[1][1]


def most_extreme_words(count: int, min_occ: int, kss: Dict[str, List[int]], pos: bool) -> List[List[Union[str, float, int]]]:
    '''Return a list of lists containing the count most extreme words
    that occur at least min_occ times in kss.
    Each item in the list is formatted as follows:
    [word, average score, number of occurrences]
    If pos is True, return the most positive words.
    If pos is False, return the most negative words.
    [examples not required]
    '''
    '''
    count: how many extreme words should it return, the top count number of sorted words
    min_occ: at least how many times each word should have occurred in the dataset
    if the occurrence of a word is lower than min_occ, dont return
    pos: if pos is True, return the top positive ones, if false, return the top negative ones
    '''
    if pos:
        sorted_list = sorted(kss.items(), key=score, reverse=True)
    else:
        sorted_list = sorted(kss.items(), key=score)
    most_extreme_word_list = []

    index = 0
    while index < count and sorted_list:
        current_item = sorted_list.pop(0)
        if current_item[1][1] >= min_occ:
            most_extreme_word_list.append([current_item[0], score(current_item), current_item[1][1]])
            index += 1

    return most_extreme_word_list


def most_negative_words(count: int, min_occ: int, kss: Dict[str, List[int]]) -> List[List[Union[str, float, int]]]:
    """Return a list of the count most negative words that occur at least min_occ times in kss.
    """
    return most_extreme_words(count, min_occ, kss, False)


def most_positive_words(count: int, min_occ: int, kss: Dict[str, List[int]]) -> List[List[Union[str, float, int]]]:
    """Return a list of the count most positive words that occur at least min_occ times in kss.
    """
    return most_extreme_words(count, min_occ, kss, True)


if __name__ == "__main__":


# Pick a dataset    
    dataset = open('tiny.txt', 'r')
    #dataset = 'small.txt'
    #dataset = 'medium.txt'
    #dataset = 'full.txt'
    
    # Your test code here
    print(extract_kss(dataset))



