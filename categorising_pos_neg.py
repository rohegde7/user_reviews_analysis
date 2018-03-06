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

list_speed = ['speed', 'clock']
list_positive_rev_for_speed = ['best', 'lovely', 'great', 'fast', 'good']
list_negative_for_speed = ['disappointed', 'utterly', 'hate', 'worst', 'worthless', 'cheated', 'waste', 'bad']
dict_no_negative_reviews_for_speed = {}
dict_no_positive_reviews_for_speed = {}
positive_revs = 0 #initial positive and negative reviews
negative_revs = 0

'''
    1st: check for speed keywords in the list of reviews
    2nd: if found, check for positive/negative keywords in the review list
'''
for rev in list_reviews:
    for speed in list_speed:
        if speed in rev.lower():
            for pos in list_positive_rev_for_speed:
                if pos in rev.lower():
                    positive_revs += 1

                    if pos in dict_no_positive_reviews_for_speed:
                        dict_no_positive_reviews_for_speed[pos] += 1
                    else:
                        dict_no_positive_reviews_for_speed[pos] = 1
            
            for neg in list_negative_for_speed:
                if neg in rev.lower():
                    negative_revs += 1

                    if neg in dict_no_negative_reviews_for_speed:
                        dict_no_negative_reviews_for_speed[neg] += 1
                    else:
                        dict_no_negative_reviews_for_speed[neg] = 1
                    
print(dict_no_positive_reviews_for_speed)
print(dict_no_negative_reviews_for_speed)

#print("pos:", positive_revs, "neg:", negative_revs)
#working but cannot confirm the accuracy

'''
Up next: Plotting the bar graph for +ve and -ve revs
'''

import matplotlib.pyplot as plt

x_coordinates = [1,2]
list_height = [positive_revs, negative_revs]

bar_labels = ['+ve', '-ve']

plt.bar(x_coordinates, list_height, tick_label = bar_labels, width = 0.8, color = ['green', 'red'])

plt.title('Hard-Disk review for SPEED')
plt.show()

'''
Next: plotting bar graph for number of times different review words have occured
'''

x_coordinates = [1,2]
list_height = [positive_revs, negative_revs]

bar_labels = ['+ve', '-ve']

plt.bar(x_coordinates, list_height, tick_label = bar_labels, width = 0.8, color = ['green', 'red'])

plt.title('Review words frequency')
plt.show()