#Complete this class definition

#It is recommended you create a node class and additional methods

myPreorder=[]
myInorder=[]
myPostorder=[]
class Node:
\tdef __init__(self,value):
\t\tself.__value = value
\t\tself.__left = None
\t\tself.__right = None 
\t\t
\t\treturn
\t
\t# def __str__(self):
\t#\t result = '[ '+str(self.__value)+' ]'
\t#\t return result
\t\t
\tdef getLeft(self):
\t\treturn self.__left
\t\t
\tdef setLeft(self,n):
\t\tself.__left=n

\tdef getRight(self):
\t\treturn self.__right
\t\t
\tdef setRight(self,n):
\t\tself.__right=n
\t\t
\t\t
\tdef getValue(self):
\t\treturn self.__value
\t\t
\tdef setValue(self,v):
\t\tself.__value = v

\t
\tdef Preorder(self): 
\t\t
\t\tif self.__value != None:
\t\t\troot =self.__value
\t\t\tmyPreorder.append(str(self.__value))
\t\t\t#print("p")
\t\t\t
\t\t\t#print("self.__left",root.getLeft())
\t\t\tif self.getLeft() == None:
\t\t\t\tmyPreorder.append("N")
\t\t\t\t#print("ln")
\t\t\telse:
\t\t\t\tself.getLeft().Preorder()
\t\t\t\t#print("getleft")
\t\t\tif self.getRight() == None:
\t\t\t\tmyPreorder.append("N")
\t\t\telse:
\t\t\t\tself.__right.Preorder()

\tdef Inorder(self): 
\t\t
\t\tif self.__value != None:
\t\t\t
\t\t 
\t\t\tif self.getLeft() == None:
\t\t\t\tmyInorder.append("N")
\t\t\telse:
\t\t\t\tself.getLeft().Inorder()

\t\t\tmyInorder.append(str(self.__value))

\t\t\tif self.getRight() == None:
\t\t\t\tmyInorder.append("N")
\t\t\telse:
\t\t\t\tself.__right.Inorder()
\t\t
\t\t\t#Preorder:
\t\t\t#PLR
\tdef Postorder(self): 
\t\t
\t\tif self.__value != None:
\t\t\t
\t\t 
\t\t\tif self.getLeft() == None:
\t\t\t\tmyPostorder.append("N")
\t\t\telse:
\t\t\t\tself.getLeft().Postorder()

\t\t\tif self.getRight() == None:
\t\t\t\tmyPostorder.append("N")
\t\t\telse:
\t\t\t\tself.__right.Postorder()

\t\t\tmyPostorder.append(str(self.__value))

class BST():
\t
\tdef __init__(self):
\t\tself.__head = None

\tdef __str__(self):
\t\tif self.__head == None:

\t\t\treturn "Empty Tree"

\t\telse:
\t\t\tself.__head.Preorder()
\t\t\tself.__head.Inorder()
\t\t\tself.__head.Postorder()
\t\t\tpreorderPrint= "Preorder: "+' '.join(myPreorder)+" "
\t\t\tinorderPrint= "Inorder: "+' '.join(myInorder)+" "
\t\t\tpostorderPrint= "Postorder: "+' '.join(myPostorder)+" "
\t\t\treturn str(preorderPrint)+'\n'+str(inorderPrint)+'\n'+str(postorderPrint)
\t\t\t

\t\t#self.Preorder(self.__head)
\t\t#Inorder:
\t\t#LPR

\t\t#Postorder:
\t\t#LRP

\t

\t# def Preorder(self,tmp): 
\t#\t tmp=self.__head

\t#\t if tmp.getValue() != None:
\t#\t\t print(tmp.getValue())
\t#\t\t tmp.Preorder(tmp.getLeft())
\t#\t\t #Preorder:
\t#\t\t #PLR
\t\t
\tdef insert(self,value):

\t\tnv= Node(value) # use my Node class
\t\t
\t\tif self.__head == None:
\t\t\tself.__head = nv
\t\t\treturn
\t\t
\t\ttmp = self.__head
\t\t

\t\twhile True:
\t\t\tif value == tmp.getValue():
\t\t\t\treturn False

\t\t\tif value < tmp.getValue():
\t\t\t\t#print("value:",value)
\t\t\t\tif tmp.getLeft() == None:
\t\t\t\t\t#print("nv:",nv)
\t\t\t\t\t#print("tmp setleft:",tmp)
\t\t\t\t\ttmp.setLeft(nv)
\t\t\t\t\t#print("setleft:?",tmp.getLeft())
\t\t\t\t\treturn False
\t\t\t\t\t
\t\t\t\telse:
\t\t\t\t\ttmp = tmp.getLeft()
\t\t\t\t\t#print("getleft:",tmp)

\t\t\telse:
\t\t\t\tif tmp.getRight() == None:
\t\t\t\t\t#print("right is none, now set")   
\t\t\t\t\ttmp.setRight(nv)
\t\t\t\t\t#print("setright:", nv)
\t\t\t\t\treturn False
\t\t\t\telse:
\t\t\t\t\t
\t\t\t\t\ttmp = tmp.getRight()
\t\t\t\t\t#print("get rigth:",tmp)
\t\t\t\t\t
\t\t\t\t\t
\t\t\t\t\t
\tdef find(self,value):
\t\tif self.__head == None:
\t\t\treturn False
\t\t\t
\t\ttmp = self.__head
\t\t
\t\twhile tmp != None:
\t\t\t
\t\t\tif tmp.getValue() == value:
\t\t\t\treturn True
\t\t\t\t
\t\t\telif value < tmp.getValue():
\t\t\t\ttmp= tmp.getLeft()

\t\t\telif value >= tmp.getValue():
\t\t\t\ttmp= tmp.getRight()
\t\treturn False
\t\t
# if __name__ == "__main__":
\t\t

#\t test = [6, 8, 4, 3, 7, 5, 9]
#\t T = BST() 
\t
#\t # for n in test:
#\t #\t print('Inserting: ', n)
#\t #\t T.insert(n)
\t
#\t print(T)

#\t #v = int(float(input('find: ')))

#\t #print(T.find(v))
