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

'''
                            1.SPEED
'''

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

'''
                        END of SPEED
                        2. COST
'''

list_cost = ['cost','price']

list_positive_cost_keywords = ['best','discounted','good','real steal for price','reasonable','4/5','lowest']
list_negative_cost_keywords = ['costly','price to be decrease','wasted','lose','not cheap','not comparative','rs.800 more','more','very high','higher','waste of money','highest','price low to attract customer','cheaper in market','damn high','much price']

dict_positive_revs_cost = {}
dict_negative_revs_cost = {}
dict_average_revs_cost = {}

count_positive_revs_cost = 0
count_negative_revs_cost = 0

#next: checking for the keywords in the reviews

for rev in list_reviews:
    for cost_key in list_cost:
        if cost_key in rev.lower():
            for pos_cost_keyy in list_positive_cost_keywords:
                if pos_cost_keyy in rev.lower():

                    count_positive_revs_cost += 1

                    if pos_cost_keyy in dict_positive_revs_cost:
                        dict_positive_revs_cost[pos_cost_keyy] += 1
                    else:
                        dict_positive_revs_cost[pos_cost_keyy] = 1

            for neg_cost_keyy in list_negative_cost_keywords:
                if neg_cost_keyy in rev.lower():

                    count_negative_revs_cost += 1

                    if neg_cost_keyy in dict_negative_revs_cost:
                        dict_negative_revs_cost[neg_cost_keyy] += 1
                    else:
                        dict_negative_revs_cost[neg_cost_keyy] = 1

#print(dict_positive_revs_cost)
#print(dict_negative_revs_cost)     both working

'''
next: plotting graph for COST
'''

x_len_cost = len(dict_positive_revs_cost) + len(dict_negative_revs_cost)
x_coor_cost = range(x_len_cost)

y_pos_revs_cost = []
bar_labels_pos_revs_cost = []
for i in dict_positive_revs_cost:
    bar_labels_pos_revs_cost.append(i)
    y_pos_revs_cost.append(dict_positive_revs_cost[i])

y_neg_revs_cost = []
bar_labels_neg_revs_cost = []
for i in dict_negative_revs_cost:
    bar_labels_neg_revs_cost.append(i)
    y_neg_revs_cost.append(dict_negative_revs_cost[i])

y_coor_cost = y_pos_revs_cost + y_neg_revs_cost
bar_labels_cost = bar_labels_pos_revs_cost + bar_labels_neg_revs_cost

color_cost = ['green']*len(dict_positive_revs_cost) + ['red']*len(dict_negative_revs_cost)

plt.bar(x_coor_cost, y_coor_cost, tick_label = bar_labels_cost, width = 0.4, color = color_cost)

plt.title('COST reviews')
plt.show()

'''
                    END of COST
                    3. LOOKS
'''

list_looks = ['looks', 'look']

list_positive_looks_keywords = ['sturdy and great', '5/5','cute', 'good', 'blue looks really good', 'slim', 'sexy', 'really good', 'best', 'aluminum face looks superb', 'great with a mac', 'truly stellar', 'mesmerizing', 'awesome', 'red good', 'Red color looks pretty and classy and very thin', 'Colour is shiny which attracts again and again', 'Mini mobile', 'nice and smaller than pic', 'stylish']
list_negative_looks_keywords = ['faulty',  'fragile']

dict_positive_revs_looks = {}
dict_negative_revs_looks = {}
dict_average_revs_looks = {}

count_positive_revs_looks = 0
count_negative_revs_looks = 0

#next: checking for the keywords in the reviews

for rev in list_reviews:
    for looks_key in list_looks:
        if looks_key in rev.lower():
            for pos_looks_keyy in list_positive_looks_keywords:
                if pos_looks_keyy in rev.lower():

                    count_positive_revs_looks += 1

                    if pos_looks_keyy in dict_positive_revs_looks:
                        dict_positive_revs_looks[pos_looks_keyy] += 1
                    else:
                        dict_positive_revs_looks[pos_looks_keyy] = 1

            for neg_looks_keyy in list_negative_looks_keywords:
                if neg_looks_keyy in rev.lower():

                    count_negative_revs_looks += 1

                    if neg_looks_keyy in dict_negative_revs_looks:
                        dict_negative_revs_looks[neg_looks_keyy] += 1
                    else:
                        dict_negative_revs_looks[neg_looks_keyy] = 1

