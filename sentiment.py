from typing import TextIO, List, Union, Dict, Tuple
from collections import Counter

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
    '''
    if token.isalpha() or '/' in token or '-' in token:
        return True
    return False


def get_word_list(statement: str) -> List[str]:
    '''Return a list of words contained in statement, converted to lowercase. 
    Use is_word to determine whether each token in statement is a word.
    
    >>> get_word_list('A terrible , 1970s mess of true-crime nonsense from writer/director Shyamalan .')
    ['a', 'terrible', 'mess', 'of', 'true-crime', 'nonsense', 'from', 'writer/director', 'shyamalan']
    '''

    statement = statement.lower()
    new_list = []
    left_bound = 0
    right_bound = 0
    while right_bound < len(statement):
        if statement[right_bound] == ' ':
            if is_word(statement[left_bound: right_bound]):
                new_list.append(statement[left_bound: right_bound])
            right_bound += 1
            left_bound = right_bound
        else:
            right_bound += 1
    return new_list


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
    # how does line in file works, ask TA or velien
    for line in file:
        for item in get_word_list(line):
            if item == word:
                ratings.append(float(line[0]))
                occurrences += 1
    if occurrences == 0:
        return None

    for rating in ratings:
        sum_rating += rating
    average = sum_rating / occurrences
    return average

# PART II: Dictionaries 


def extract_kss(file: TextIO) -> Dict[str, List[int]]:
    '''Given file composed of rated movie reviews, return a dictionary
    containing all words in file as keys. For each key, store a list
    containing the total sum of review scores and the number of times
    the key has occurred as a value, e.g., { 'a' : [12, 4] }
    [examples not required]
    '''
    '''
    for each line and for each word:
        if the word is already in the dictionary:
            add the current review score to the review score asscoiated with the word (find it in dict)
            add the occurrence by one
        else:
            create a new word in the dictionary and append the current review score and set the occurrence 
            as 1
    '''
    dictionary = {}
    occurrences = 1
    sum_review_score = 0
    value_list = [sum_review_score, occurrences]

    for line in file:
        for item in get_word_list(line):
            if item in dictionary:
                dictionary[item] = [dictionary.get(item, 0)[0] + int(line[0]), dictionary.get(item, 1)[1] + 1]
            else:
                dictionary[item] = [int(line[0]), 1]

    return dictionary


def word_kss(word: str, kss: Dict[str, List[int]]) -> Union[float, None]:
    '''Return the Known Sentiment Score of word if it appears in kss. 
    If word does not appear in kss, return None.
    [examples not required]
    '''    
    if word in kss:
        return float(kss[word][0])
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
            kss_sum += kss[word][0]
            word_count += 1
        else:
            kss_sum += 0

    return kss_sum / word_count



# PART III: Word Frequencies

def score(item: Tuple[str, List[int]]) -> float:
    '''Given item as a (key, value) tuple, return the
    ratio of the first and second integer in value
    '''
    
    return 0


def most_extreme_words(count, min_occ, kss, pos):
    '''Return a list of lists containing the count most extreme words
    that occur at least min_occ times in kss.
    Each item in the list is formatted as follows:
    [word, average score, number of occurrences]
    If pos is True, return the most positive words.
    If pos is False, return the most negative words.
    [examples not required]
    '''
    
    return []
    
    
def most_negative_words(count, min_occ, kss):
    '''Return a list of the count most negative words that occur at least min_occ times in kss.
    '''
    
    return []
    
def most_positive_words(count, min_occ, kss):
    '''Return a list of the count most positive words that occur at least min_occ times in kss.
    '''
    
    return []

        
    
if __name__ == "__main__":

# Pick a dataset    
    dataset = 'tiny.txt'
    #dataset = 'small.txt'
    #dataset = 'medium.txt'
    #dataset = 'full.txt'
    
    # Your test code here
    pass

