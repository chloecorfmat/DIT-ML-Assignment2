from collections import Counter
import operator
import csv

class Toolkit():
    def count_modes(list_of_cardinalities, feature):
        sorted_possible_values_with_cardinality = sorted(list_of_cardinalities[feature].items(),key=operator.itemgetter(1))
        length = len(sorted_possible_values_with_cardinality)
        mode = sorted_possible_values_with_cardinality[length - 1][0]
        mode_freq = sorted_possible_values_with_cardinality[length - 1][1]
        second_mode = sorted_possible_values_with_cardinality[length - 2][0]
        second_mode_freq = sorted_possible_values_with_cardinality[length - 2][1]
        return mode, mode_freq, second_mode, second_mode_freq

# define whether category is continuous or categorical
def make_list_name(datas):
    continuous_names = []
    categorical_names = []
    for name in datas:
        if name == 'id':
            continue
        index = 2
        while str(datas[name][index]) == "?":
            index = index + 1
        if str(datas[name][2]).isnumeric():
            continuous_names.append(name)
        else:
            categorical_names.append(name)
    return continuous_names, categorical_names

# Write in a new csv file continuous features.
def dqr_continuous(datas, continuous_names, list_of_cardinalities):
    with open('./data/B-DQR-ContinuousFeatures.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Feature', 'Count', 'Miss. (%)', 'Card.', 'Min.', '1st Qrt.', 'Mean', 'Median', '3rd Qrt.', 'Max.','Std. Dev.'])
        for feature in continuous_names:
            list_of_cardinalities[feature] = Counter(datas[feature])
            count = datas[feature].count()
            miss = list_of_cardinalities[feature]["?"] * 100 / count
            card = len(list_of_cardinalities[feature])
            min = datas[feature].min()
            fstQrt = datas[feature].quantile(0.25)
            mean = datas[feature].mean()
            median = datas[feature].median()
            trdQrt = datas[feature].quantile(0.75)
            max = datas[feature].max()
            std = datas[feature].std()
            filewriter.writerow([feature, count, miss, card, min, fstQrt, mean, median, trdQrt, max, std])

# Write in a new csv file categorical features.
def dqr_categorical(datas, categorical_names, list_of_cardinalities):
    with open('./data/B-DQR-CategoricalFeatures.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Feature', 'Count', 'Miss', 'Card', 'Mode', 'Mode Freq.', 'Mode (%)', '2nd Mode', '2nd Mode Freq','2nd Mode (%)'])
        for feature in categorical_names:
            list_of_cardinalities[feature] = Counter(datas[feature])
            count = datas[feature].count()
            miss = list_of_cardinalities[feature]["?"] * 100 / count
            card = len(list_of_cardinalities[feature])
            mode, mode_freq, second_mode, second_mode_freq = Toolkit.count_modes(list_of_cardinalities, feature)
            mode_perc = (count - mode_freq) * 100 / count
            second_mode_perc = (count - second_mode_freq) * 100 / count
            filewriter.writerow([feature, count, miss, card, mode, mode_freq, mode_perc, second_mode, second_mode_freq, second_mode_perc])
