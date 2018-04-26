import pandas
import csv
import os

# Import custom functions.
from DQR_CSVFileManagment import *
from DQR_PlotGraphicalDisplay import *

# Create directory for Virsualisations (html files).
if not os.path.exists('Visualisations'):
	os.makedirs('Visualisations')

# Read CSV file.
try:
	datas = pandas.read_csv('./dataset_diabetes/diabetic_data.csv', header=0)
except:
	print("Error: ./dataset_diabetes/diabetic_data.csv is missing.")
	exit()


# Define if name is continuous or categorical
continuous_names = datas.select_dtypes(exclude=[object])
categorical_names = datas.select_dtypes(include=[object])

# Define the list of dictionnaries feature -> cardinalities
all_names = categorical_names+continuous_names
list_of_cardinalities = dict(zip(all_names, [None]*len(all_names)))

# Write in a new csv file for continuous features.
dqr_continuous(datas, continuous_names, list_of_cardinalities)
# Write in a new csv file for categorical features.
dqr_categorical(datas, categorical_names, list_of_cardinalities)

# Generate graphs (html local files) for all continuous features.
generate_graphs(datas, continuous_names, True, list_of_cardinalities)
generate_graphs(datas, categorical_names, False, list_of_cardinalities)
