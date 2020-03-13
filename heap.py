#Mark Boady
#CS 260 - Complete Implementation
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
	
	# def printMe(self):
	# 	if len(self.data)== 0:
	# 		return "Empty"

	# 	else:

	# 		#preorderPrint= "Preorder: "+' '.join(myPreorder)+" "
	# 		inorderPrint= "Inorder: "+' '.join(myInorder)+" "
	# 		#postorderPrint= "Postorder: "+' '.join(myPostorder)+" "
	# 		return str(inorderPrint)#+'\n'+str(postorderPrint)+'\n'+str(preorderPrint)
	
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

#• The left child of the node at index n is at (n + 1) ∗ 2 − 1
#• The right child of the node at index n is at index (n + 1) ∗ 2
		
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
			#if self.left(index) < len(self.data):
			
			#print(str(self.data[index])+" ",end='')
			#if self.right(index) < len(self.data):
			
			# return self.inorder(self.left(index))+' '+str(self.data[index])+' '+self.inorder(self.right(index))

			#return str(self.inorder(self.left(index)))+' '+str(self.data[index])+' '+ str(self.inorder(self.right(index)))``
			
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
		# if self.left(index)< len(self.data) and self.right(index) > (len(self.data)-1):
		# 	return 1
		# if self.left(index)> (len(self.data)-1):
		# 	if self.right(index) < len(self.data):
		# 		return 1
		

	def downheap(self,index): 

		# if self.left(index)> len(self.data)-1 and self.right(index)> len(self.data)-1:
		# 	return

		# elif self.left(index)> len(self.data)-1 and self.right(index)< len(self.data):
    	# 	if self.data[index]<self.data[self.right(index)]:

		#  	self.swap(index, self.right(index))
		#  	self.downheap(self.right(index)) 	
		# elif self.left(index)< len(self.data) and self.right(index)< len(self.data):
		# 	self.swap(index, self.right(index))
		# 	self.downheap(self.right(index))

		# while (index * 2) + 2 < len(self.data)-1:
		# 	if self.left(index) is not None or self.right(index) is not None:
		# 		if self.data[self.left(index)] < self.data[self.right(index)]:
		# 			temp = self.left(index)
		# 		else:
		# 			temp = self.right(index)
		# 	if self.data[index] > self.data[temp]:
		# 		self.swap(temp, index)
		# 	index = temp

		
		#-----------
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


	# def sort(self):
		
	# 	while len(self.data)>0:			
	# 		if len(self.data)==1:
	# 			sortlist.append(self.data[0])
	# 			return sortlist
	# 		if len(self.data)==2:
	# 			if self.data[0]>self.data[1]:
	# 				tmp=self.data[0]
	# 				self.data[0]=self.data[1]
	# 				self.data[1]=tmp
	# 			sortlist.append(self.data[0])
	# 			sortlist.append(self.data[1])
	# 			return sortlist
					
	# 		else:
	# 			self.swap(0,len(self.data)-1)
	# 			sortlist.append(self.data.pop())			
	# 			self.downheap(self.data[0])
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


if __name__ == '__main__':
	test = [99,88,93,19,65,46,55,6,89,76,14,94,2,100,67,87,35,93,50,97 ]

	print("mytest: ", test )
	T = heap()
	for n in test:
		T.insert(n)
	print(T)
	print(T.sort())