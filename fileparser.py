from collections import defaultdict
import csv


def parseFile():
    path = "/home/jakobis/PycharmProjects/Kattis/.other/shiftmaker/data/Analog3.csv"

    file = open(path, newline='', encoding='utf-8')
    reader = csv.reader(file)
    lines = [row for row in reader]
    preferred = defaultdict(set)
    unpreferred = defaultdict(set)

    for line in lines[1:]:
        name = line[1]
        preferredString = line[3]
        unpreferredString = line[2]
        for shift in preferredString.split(", "):
            if shift == "":
                continue
            preferred[name].add(shift)
        for shift in unpreferredString.split(", "):
            if shift == "":
                continue
            if shift not in preferred[name]:
                unpreferred[name].add(shift)
    return preferred, unpreferred

parseFile()