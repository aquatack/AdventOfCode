import pandas as pd

list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

df= pd.read_csv('./Day01/day01.csv', header=None)
list1 = df.iloc[:,0].tolist()
list2 = df.iloc[:,1].tolist()
#list2 = df['list2'].tolist()

list1.sort()
list2.sort()

cumdiff = 0

#for i in range(len(list1)):
#    absdiff = abs(list1[i] - list2[i])
#    cumdiff += absdiff
#    print(i, list1[i], list2[i], absdiff, cumdiff)

cumdist = 0
for i in range(len(list1)):
    matches = [j for j in range(len(list2)) if list2[j] == list1[i]]
    distance = list1[i] * len(matches)
    cumdist += distance
    print(matches, len(matches), distance, cumdist)