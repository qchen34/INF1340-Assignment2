from typing import TextIO, List, Union, Dict, Tuple
import matplotlib.pyplot as plt
from sentiment import *


# Your exploration functions here

def mean_difference_pss_score(filename: str) -> float:
    """
    :param filename: takes in a string of filename
    :return: return the mean differences between the actual score and Predicted Sentiment Score of each sentence
    This function calculates the absolution value (the difference) from the subtraction of PSS and
    actual score, and then calculate the mean of that value for the target file
    """
    processing_file = open(filename, 'r')
    sum_pss_score_differences = 0
    line_count = 0
    for line in processing_file:
        line_count += 1
        sum_pss_score_differences += abs(statement_pss(line, extract_kss(processing_file)) - float(line[0]))
    processing_file.close()
    return sum_pss_score_differences / line_count


def file_content_to_list(filename: str) -> List[str]:
    """
    :param filename: takes in a string of filename
    :return: return a list contains all the content of the file in the list
    """
    processing_file = open(filename, 'r')
    return_list = []
    for line in processing_file:
        return_list.append(line)
    processing_file.close()
    return return_list


# Store each file into a list
tiny_list = file_content_to_list('tiny.txt')
small_list = file_content_to_list('small.txt')
medium_list = file_content_to_list('medium.txt')
full_list = file_content_to_list('full.txt')

'''
Visualization code for the mean difference for each file.
Hypothesis: as the file gets bigger, the mean differences for the target file get smaller
'''
# The mean differences of PSS and original score for 'tiny.txt'

y_values = [mean_difference_pss_score('tiny.txt'),
            mean_difference_pss_score('small.txt'),
            mean_difference_pss_score('medium.txt'),
            mean_difference_pss_score('full.txt')]

x = ["tiny.txt", "small.txt", "medium.txt", "full.txt"]
plt.plot(x, y_values)
plt.title("Mean difference for tiny, small, medium and full", fontsize=14)
plt.xlabel("Text files", fontsize=14)
plt.ylabel("Scores", fontsize=14)
plt.show()


plt.scatter(x, y_values, s=200)
plt.title("Scatter mean difference for tiny.txt, small.txt and medium.txt", fontsize=14)
plt.xlabel("Text files", fontsize=14)
plt.ylabel("Scores", fontsize=14)
plt.show()


# The pss and original score graph for 'tiny.txt'

'''
tiny_pss = get_pss(tiny)
x_label = create_x_value(tiny)
plt.scatter(x_label, tiny_pss)
plt.title("PSS and Original Scores for tiny.txt", fontsize=14)
plt.xlabel("Statement", fontsize=14)
plt.ylabel("Score", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

# The pss and original score graph for 'small.txt'
small_pss = get_pss(small)
print(small_pss)
plt.plot(small_pss)
plt.title("PSS and Original Scores for small.txt", fontsize=14)
plt.xlabel("Statement", fontsize=14)
plt.ylabel("Score", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

# The pss and original score graph for 'medium.txt'

plt.plot(get_pss(medium))
plt.title("PSS and Original Scores for medium.txt", fontsize=14)
plt.xlabel("Statement", fontsize=14)
plt.ylabel("Score", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

# The pss and original score graph for 'full.txt'

plt.plot(get_pss(full))
plt.title("PSS and Original Scores for full.txt", fontsize=14)
plt.xlabel("Statement", fontsize=14)
plt.ylabel("Score", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
'''
'''
def get_original_score(input_list: List[str]) -> List[float]:
    original_list = []
    for line in input_list:
        original_list.append(float(line[0]))
    return original_list


def get_pss(input_list: List[str], filename: str) -> List[float]:
    processing_file = open(filename, 'r')
    pss_list = []
    for line in input_list:
        pss_list.append(statement_pss(line, extract_kss(processing_file)))
    processing_file.close()
    return pss_list


def create_x_value(input_list: List[str]):
    """
    :param input_list: takes in a list of movie comments that were transformed into a list
    :return: return a list that starts from 1 to the length of the list
    >>> create_x_value(['a', 'b', 'c'])
    [1, 2, 3]
    """
    return_list = []
    current_line = 1
    for line in input_list:
        return_list.append(current_line)
        current_line += 1
    return return_list

'''

# Follow FDR

if __name__ == "__main__":

    # Pick a dataset    
    dataset = 'tiny.txt'
    #dataset = 'small.txt'
    #dataset = 'medium.txt'
    #dataset = 'full.txt'
    
    # Your exploration testing code here
    print(file_content_to_list(dataset))


'''
Looking at PSS in comparison to original score for each line. Calculate the difference for each line. Calculate sum of
the differences and then divide to receive an average variance.

if were to go deeper, might want to look at the impact of the neutral words on our PSS model
'''

