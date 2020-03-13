#################################################
myInorder=[]
myPreorder=[]
myPostorder=[]
sortlist=[]
import math
class heap:
	def __init__(self):
		self.data = []
		self.count=0

	def __str__(self):
		res=""
		for x in self.data:
			res=res+str(x)+" "
		return res
	
	def __len__(self):
		return len(self.data)

	def makenull(self):
	# should i still use return or not?
		self.data=[]

	def insert(self,x):

		self.data.append(x)
		self.upheap(len(self.data)-1)


	def parent(self,index):
		parentIdx=(index-1)//2
		return parentIdx

	def left(self,index):
		leftIdx= (index+1)*2-1
		return leftIdx
	def right(self,index):
		rightIdx= (index+1)*2
		return rightIdx

	def swap(self,a,b):
		tmp = self.data[a]
		self.data[a]=self.data[b]
		self.data[b]=tmp

	def upheap(self,index):
		parentIndex=self.parent(index)
		if parentIndex < 0:
			return
		p=self.data[parentIndex]
		c=self.data[index]
		if p > c :
			self.swap(index,parentIndex)
			self.upheap(self.parent(index))
			
	def inorder(self,index):

		if index < len(self.data):
			self.inorder(self.left(index))
			print(str(self.data[index])+" ",end='')
			self.inorder(self.right(index))
		return ''


			

	def preorder(self,index):


		if index < len(self.data):
			
			print(str(self.data[index])+" ",end='')

			self.preorder(self.left(index))

			self.preorder(self.right(index))
		return ''


	def postorder(self,index):

		if index < len(self.data):
	
			self.postorder(self.left(index))
			self.postorder(self.right(index))
			print(str(self.data[index])+" ",end='')
		return ''

	def min(self):
		return self.data[0]
	
	def deletemin(self):
		if len(self.data) == 0:
			return "empty, can not delete"
		self.swap(0, len(self.data)-1)
		self.data.pop()
		self.downheap(0) # downheap from the first one

	def findNumC(self,index):
		if self.left(index)< len(self.data) and (self.right(index)< len(self.data)):
			return 2
		elif self.left(index)> (len(self.data)-1) and  (self.right(index) > (len(self.data)-1)):
			return 0
		else:
			return 1
	
		

	def downheap(self,index): 
		v= self.findNumC(index)

		if v == 2:
			if self.data[index]<= self.data[self.left(index)] and self.data[index]<= self.data[self.right(index)]:
				return ''
			if self.data[self.left(index)]<= self.data[self.right(index)]:
				self.swap(index, self.left(index))
				self.downheap(self.left(index))
			else:
				self.swap(index, self.right(index))
				self.downheap(self.right(index))
		elif v==1:
			self.swap(index, self.left(index))
			self.downheap(self.left(index))
		else:
			return ''

	def sort(self):
			
		while len(self.data)>0:			
			if len(self.data)==1:
				print(self.data[0])
				return 
			if len(self.data)==2:
				if self.data[0]>self.data[1]:
					tmp=self.data[0]
					self.data[0]=self.data[1]
					self.data[1]=tmp
				print(self.data[0])
				print(self.data[1])
				return 
					
			else:
				self.swap(0,len(self.data)-1)
				print(self.data.pop())		
				self.downheap(0)

################################################

RawFile=input("File containing graph:\n")




print("Possible Commands are: ")
print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
print("floyd - Runs Floyd's algorithm")
print("help - prints this menu")
print("exit or ctrl-D - Exits the program")





with open(RawFile, 'r') as f:
	G = [[int(num) for num in line.split(' ')] for line in f]
# Gf is the number of nodes in a graph
Gf = G[0][0]

G.pop(0)

# [[0, 1, 1], [1, 2, 2], [2, 3, 2], [2, 4, 4], [3, 1, 1], [3, 2, 3], [4, 3, 5]]



def ll(self):
	Rawl=[]
	for i in range(self):
		Rawl.append(float('inf'))
	return Rawl

# create a raw matrix by using the input file. 
# This matrix shows the distance, but not the shortest.
# This is "adjacency Matrix"
def RawMatrix(self): # self is G
	RM=[]
	for i in range(Gf):
		RM.append(ll(Gf))

	for k in range(len(self)):
		RM[self[k][0]][self[k][1]]=self[k][2]
	
	return RM



def dijkstra(self, sn): # sn is the staring nodes
	self=RawMatrix(G) # "self" is the adjacent matirx
	D=[]
	for i in range(Gf):
		D.append(float('inf'))
	# D is a list now, [inf, inf, inf, inf, inf]

	D[sn]=0 # because start node to start node is 0
	H=heap()
	H.insert(0)
	

	while len(H) !=0:
		uValue=H.min()  # here we didn't do insert or sort or upheap
		# u's value is the minimum of H, which is always H[0], but we need to return the index of the value in D, that index is u.
		for i in D:
			if i == uValue:
				u = D.index(uValue) # now u is the index of the minimum number in D
				break
		# for each node v (value of RawMatrix row u) adjacent to u 
		for value in self[u]:
			if value != float('inf'): # this is to make sure that v is adjacent to u
				valueIndex=self[u].index(value)
				if D[valueIndex]>D[u]+self[u][valueIndex]:
					D[valueIndex]=D[u]+self[u][valueIndex]
					H.insert(D[valueIndex])
					

		H.deletemin()

	Ans=[float(i) for i in D]
	return Ans

   
 
def floyd(self): # sn is the staring nodes
	self=RawMatrix(G)
	print(self)
	for i in range(Gf):
		for j in range(Gf):
			if self[i][j]!=float('inf') and self[j][i]!=float('inf'):
			
				if i==j:
					self[i][j]=0
				for l in range(Gf):
					if self[i][l]!=float('inf') and self[l][j]!=float('inf'):
				  
					
						if self[i][j]> self[i][l]+self[l][j]:
					
							self[i][j] = self[i][l]+self[l][j]



	return


# input1.txt
x=1
while x==1:
	cmd=input("Enter command:\n")
	if cmd == "help":
		print("Possible Commands are: ")
		print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
		print("floyd - Runs Floyd's algorithm")
		print("help - prints this menu")
		print("exit or ctrl-D - Exits the program")
		
	startWithDi=cmd.startswith("dijkstra")
	if startWithDi== True:
		NumL = [int(i) for i in cmd.split() if i.isdigit()] 
		Num=int(NumL[0])
		# Get dijkstra Num

		print(dijkstra(G,Num))
	 

	# [[0, 1, 1], [1, 2, 2], [2, 3, 2], [2, 4, 4], [3, 1, 1], [3, 2, 3], [4, 3, 5]]
	if cmd == "floyd":
 
		for i in floyd(G):
			print(i)

	if cmd == "exit":
		print("Bye")
		x=0

