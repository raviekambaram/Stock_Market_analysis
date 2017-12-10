# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:34:01 2017

@author: Shree
"""

# Example of kNN implemented from Scratch in Python

import csv
import random
import math
import operator
from operator import itemgetter
import xlrd


def loadDataset(filename, split, trainingSet=[], testSet=[],dateSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(3):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(itemgetter(0,1,2)(dataset[x]))
            else:
                testSet.append(itemgetter(0,1,2)(dataset[x]))
                dateSet.append(dataset[x][3])



def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def main():
    trainingSet = []
    testSet = []
    DateSet = []
    split = 0.67
    loadDataset('mmm.csv', split, trainingSet, testSet,DateSet)
    predictions = []
    k = 5
    with open("mmm_result.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Predicted", "Actual"])
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
            writer.writerow([DateSet[x],repr(result), repr(testSet[x][-1])])
    f.close

main()
