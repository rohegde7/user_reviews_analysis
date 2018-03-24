'''
status:
    -categorised all the +ve & -ve reviews
    -done: draw a bar graph for all review keywords for Speed
    -next: do the same for Price factor
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
list_negative_for_speed = ['average', 'disappointed', 'utterly', 'hate', 'worst', 'worthless', 'cheated', 'waste', 'bad']
dict_no_negative_reviews_for_speed = {}
dict_no_positive_reviews_for_speed = {}
dict_rating_reviews_for_speed = {}
dict_speed_nums_reviews_for_speed = {}
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
            break

'''for checking USB speed now: '''
list_speed_usb = ['usb', 'read-write', 'speed']
list_usb_speed_numbers = []
for rev in list_reviews:
    for speed in list_speed_usb:
        if speed in rev.lower():
            import re   #regular expression
            #finding all digits:
            #list_usb_speed_numbers = list(map(int, re.findall(r'\d+', str(rev.lower))))
            
            list_rating_numbers_raw = list(re.findall(r'[:|\ ](\d+)\/(\d+)\ ', str(rev)))
            #ex. 5/5, 4/5, 9/10 (here dates such as 20/04/17 will be ignored)
            #print(list_rating_numbers_raw)
            
            list_rating_numbers_sorted = []

            for i in list_rating_numbers_raw:
                list_rating_numbers_sorted.append(i[0] + '/' + i[1])
                #print(list_rating_numbers_sorted) #working

                for j in list_rating_numbers_sorted:
                    if j in dict_rating_reviews_for_speed:
                        dict_rating_reviews_for_speed[j] += 1
                    else:
                        dict_rating_reviews_for_speed[j] = 1

            list_speed_numbers_raw = list(re.findall(r'[:|\ ](\d+)\-(\d+)\ ', str(rev)))
            #ex. 5/5, 4/5, 9/10 (here dates such as 20/04/17 will be ignored)
            #print(list_rating_numbers_raw)
            
            list_speed_numbers_sorted = []

            for i in list_speed_numbers_raw:
                list_speed_numbers_sorted.append(i[0] + '-' + i[1])

                for j in list_speed_numbers_sorted:
                    if j in dict_speed_nums_reviews_for_speed:
                        dict_speed_nums_reviews_for_speed[j] += 1
                    else:
                        dict_speed_nums_reviews_for_speed[j] = 1

                    
#print(dict_no_positive_reviews_for_speed)
#print(dict_no_negative_reviews_for_speed)
#print(dict_rating_reviews_for_speed)

#print("pos:", count_positive_revs_for_speed, "neg:", count_negative_revs_for_speed)

'''
Up next: Plotting the bar graph for +ve reviews of SPEED
'''

import matplotlib.pyplot as plt

total_x_coor = len(dict_no_positive_reviews_for_speed) + len(dict_no_negative_reviews_for_speed) + len(dict_rating_reviews_for_speed) + len(dict_speed_nums_reviews_for_speed)
x = range(total_x_coor)
#how many +ve/-ve/average/rating distinct keywords are present, to be on x-axis

#y = [count_positive_revs_for_speed, count_negative_revs_for_speed]
#bar_labels = ['+ve', '-ve']

y_pos_reviews = []
bar_labels_pos_reviews = []
for i in dict_no_positive_reviews_for_speed:
    bar_labels_pos_reviews.append(i)
    y_pos_reviews.append(dict_no_positive_reviews_for_speed[i])


y_neg_reviews = []
bar_labels_neg_reviews = []
for i in dict_no_negative_reviews_for_speed:
    bar_labels_neg_reviews.append(i)
    y_neg_reviews.append(dict_no_negative_reviews_for_speed[i])


y_rating_reviews = []
bar_labels_rating_reviews = []
for i in dict_rating_reviews_for_speed:
    bar_labels_rating_reviews.append(i)
    y_rating_reviews.append(dict_rating_reviews_for_speed[i])

y_speed_nums_reviews = []
bar_labels_speed_nums_reviews = []
for i in dict_speed_nums_reviews_for_speed:
    bar_labels_speed_nums_reviews.append(i)
    y_speed_nums_reviews.append(dict_speed_nums_reviews_for_speed[i])


y = y_pos_reviews + y_neg_reviews + y_rating_reviews + y_speed_nums_reviews
bar_labels = bar_labels_pos_reviews + bar_labels_neg_reviews + bar_labels_rating_reviews + bar_labels_speed_nums_reviews

#print(bar_labels + bar_labels_rating_reviews)
#print(y + y_rating_reviews)

#y = y_pos_reviews
#bar_labels = bar_labels_pos_reviews

color = ['green']*len(dict_no_positive_reviews_for_speed) + ['red']*len(dict_no_negative_reviews_for_speed) + ['orange']*len(dict_rating_reviews_for_speed) + ['yellow']*len(dict_speed_nums_reviews_for_speed)

plt.bar(x, y, tick_label = bar_labels, width = 0.4, color = color)

plt.title('Hard-Disk review for SPEED')
plt.show()