#print(dict_positive_revs_cost)
#print(dict_negative_revs_cost)     both working

'''
next: plotting graph for LOOKS
'''

x_len_looks = len(dict_positive_revs_looks) + len(dict_negative_revs_looks)
x_coor_looks = range(x_len_looks)

y_pos_revs_looks = []
bar_labels_pos_revs_looks = []
for i in dict_positive_revs_looks:
    bar_labels_pos_revs_looks.append(i)
    y_pos_revs_looks.append(dict_positive_revs_looks[i])

y_neg_revs_looks = []
bar_labels_neg_revs_looks = []
for i in dict_negative_revs_looks:
    bar_labels_neg_revs_looks.append(i)
    y_neg_revs_looks.append(dict_negative_revs_looks[i])

y_coor_looks = y_pos_revs_looks + y_neg_revs_looks
bar_labels_looks = bar_labels_pos_revs_looks + bar_labels_neg_revs_looks

color_looks = ['green']*len(dict_positive_revs_looks) + ['red']*len(dict_negative_revs_looks)

plt.bar(x_coor_looks, y_coor_looks, tick_label = bar_labels_looks, width = 0.4, color = color_looks)

plt.title('LOOKS reviews')
plt.show()

'''
                    END of LOOKS
                    4.SIZE
'''

list_size = ['size']

list_positive_size_keywords = ['smaller', 'awesome', 'brilliant', 'wallet size', 'slimmest', '12mm', '10/10', 'compact', 'perfect', 'small', 'fits in pocket', 'very compact']
list_negative_size_keywords = ['big', 'heavy']

dict_positive_revs_size = {}
dict_negative_revs_size = {}
dict_average_revs_size = {}

count_positive_revs_size = 0
count_negative_revs_size = 0

#next: checking for the keywords in the reviews

for rev in list_reviews:
    for size_key in list_size:
        if size_key in rev.lower():
            for pos_size_keyy in list_positive_size_keywords:
                if pos_size_keyy in rev.lower():

                    count_positive_revs_size += 1

                    if pos_size_keyy in dict_positive_revs_size:
                        dict_positive_revs_size[pos_size_keyy] += 1
                    else:
                        dict_positive_revs_size[pos_size_keyy] = 1

            for neg_size_keyy in list_negative_size_keywords:
                if neg_size_keyy in rev.lower():

                    count_negative_revs_size += 1

                    if neg_size_keyy in dict_negative_revs_size:
                        dict_negative_revs_size[neg_size_keyy] += 1
                    else:
                        dict_negative_revs_size[neg_size_keyy] = 1

#print(dict_positive_revs_cost)
#print(dict_negative_revs_cost)     both working

'''
next: plotting graph for LOOKS
'''

x_len_size = len(dict_positive_revs_size) + len(dict_negative_revs_size)
x_coor_size = range(x_len_size)

y_pos_revs_size = []
bar_labels_pos_revs_size = []
for i in dict_positive_revs_size:
    bar_labels_pos_revs_size.append(i)
    y_pos_revs_size.append(dict_positive_revs_size[i])

y_neg_revs_size = []
bar_labels_neg_revs_size = []
for i in dict_negative_revs_size:
    bar_labels_neg_revs_size.append(i)
    y_neg_revs_size.append(dict_negative_revs_size[i])

y_coor_size = y_pos_revs_size + y_neg_revs_size
bar_labels_size = bar_labels_pos_revs_size + bar_labels_neg_revs_size

color_size = ['green']*len(dict_positive_revs_size) + ['red']*len(dict_negative_revs_size)

plt.bar(x_coor_size, y_coor_size, tick_label = bar_labels_size, width = 0.4, color = color_size)

plt.title('SIZE reviews')
plt.show()

'''
                    END of SIZE
'''

