import collections
import random2

class cocktail_quantum_sort:

    def __init__(self, arr: list):
        self.occupied_indexes = []
        self.list = arr
        self.linklist = {}
        self.final_list = []
        self.biggest_i = None
        self.lowest_i = None

    def getelements(self):
        arr = self.list
        biggest_i = 0
        biggest_index = 0
        for x in range(len(arr)):
            if arr[x] > biggest_i and x not in self.occupied_indexes:
                biggest_index = x
                biggest_i = arr[x]

        self.occupied_indexes.append(biggest_index)
        if self.biggest_i == None:
            self.biggest_i = biggest_i

        lowest_index = biggest_index
        lowest_i =  biggest_i

        for x in range(len(arr)):
            if arr[x] < lowest_i and x not in self.occupied_indexes:
                lowest_index = x
                lowest_i = arr[x]

        self.occupied_indexes.append(lowest_index)
        if self.lowest_i == None:
            self.lowest_i = lowest_i

        self.linklist[abs(biggest_i - lowest_i)] = [lowest_i, biggest_i]
    
    def createlists(self):
        for x in range(round(len(self.list)/2)):
            self.getelements()

    def finally_sort(self):
        for x in range(abs(self.biggest_i - self.lowest_i)):
            try:
                if self.linklist[x][0] == self.linklist[x][1]:
                    self.final_list.append(self.linklist[x][0])
                else:
                    self.final_list.insert(0, self.linklist[x][0])
                    self.final_list.append(self.linklist[x][1])
            except KeyError:
                continue

    
    def print_everything(self):
        print(self.list)
        print(self.occupied_indexes)
        print(self.linklist)
        print(self.final_list)

    def print_sorted(self):
        print(self.final_list)



randomlist = []
length = 1000
for i in range(length):
    n = random2.randint(1,length*2)
    if n not in randomlist:
        randomlist.append(n)

print(randomlist)
x = cocktail_quantum_sort(randomlist)
x.createlists()
x.finally_sort()
x.print_sorted()