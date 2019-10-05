"""
demo12_names.py
"""
import random
import numpy as np
import nltk.corpus as nc
import nltk.classify as cf

male_names = nc.names.words('male.txt')
female_names = nc.names.words('female.txt')

data = []
for male_name in male_names:
    feature = {'feature': male_name[-2:].lower()}
    data.append((feature, 'male'))
for female_name in female_names:
    feature = {'feature': female_name[-2:].lower()}
    data.append((feature, 'female'))
random.seed(7)
random.shuffle(data)
train_data = data[:int(len(data) / 2)]
test_data = data[int(len(data) / 2):]
model = cf.NaiveBayesClassifier.train(train_data)
ac = cf.accuracy(model, test_data)
print(ac)

names, genders = ['Leonardo', 'Amy', 'Sam',
                  'Tom', 'Katherine', 'Taylor', 'Susanne'], []
for name in names:
    feature = {'feature': name[-2:].lower()}
    gender = model.classify(feature)
    genders.append(gender)
for name, gender in zip(names, genders):
    print(name, '->', gender)
