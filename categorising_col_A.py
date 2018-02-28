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

print(list_reviews)    #working

