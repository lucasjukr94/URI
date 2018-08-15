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

#Ini Array Methods----------------------------------------------------
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
        print( self.data);
        if self.right:
            self.right.PrintTree()

    def GetTree(self):
        if self.left:
            return(str(self.data)+";"+str(self.left.GetTree()));
        if self.right:
            return(str(self.data)+";"+str(self.right.GetTree()));
        return(str(self.data)+";");

    def GetTreeArray(self):
        arr = [];
        #self.PrintTree();
        arr = self.GetTree();
        i=0;
        arrReal = [];
        val = '';
        while(i<len(arr)):
            if(arr[i]!=';'):
                val = str(val) + str(arr[i]);
            else:
                arrReal.append(int(val));
                val = '';
            i+=1;
        return arrReal;
        
class ArrayMethods(object):
    #inverte a array
    def Invert(self,*array):
        #convertendo tupla para array
        ar = [];
        ar.append(*array);#array[0][n]
        ar2 = [];
        ar2 = ar[0];#array[n]
        #----------------------------
        i=len(*array);
        arr = [];
        while(i>0):
            i-=1;
            arr.append(ar2[i]);
        return arr;

    #organiza a array em forma de árvore binária
    def BinaryTree(self,*array):
        #convertendo tupla para array
        ar = [];
        ar.append(*array);#array[0][n]
        ar2 = [];
        ar2 = ar[0];#array[n]
        #----------------------------
        arr = [];
        i=1;
        root = Node(ar2[0]);
        while(i<len(ar2)):
            root.insert(ar2[i]);
            i+=1;
        arr = root.GetTreeArray();
        return arr;

    def BinarySearch(self,*array,val):
        #convertendo tupla para array
        ar = [];
        ar.append(*array);#array[0][n]
        ar2 = [];
        ar2 = ar[0];#array[n]
        #----------------------------
        self.BinaryTree(ar2);#Transforma a array para uma árvore binária p/ a busca
        #Fazendo a Busca Binária
        #True se a árvore possuir o valor e False para o contrário
        
        #---------------------------------------------------------
        return True;
    
a = [8,5,12,55,3,7,82,44,35,25,41,29,17];
q = Quick();
quicked = q.quickSort(a,0,len(a));#Quick Sort

am = ArrayMethods();
print(am.Invert(quicked));#Invert Array
print(am.BinaryTree(quicked));#Get Binary Tree Array
am.BinarySearch(quicked,val=1);
print("End Array Methods Program--------------------------------------")
#End Array Methods----------------------------------------------------
