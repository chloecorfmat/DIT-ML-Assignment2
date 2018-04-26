from collections import Counter

def modify_dataset(dataset, header_names):

	# Delete descriptive features which contain more than 90% of a single value
	for feature in header_names:
		most_common_value_in_feature = Counter(dataset[feature]).most_common(1)[0][1]
		if most_common_value_in_feature > float(len(dataset[feature])*0.9):
			del dataset[feature]
	
	# Delete ID-like descriptive features
	del dataset['encounter_id']

	# Delete rows containing missing values
	header_names = list(dataset.columns.values)
	for feature in header_names:
		indices = [i for i, x in enumerate(dataset[feature]) if x == "?"]
		dataset = dataset.drop(dataset.index[indices])
	return dataset
