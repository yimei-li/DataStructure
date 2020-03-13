############################
class TestCycle: 
	def __init__(self,numNodes): 
		self.n= numNodes 
		self.lst = []
		# create a nested list 
		for i in range(numNodes):
			self.lst.append({i})
		
	def insert(self, a, b):
		
		for i in self.lst:
			if a in i:
				if b in i:
					return True
		for i in self.lst:
			for j in self.lst:
				if i != j:
					#print("i: ", i, "j: ",j)
					if a in i:
						#print("a in i", "\na: ",a,"\ni: ",i)
						if b in j:
							#print("b in j", "\nb: ",b,"\nj: ",j)
							self.lst.append(i.union(j))
							self.lst.remove(i)
							self.lst.remove(j)
							return False
							break

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
		if len(self)==0:
			return "empty, no minumum"
		else:
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
		srt=[]
		while len(self.data)>0:			
			if len(self.data)==1:
				srt.append(self.data[0])
				return srt
			if len(self.data)==2:
				if self.data[0]>self.data[1]:
					tmp=self.data[0]
					self.data[0]=self.data[1]
					self.data[1]=tmp
				srt.append(self.data[0])
				srt.append(self.data[1])
				return srt
					
			else:
				self.swap(0,len(self.data)-1)
				srt.append(self.data.pop())		
				self.downheap(0)

################################################
###########################

print("Welcome to Minimum Spanning Tree Finder")


#RED
RawFile=input("Give the file name graph is in:\n")

print("Commands: ")
print("exit or ctrl-d - quits the program")
print("help - prints this menu")
print("prim integer_value - run's Prim's algorithm starting at node given")
print("kruskal - runs Kruskal's algorithm")

#DEL
#RawFile="input1.txt"

with open(RawFile, 'r') as f:
	G = [[float(num) for num in line.split(' ')] for line in f]


numNodes=int(G[0][0])
G.pop(0)





def AdjMatrix(G): # this is to convert G to a Adjaceny Matrix
	
	RM=[]
	
	for i in range(numNodes):
		Rawl=[]
		for i in range(numNodes):
			Rawl.append(float('inf')) # this is to append "inf" to a nested list
		RM.append(Rawl)
	for k in range(len(G)):
		RM[int(G[k][0])][int(G[k][1])]=G[k][2]
	


	return RM



def AdjMatrixSymmetry(G): # this is to convert G to a Adjaceny Matrix
	
	RM=[]
	
	for i in range(numNodes):
		Rawl=[]
		for i in range(numNodes):
			Rawl.append(float('inf')) # this is to append "inf" to a nested list
		RM.append(Rawl)
	for k in range(len(G)):
		RM[int(G[k][0])][int(G[k][1])]=G[k][2]
	
	for i in range(numNodes):
		for j in range(numNodes):
			if RM[i][j] != float('inf'):
				RM[j][i]=RM[i][j]

	return RM



def prim(G,st):
	print("Running Prim's Algorithm")
	print("Starting Node:",st)
	AdjM=AdjMatrixSymmetry(G)
	# for i in AdjM:
	# 	print(i)
	T=set()
	U={st}
	V=set()
	for i in range(numNodes):
		V.add(i)


	
	while len(U)< numNodes:

		findMinWeight=heap()
		findMinWeight.makenull()
		# print("n:\n",n,"\nf:\n",f,"\nAdjM[n][f]\n",AdjM[list(U)[n]][f])
		for v in V.difference(U) : # avoid that we do same path twice
			for u in U:
				findMinWeight.insert(( AdjM[v][u], (u,v)))


		minInAdjN=findMinWeight.min()

		minWeight=minInAdjN[0]
		minu=minInAdjN[1][0]
		minv=minInAdjN[1][1]
		# (u,minIdx)=(u, v) = Lowest cost edge where u in U and v in V − U
		# n is the index of u in U
		T.add((minu,minv,minWeight))
			
		print("Added",minv)
		if minu>minv:
			print("Using Edge",[minv,minu,minWeight])
		else:
			print("Using Edge",[minu,minv,minWeight])
		U.add(minv)


		

	

	return


#	   T := T ∪ {(u, v)}
#	   U := U ∪ {u}

trycyc=[]

#----------------
# function kruskal(Graph G = (E, V))
def kruskal(G):
	AdjM=AdjMatrix(G)
#   Sort Edges
	print("Running Kruskal's Algorithm")

	T=set()
	U=set()# nodes that we have gone through
	V= set()
	for i in range(numNodes):
		V.add(i)

	SortWeight=heap()
	for j in range(numNodes):
		for k in range(numNodes):
			if j>k:
				SortWeight.insert((AdjM[j][k],(k,j)))
			elif j<k:
				SortWeight.insert((AdjM[j][k],(j,k)))
	SortList=SortWeight.sort() # actually you don't need this

	g=TestCycle(numNodes)
	while len(SortList)>0:
	
		minS=SortList[0]
		na=minS[1][0]
		nb=minS[1][1]
		
		if na>=nb:
			w=na
			na=nb
			nb=w

		VMU=V.difference(U)
		
		test=g.insert(na,nb)
		
		if test==True:
			g=TestCycle(numNodes)
			for i in trycyc:
				a=int(i[1][0])
				b=int(i[1][1])
				g.insert(a,b)
			#print("cyclic","SortList: ",SortList)
			SortList.pop(0)
		else:
			#print("Not cyclic","MySortList: ",SortList)
			print("Select Edge: "+"["+str(int(na))+", "+str(int(nb))+", "+str(float(minS[0]))+"]")
			T.add(minS)
			U.add(minS[1][0])
			U.add(minS[1][1])
			trycyc.append(SortList.pop(0))
	return
		
		
				
		
		
		







#   T = Empty Set
#   for each node n in V do
#	   Create a Set Containing {n}
#   end for
#   for each edge (x,y) in order do
#	   if Find-Set(x) != Find-Set(y) then
#		   T = T ∪ {(x, y)}
#		   Union(Find-Set(x),Find-Set(y))
#	   end if
#   end for
#   return A
# end function




# RED
x=1
while x==1:
	cmd=str(input("Enter command:\n"))
	startWithDi=cmd.startswith("prim")
	if cmd == "help":
		print("Commands: ")
		print("exit or ctrl-d - quits the program")
		print("help - prints this menu")
		print("prim integer_value - run's Prim's algorithm starting at node given")
		print("kruskal - runs Kruskal's algorithm")
	
	elif startWithDi== True:
		NumL = [int(i) for i in cmd.split() if i.isdigit()] 
		Num=int(NumL[0])
		prim(G,Num)
	 

	 # [[0, 1, 1], [1, 2, 2], [2, 3, 2], [2, 4, 4], [3, 1, 1], [3, 2, 3], [4, 3, 5]]
	elif cmd == "kruskal":
 
		kruskal(G)
		

	elif cmd == "exit":
		print("Bye")
		x=0
	

	else:
		print("Unknown Command")
