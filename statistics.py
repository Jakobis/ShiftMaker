from collections import defaultdict

from fileparser import parseFile

preferred, unpreferred = parseFile()


allPeople = list(set(preferred.keys()).union(set(unpreferred.keys())))
allShifts = list(set([item for x in preferred for item in preferred[x]]).union(set([item for x in unpreferred for item in unpreferred[x]])))
peopleCount = defaultdict(int)

ableForPeople = preferred.copy()
for person in ableForPeople:
    ableForPeople[person].update(unpreferred[person])

ableForShifts = defaultdict(set)
for person in preferred:
    for shift in preferred[person]:
        ableForShifts[shift].add(person)
        peopleCount[person] += 1


allPeople.sort(key=lambda x: (peopleCount[x], x))
allShifts.sort(key=lambda x: (len(ableForShifts[x]), x))

print("How many shifts can each person take")
for p in allPeople:
    print(f"{p}: {peopleCount[p]}")
print()
print("How many people are available for each shift")
for p in allShifts:
    print(f"{p}: {len(ableForShifts[p])}")

print()
print("Who are available for each shift")
for shift in allShifts:
    print(f"{shift}: {ableForShifts[shift]}")