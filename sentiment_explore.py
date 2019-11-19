from typing import TextIO, List, Union, Dict, Tuple
import matplotlib.pyplot as plt
from sentiment import *


# Your exploration functions here
# first try
def mean_diff_pss(filename: str) -> float:
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


# modification
def mean_diff_pss2(testing_filename: str, training_filename: str) -> float:
    """
    :param training_filename: takes in a file as training_file
    :param testing_filename: takes in a file as testing file
    :return: return the mean differences between the actual score and Predicted Sentiment Score of each sentence
    This function calculates the absolution value (the difference) from the subtraction of PSS and
    actual score, and then calculate the mean of that value for the target file
    """
    training_file = open(training_filename, 'r')
    training_dictionary = extract_kss(training_file)
    testing_file = open(testing_filename, 'r')
    sum_pss_score_differences = 0
    line_count = 0
    for line in testing_file:
        sum_pss_score_differences += abs(statement_pss(line, training_dictionary) - float(line[0]))
        line_count += 1

    testing_file.close()
    training_file.close()
    return sum_pss_score_differences / line_count


'''
Visualization code for the mean difference for each file.
Hypothesis: as the file gets bigger, the mean differences for the target file get smaller
'''
# The mean differences of PSS and original score for 'tiny.txt'

y_values = [mean_diff_pss2('tiny.txt', 'full.txt'),
            mean_diff_pss2('small.txt', 'full.txt'),
            mean_diff_pss2('medium.txt', 'full.txt')]

x = ["tiny.txt", "small.txt", "medium.txt"]
plt.plot(x, y_values)
plt.title("Mean difference for tiny, small, medium", fontsize=14)
plt.xlabel("Text files", fontsize=14)
plt.ylabel("Scores", fontsize=14)
plt.show()

plt.scatter(x, y_values, s=200)
plt.title("Scatter mean difference for tiny, small and medium", fontsize=14)
plt.xlabel("Text files", fontsize=14)
plt.ylabel("Scores", fontsize=14)
plt.show()

# The pss and original score graph for 'tiny.txt'


# Follow FDR

if __name__ == "__main__":
    # Pick a dataset
    dataset = 'tiny.txt'
    # dataset = 'small.txt'
    # dataset = 'medium.txt'
    # dataset = 'full.txt'

    # Your exploration testing code here

'''
Looking at PSS in comparison to original score for each line. Calculate the difference for each line. Calculate sum of
the differences and then divide to receive an average variance.

if were to go deeper, might want to look at the impact of the neutral words on our PSS model
'''
