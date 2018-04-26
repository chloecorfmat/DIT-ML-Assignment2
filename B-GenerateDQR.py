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
#continuous_names, categorical_names = make_list_name(datas)

continuous_names = datas.select_dtypes(exclude=[object])
categorical_names = datas.select_dtypes(include=[object])

# Write in a new csv file for continuous features.
dqr_continuous(datas, continuous_names)
# Write in a new csv file for categorical features.
dqr_categorical(datas, categorical_names)

# Generate graphs (html local files) for all continuous features.
generate_graphs(datas, continuous_names, True)
generate_graphs(datas, categorical_names, False)
