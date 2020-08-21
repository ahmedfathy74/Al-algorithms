'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import math


class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense


def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0, labels[0]))
    data.append(item(0, 0, 0, 1, labels[1]))
    data.append(item(0, 0, 1, 0, labels[2]))
    data.append(item(0, 0, 1, 1, labels[3]))
    data.append(item(0, 1, 0, 0, labels[4]))
    data.append(item(0, 1, 0, 1, labels[5]))
    data.append(item(0, 1, 1, 0, labels[6]))
    data.append(item(0, 1, 1, 1, labels[7]))
    data.append(item(1, 0, 0, 0, labels[8]))
    data.append(item(1, 0, 0, 1, labels[9]))
    data.append(item(1, 0, 1, 0, labels[10]))
    data.append(item(1, 0, 1, 1, labels[11]))
    data.append(item(1, 1, 0, 0, labels[12]))
    data.append(item(1, 1, 0, 1, labels[13]))
    data.append(item(1, 1, 1, 0, labels[14]))
    data.append(item(1, 1, 1, 1, labels[15]))
    data.append(item(1, 0, 0, 0, labels[16]))
    data.append(item(1, 0, 0, 1, labels[17]))
    data.append(item(1, 0, 1, 0, labels[18]))
    data.append(item(1, 0, 1, 1, labels[19]))
    data.append(item(1, 1, 0, 0, labels[20]))
    return data


class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1
        self.child = []
        self.zero_pure = -1
        self.one_pure = -1
        self.des_zero = -1
        self.des_one = -1
        self.index = 0


tree = []
tree.append(Feature("ay_haga"))
tree.clear()
visited = {"feat"}
visited.clear()
age_entropy = 0
prescription_entropy = 0
astigmatic_entropy = 0
tear_entropy = 0


class ID3:
    def __init__(self, features):
        self.features = features

    def classify(self, input):
        # takes an array for the features ex. [0, 0, 1, 1]
        # should return 0 or 1 based on the classification
        # tree = [1]
        # tree.clear()
        build_my_tree(dataset, Feature("ay_haga"))
        tmpTree = []

        # for index in range(len(tree)):
        #     tmpTree.append(tree[index])
        # tree = tmpTree
        for i in range(len(tree)):
            x = tree[len(tree)-1-i]
            if input[x.index] == 0:
                if x.zero_pure == 1:
                    return x.des_zero
            else:
                if x.one_pure == 1:
                    return x.des_one



def build_my_tree(data, parent):
    # parent.name != "ay_haga" and
    if len(visited) == 4 or (parent.zero_pure == 1 and parent.one_pure == 1):
      if len(visited) == 4:
          return None,data[0].needLense
      else:
          return -100, -100

    total_entropy = totentropy(data)
    if total_entropy != 0.0:
        top_of_tree = infogain(data, total_entropy)
        tables = split_tables(data, top_of_tree.name)
        # for i in tables:
        #    #check if table00 is pure or not
        if top_of_tree.zero_pure == -1:
            zero_ret, value = build_my_tree(tables[0], top_of_tree)
            if zero_ret is None and value is not -100:
                top_of_tree.zero_pure = 1
                top_of_tree.des_zero = value
            if zero_ret is None :
                top_of_tree.zero_pure = 1
                top_of_tree.des_zero = value
        if top_of_tree.one_pure == -1:
            one_ret, value = build_my_tree((tables[1]), top_of_tree)
            if one_ret is None and value is not -100:
                top_of_tree.one_pure = 1
                top_of_tree.des_one = value
            if one_ret is None:
                top_of_tree.one_pure = 1
                top_of_tree.des_one = value
        top_of_tree.child.append(tables[0])
        top_of_tree.child.append(tables[1])
        tree.append(top_of_tree)
        return top_of_tree.one_pure, value


    else:
        return None, data[0].needLense


def split_tables(data, feature1):
    list_1 = []
    list_0 = []
    list2 = [0, 1]
    l = 0
    for f in list2:
        for item in data:
            if item.age == f and feature1 == "age":
                if f == 0:
                    list_0.append(item)
                else:
                    list_1.append(item)
            elif item.needLense == f and feature1 == "needLense":
                if f == 0:
                    list_0.append(item)
                else:
                    list_1.append(item)
            elif item.prescription == f and feature1 == "prescription":
                if f == 0:
                    list_0.append(item)
                else:
                    list_1.append(item)
            elif item.tearRate == f and feature1 == "tearRate":
                if f == 0:
                    list_0.append(item)
                else:
                    list_1.append(item)
            elif item.astigmatic == f and feature1 == "astigmatic":
                if f == 0:
                    list_0.append(item)
                else:
                    list_1.append(item)
    return list_0, list_1


def totentropy(data):
    counter0 = 0
    counter1 = 0
    final = 0.0
    if len(visited) == 4 or len(data) == 0:
        return
    for h in range(0, len(data)):
        if data[h].needLense == 0:
            counter0 += 1
        elif data[h].needLense == 1:
            counter1 += 1
    rst0 = counter0 / len(data)
    rst1 = counter1 / len(data)
    if rst0 == 0 or rst1 == 0:
        return final
    if rst0 != 0.0:
        final = - rst0 * math.log(rst0, 2)
    if rst1 != 0.0:
        final = final - rst1 * math.log(rst1, 2)
    return final


def infogain(data, total_entropy):
    max_gain = 0.0
    tmp_of_max = 0
    if len(visited) == 4 or len(data) == 0:
        return
    for j in range(0, len(features)):
        if features[j].visited == -1:
            information_gain = total_entropy
            list_of_zeros, list_of_ones = split_tables(data, features[j].name)
            information_gain = information_gain - ((len(list_of_zeros) / len(data)) * totentropy(list_of_zeros))
            information_gain -= ((len(list_of_ones) / len(data)) * totentropy(list_of_ones))
            if information_gain > max_gain:
                max_gain = information_gain
                tmp_of_max = j
    features[tmp_of_max].infoGain = max_gain
    features[tmp_of_max].visited = 1
    visited.add(features[tmp_of_max].name)
    features[tmp_of_max].index = tmp_of_max
    return features[tmp_of_max]


dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1])  # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0])  # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0])  # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1])  # should print 1
print('testcase 4: ', cls)
