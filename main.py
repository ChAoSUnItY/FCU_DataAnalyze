from typing import (Dict, MutableSequence)
from statistics import mean
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plot

# setup
finalDict: Dict[str, MutableSequence[float]] = defaultdict(list)

# read csv
df = pd.read_csv('stack-overflow-annual-developer-survey-2022/survey_results_public.csv')

# filter out unnecessary columns and entries contains NaN 
df = df.filter(items=['Currency', 'CompTotal', 'CompFreq', 'LanguageHaveWorkedWith']).dropna()

# map yearly to monthly
df.loc[df['CompFreq'] == 'Yearly', 'CompTotal'] /= 12
del df['CompFreq']

# select USD salaries only, due to currency conversion issue (rate limit related)

df = df[df['Currency'] == 'USD	United States dollar']
del df['Currency']

# Filter dirty datas, there are several dirty datas that are have unreasonable high value

df = df[df['CompTotal'] < 100000] # Seems legit to me

# Mapping salary to dict

for idx, row in df.iterrows():
    compTotal = int(row['CompTotal'])
    languages = str(row['LanguageHaveWorkedWith']).split(';')
    for language in languages:
        finalDict[language].append(compTotal)

# Processing salary to mean value

usersDict = {k: len(v) for k, v in finalDict.items()}
finalDict = {k: mean(v) for k, v in finalDict.items()}

# Order by the value so plot won't being a mess

usersDict = sorted(usersDict.items(), key=lambda x: x[1])
finalDict = sorted(finalDict.items(), key=lambda x: x[1])

# Show it!

# Show salary first

plot.figure(0)
plot.plot(*zip(*finalDict))

# Then show users

plot.figure(1)
plot.plot(*zip(*usersDict))

# Finally show it!

plot.show()
