import pandas
import csv
import numpy
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


# Load dataset
dataset = pandas.read_csv("./dataset_diabetes/diabetic_data.csv", header=0)
headers = list(dataset.columns.values)

# Isolate categorical and continuous features
categorical_data = dataset.select_dtypes(include=[object])
continuous_data = dataset.select_dtypes(exclude=[object])
#print(continuous_data.columns)

# Create a LabelEncoder object and fit it to each feature of categorical_data
# Encode labels with value between 0 and n_classes-1
label = preprocessing.LabelEncoder()

# Transform categorical features to numerical values
categorical_data_v2 = categorical_data.apply(label.fit_transform)
# print(categorical_data_v2.head(2))
# print(continuous_data.head(2))

# New dataset
dataset_v2 = pandas.concat([continuous_data, categorical_data_v2], axis=1)
# print(dataset_v2.head(2))

# Prediction models
models = []
models.append(('CART', DecisionTreeClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('GNB', RandomForestClassifier()))

# Split data into training and validation sets
array = dataset_v2.values
x = array[:,1:-2]
y = array[:,-1]
validation_size = 0.20

# Test options and evaluation metric
seed = 3
scoring = 'accuracy'

# init training and validation sets
x_train, x_validation, y_train, y_validation = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)


# Evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=5, random_state=seed)
    cv_results = model_selection.cross_val_score(model, x_train, y_train, cv=kfold, scoring = scoring)
    results.append(cv_results)
    names.append(name)
    message = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(message)


# Compare Algorithms with box plots
# box_plot = []
# for result in results:
#     trace = go.Box(
#         y = result,
#         name = "hey",
#         marker = dict(
#             color = 'rgb(0, 128, 128)',
#         )
#     )
#     box_plot.append(trace)
# layout = go.Layout(
#     title="Algorithm Comparison",
# )
# fig = go.Figure(data=box_plot, layout=layout)
# plotly.offline.plot(fig, filename="Coucou.html")


# Make prediction on validation dataset
for model in models:
    model[1].fit(x_train, y_train)
    predictions = model[1].predict(x_validation)
    print(model[0]+":")
    print(accuracy_score(y_validation, predictions))
    print(confusion_matrix(y_validation, predictions))
    print(classification_report(y_validation, predictions))
