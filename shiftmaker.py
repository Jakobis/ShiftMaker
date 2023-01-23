from collections import defaultdict, deque
from fileparser import parseFile

peoplePerShift = int(input("How many people per shift?"))
allPeople = set()
preferredShifts = set()
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def sorter(shift):
    day, time = shift.split()
    return (weekdays.index(day), int(time.split("-")[0]))

preferred, unpreferred = parseFile()
allPeople.update(preferred.keys())
allPeople.update(unpreferred.keys())

shiftsToPeople = defaultdict(set)
for person, shiftSet in preferred.items():
    for shift in shiftSet:
        preferredShifts.add((shift, person))
        shiftsToPeople[shift].add(person)

for person, shiftSet in unpreferred.items():
    for shift in shiftSet:
        shiftsToPeople[shift].add(person)

print(f"{len(shiftsToPeople)} shifts detected")

s = -1
e = -2
shifts = list(shiftsToPeople.keys())


def createGraph():
    graph = defaultdict(dict)
    for shift in shiftsToPeople:
        graph[s][shift] = peoplePerShift
        graph[shift][s] = 0
        for person in shiftsToPeople[shift]:
            graph[shift][person] = 1
            graph[person][shift] = 0
            graph[person][e] = 1
            graph[e][person] = 0
    return graph


graph = createGraph()


def dfs(maxOnShift, preferredOnly):
    scale = 1
    stack = deque([s])
    paths = {s: []}
    while stack:
        fro = stack.popleft()
        for to in graph[fro]:
            if preferredOnly and s not in [to, fro] and e not in [to, fro] and (fro, to) not in preferredShifts and (to, fro) not in preferredShifts:
                continue
            if graph[fro][to] >= scale and graph[to][fro] < maxOnShift and to not in paths:
                paths[to] = paths[fro] + [(fro, to)]
                if to == e:
                    return paths[e]
                stack.append(to)


def increaseFlow(maxOnShift, preferredOnly):
    totalFlow = 0
    path = dfs(maxOnShift, preferredOnly)
    while path:
        flow = min(graph[fro][to] for fro, to in path)
        totalFlow += flow
        for fro, to in path:
            graph[fro][to] -= flow
            graph[to][fro] += flow
        path = dfs(maxOnShift, preferredOnly)

for i in range(peoplePerShift):
    increaseFlow(i + 1, True)
    increaseFlow(i + 1, False)


answers = []
used = set()
shifts.sort(key=sorter)
for shift in shifts:
    answers.append(shift)
    for person in graph[shift].keys():
        if graph[shift][person] == 0 and person != -1:
            answers.append(f"{person}")
            used.add(person)
    answers.append("")
answers.append("unused")
answers.extend([x for x in allPeople if x not in used])
print("\n".join(answers))
