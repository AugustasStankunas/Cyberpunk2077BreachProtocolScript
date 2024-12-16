import numpy as np
from copy import deepcopy

def calculateRoute(startArray: np.ndarray, goals: np.ndarray, bufferLength: int, mask):
    solutions = set()
    solutions = row(startArray[0], 0, -1, [], bufferLength, goals, startArray, mask, solutions)
    sorted_solutions = sorted(list(solutions), key=lambda x: (-x[1], len(x[0])))
    print("First 3 solutions")
    for i in range(min(3, len(sorted_solutions))):
        print(sorted_solutions[i])

def row(row, rowIndex, columnIndex, builtPath, bufferLength, goals, startArray, mask, solutions):
    if len(builtPath) == bufferLength or goalCount(builtPath, goals) == len(goals):
        count = goalCount(builtPath, goals)
        if count >= 1: 
            solutions.add((tuple(builtPath), count))
        return solutions
    
    if builtPath == ['1C', 'E9']:
        print('here')
    
    for i in range(len(row)):
        if i != columnIndex and mask[rowIndex, i] == False:
            builtPath.append(str(row[i]))
            mask[rowIndex, i] = True
            solutions = column(startArray[:, i], rowIndex, i, builtPath, bufferLength, goals, startArray, mask, solutions)
            mask[rowIndex, i] = False
            builtPath.pop()

    return solutions
    

def column(column, rowIndex, columnIndex, builtPath, bufferLength, goals, startArray, mask, solutions):
    if len(builtPath) == bufferLength or goalCount(builtPath, goals) == len(goals):
        count = goalCount(builtPath, goals)
        if count >= 1: 
            solutions.add((tuple(builtPath), count))
        return solutions
    
    if builtPath == ['1C', 'E9', '55']:
        print('here')
    
    for i in range(len(column)):
        if i != rowIndex and mask[i, columnIndex] == False:
            builtPath.append(str(column[i]))
            mask[i, columnIndex] = True
            solutions = row(startArray[i], i, columnIndex, builtPath, bufferLength, goals, startArray, mask, solutions)
            mask[i, columnIndex] = False
            builtPath.pop()

    return solutions


def goalCount(path, goals):
    count = 0
    for goal in goals:
        for i in range(len(path) - len(goal) + 1):
            if path[i:i + len(goal)] == goal:
                count += 1
                break

    return count

def main():
    array = np.array([
    ['1C', '1C', '1C', '1C', '1C'],
    ['E9', 'E9', 'E9', 'E9', '1C'],
    ['1C', '1C', 'BD', '1C', '1C'],
    ['E9', 'E9', '1C', 'E9', 'E9'],
    ['BD', 'BD', 'E9', '55', '1C']
])
    mask = np.zeros(array.shape, dtype=bool)
    goals = [
    ['BD', 'E9'],
    ['1C', '1C'],
    ['1C', 'E9', 'E9', 'E9']
    ]
    bufferLength = 4
    calculateRoute(array, goals, bufferLength, mask)

if __name__ == "__main__":
    main()