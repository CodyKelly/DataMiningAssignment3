import matplotlib.pyplot as plt
import collections
import math
from itertools import combinations
import time
import csv
from anytree import Node, RenderTree


dataset_name =   'retail.txt'     # dataset_name: that is the dataset name (such as dataset.txt)
patterns_path =  'patterns.csv'   # the file name that will store the frequent patterns
negative_path = 'negative.csv'    # the file name that will store the negatively correlated items
rules_path =     'rules.csv'      # the file name that will store the maximal patterns
maximal_path =   'maximal.csv'    # the file name that will store the association rules
min_support =     0.0015          # minimum support threshold which is in percentage format (for example 0.2 means 20%)
min_confidence =  0.9             # the minimum confidence threshold in the percentage format

support_counts = {}
transactions = []
total_items = 0

with open(dataset_name) as file:
    for line in file:
        transaction = []
        for item in line.split():
            intitem = int(item)
            if intitem not in support_counts:
                support_counts[intitem] = 1
            else:
                support_counts[intitem] += 1
            transaction.append(intitem)
            total_items += 1
        transactions.append(transaction)

# sorted_support_counts = [k for k, v in sorted(support_counts.items(), key=lambda item: item[1], reverse=True) if v > round(min_support * len(items))]

for i in range(len(transactions)):
    transaction = transactions[i]
    transactions[i] = ([item for item in sorted(transaction, key=lambda x: support_counts[x], reverse=True) if
                        support_counts[item] > round(min_support * total_items)])

print(transactions)

class Node:
    def __init__(self, tid, parent):
        self.tid = tid
        self.count = 0
        self.parent = parent
        self.children = []
    def __str__(self):
        print(f"tid: {self.tid}, children: {[child.tid for child in self.children]}")
        for child in self.children:
            print(child)

root_node = Node(-1, None)
for transaction in transactions:
    current_node = root_node
    for item in transaction:
        child_found = False
        for child in current_node.children:
            if child.tid == item:
                child.count += 1
                current_node = child
                child_found = True
                break
        if not child_found:
            new_child = Node(item, current_node)
            new_child.count += 1
            current_node.children.append(new_child)

print(root_node)