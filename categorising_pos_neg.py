import pandas as pd

xl_DataFrame = pd.read_excel('external-hard-disk-drive.xlsx')    #stores in the form of a DataFrame object
#xl_DataFrame = pd.read_excel('test.xls', usecols=2)    #stores in the form of a DataFrame object

#print(xl_DataFrame.iloc[2,1])  #working

xl_shape = xl_DataFrame.shape   #returns the no. of rows and cols in a tuple form
no_records = xl_shape[0]    #extracting the no. of rows
#print(no_records)

list_reviews = []   #stores all the records from column 2 which we need to analyse
for i in range(no_records):
    list_reviews.append(xl_DataFrame.iloc[i, 1])
    # 1 because we need the 2nd column review only
    # i represents the 'i'th row/record

#print(list_reviews)    #working

list_speed = ['speed']
list_positive = ['best', 'lovely', 'great', 'fast', 'good']
list_negative = ['disappointed', 'utterly', 'hate', 'worst', 'worthless', 'cheated', 'waste']

positive_revs = 0 #initial positive and negative reviews
negative_revs = 0

'''
    1st: check for speed keywords in the list of reviews
    2nd: if found, check for positive/negative keywords in the review list
'''
for rev in list_reviews:
    for speed in list_speed:
        if speed in rev.lower():
            for pos in list_positive:
                if pos in rev.lower():
                    positive_revs += 1
            
            for neg in list_negative:
                if neg in rev.lower():
                    negative_revs += 1

#print("pos:", positive_revs, "neg:", negative_revs)
#working but cannot confirm the accuracy

'''
For plotting the graphs: visit plotting_graph.py
'''

import matplotlib.pyplot as plt

x_cooirdinates = [1,2]
list_height = [positive_revs, negative_revs]

bar_labels = ['+ve', '-ve']

plt.bar(x_cooirdinates, list_height, tick_label = bar_labels, width = 0.8, color = ['green', 'red'])

plt.title('Hard-Disk review')
plt.show()





