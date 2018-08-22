#list methods---------------------------------------------------------
#Python List append()	Add Single Element to The List
#Python List extend()	Add Elements of a List to Another List
#Python List insert()	Inserts Element to The List
#Python List remove()	Removes Element from the List
#Python List index()	returns smallest index of element in list
#Python List count()	returns occurrences of element in a list
#Python List pop()	Removes Element at Given Index
#Python List reverse()	Reverses a List
#Python List sort()	sorts elements of a list
#Python List copy()	Returns Shallow Copy of a List
#Python List clear()	Removes all Items from the List
#Python any()   	Checks if any Element of an Iterable is True
#Python all()	        returns true when all elements in iterable is true
#Python ascii()	        Returns String Containing Printable Representation
#Python bool()	        Coverts a Value to Boolean
#Python enumerate()	Returns an Enumerate Object
#Python filter()	constructs iterator from elements which are true
#Python iter()	        returns iterator for an object
#Python list()          Function creates list in Python
#Python len()	        Returns Length of an Object
#Python max()	        returns largest element
#Python min()	        returns smallest element
#Python map()	        Applies Function and Returns a List
#Python reversed()	returns reversed iterator of a sequence
#Python slice()	        creates a slice object specified by range()
#Python sorted()	returns sorted list from a given iterable
#Python sum()	        Add items of an Iterable
#Python zip()	        Returns an Iterator of Tuples
#---------------------------------------------------------------------

#Ini Quick Sort-------------------------------------------------------
import random

class Quick(object):
    def particao(self, a, ini, fim):
        pivo = a[fim-1]
        start = ini
        end = ini
        for i in range(ini,fim):
            if a[i] > pivo:
                end += 1
            else:
                end += 1       
                start += 1
                aux = a[start-1]
                a[start-1] = a[i]
                a[i] = aux
        return start-1
        
    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.randparticao(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp+1,fim)
        return a
        
    def randparticao(self,a,ini,fim):
        rand = random.randrange(ini,fim)
        aux = a[fim-1]
        a[fim-1] = a[rand]
        a[rand] = aux
        return self.particao(a,ini,fim)
    
a = [8,5,12,55,3,7,82,44,35,25,41,29,17]
print (a)
q = Quick()
print (q.quickSort(a,0,len(a)))
print("End Quick Sort Program-----------------------------------------")
#End Quick Sort-------------------------------------------------------
#Tem o método sorted(list); também que retorna uma lista ordenada
#sorted(list, key=..., reverse=...) ou list.sort(key=..., reverse=...)

#dictionary----------------------------------------------------------
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#update
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#delete
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#lista de entidades
dic = [];
dic.append({'a':3});
print(dic[0]['a']);
#--------------------------------------------------------------------

#Binary Tree---------------------------------------------------------
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
#--------------------------------------------------------------------

#Binary Search Tree--------------------------------------------------
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
#--------------------------------------------------------------------

#Binary Search Divide and Conquer------------------------------------
def bsearch(list, val):

    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size
# Find the middle most value

    while idx0 <= idxn:
        midval = (idx0 + idxn)// 2

        if list[midval] == val:
            return midval
# Compare the value the middle most value
        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1

    if idx0 > idxn:
        return None
# Initialize the sorted list
list = [2,7,19,34,53,72]

# Print the search result
print(bsearch(list,72))
print(bsearch(list,11))
#-------------------------------------------------------------------
