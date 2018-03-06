'''
status:
    -categorised all the +ve & -ve reviews for speed
    -next: draw a bar graph for all review keywords for speed
    -next: do the same for price factor
'''

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
count_positive_revs_for_speed = 0 #initial positive and negative reviews
count_negative_revs_for_speed = 0

'''
                    SPEED!
    1st: check for speed keywords in the list of reviews
    2nd: if found, check for positive/negative keywords in the review list
'''
for rev in list_reviews:
    for speed in list_speed:
        if speed in rev.lower():
            for pos in list_positive_rev_for_speed:
                if pos in rev.lower():
                    count_positive_revs_for_speed += 1

                    if pos in dict_no_positive_reviews_for_speed:
                        dict_no_positive_reviews_for_speed[pos] += 1
                    else:
                        dict_no_positive_reviews_for_speed[pos] = 1
            
            for neg in list_negative_for_speed:
                if neg in rev.lower():
                    count_negative_revs_for_speed += 1

                    if neg in dict_no_negative_reviews_for_speed:
                        dict_no_negative_reviews_for_speed[neg] += 1
                    else:
                        dict_no_negative_reviews_for_speed[neg] = 1
                    
#print(dict_no_positive_reviews_for_speed)
#print(dict_no_negative_reviews_for_speed)

#print("pos:", count_positive_revs_for_speed, "neg:", count_negative_revs_for_speed)

'''
Up next: Plotting the bar graph for +ve reviews of SPEED
'''

import matplotlib.pyplot as plt

total_x_coor = len(dict_no_positive_reviews_for_speed) + len(dict_no_negative_reviews_for_speed)
x = range(total_x_coor)
#how many +ve distinct keywords are present, to be on x-axis

#y = [count_positive_revs_for_speed, count_negative_revs_for_speed]
#bar_labels = ['+ve', '-ve']

y_pos = []
bar_labels_pos = []
for i in dict_no_positive_reviews_for_speed:
    bar_labels_pos.append(i)
    y_pos.append(dict_no_positive_reviews_for_speed[i])


y_neg = []
bar_labels_neg = []
for i in dict_no_negative_reviews_for_speed:
    bar_labels_neg.append(i)
    y_neg.append(dict_no_negative_reviews_for_speed[i])

y = y_pos + y_neg
bar_labels = bar_labels_pos + bar_labels_neg

#y = y_pos
#bar_labels = bar_labels_pos

color = ['green']*len(dict_no_positive_reviews_for_speed) + ['red']*len(dict_no_negative_reviews_for_speed)

plt.bar(x, y, tick_label = bar_labels, width = 0.4, color = color)

plt.title('Hard-Disk review for SPEED')
plt.show()

