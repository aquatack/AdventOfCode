# Open the file in read mode
reports = []
with open('Day02/testdata.txt', 'r') as file:
    # Read each line from the file
    
    for line in file:
        report = [int(num) for num in line.split()]
        print(report)
        reports.append(report)
    
def issafe(report) -> bool:
    # calculate the differences between each element in the list

    #def getnextvalue(report):


    diffs = []
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        #diff2 = report[i] - report[i+2]
        #sign = diff > 0

        diffs.append(diff)
    #print(diffs)

    # check they're all the same sign
    sign0 = diffs[0] > 0
    safetybreaches = 0
    for diff in diffs:
        if (diff > 0) != sign0:
            safetybreaches += 1

    # check if the abs differences are all between 1 and 3
    for diff in diffs:
        if abs(diff) > 3:
            safetybreaches += 1
        if abs(diff) < 1:
            safetybreaches += 1

    if safetybreaches > 0:
        return False
    
    return True

def countsafereports(reports) -> int:
    safereports = 0
    for report in reports:
        safereports += 1 if issafe(report) else 0

    return safereports
           
print(countsafereports(reports))


