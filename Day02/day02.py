# Open the file in read mode

reports = []
with open('Day02/fulldata.txt', 'r') as file:
    # Read each line from the file

    for line in file:
        report = [int(num) for num in line.split()]
        # print(report)
        reports.append(report)


def issafe(report) -> bool:

    diffs = []
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        # diff2 = report[i] - report[i+2]
        # sign = diff > 0

        diffs.append(diff)
    # print(diffs)

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

    if safetybreaches == 0:
        return True

    return False


def issafedampened(report) -> bool:

    for i in range(len(report)):

        report2 = report[0:i]
        report2.extend(report[i+1:])
        # print(report, report2)
        if issafe(report2):
            return True

    return False


def countsafereports(reports) -> int:
    safereports = 0
    unsafereports = []
    for report in reports:
        result = issafe(report)
        if result == False:
            unsafereports.append(report)

        safereports += 1 if result else 0
        # print(result, safereports)

    for unsaferport in unsafereports:
        result = issafedampened(unsaferport)
        if (result):
            safereports += 1
            # print(result, safereports)

    return safereports


print(countsafereports(reports))
