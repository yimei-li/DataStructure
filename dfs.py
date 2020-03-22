
cycle=0        
#RED
RawFile=input("Give the test file name :\n")


with open(RawFile, 'r') as f:
	G = [[float(num) for num in line.split(' ')] for line in f]

numNodes=int(G[0][0])
G.pop(0)
#[[0.0, 1.0], [1.0, 2.0], [2.0, 3.0], [2.0, 4.0], [4.0, 1.0], [0.0, 4.0]]
adj=[]
for i in range(numNodes):   
    adj.append([])
for i in G:
    k=i[0]
    k1=i[1]
    m=0
    while m<numNodes:
        if m==k:
            adj[m].append(k1)
        m=m+1



V=[]

class NColor:
    def __init__(self,num):
        self.__color = None
        self.__found = None
        self.__finished= None
        self.__number = num
    def __str__(self):
        return str(self.__number)
    def color(self,color):
        self.__color=color
    def getColor(self):
        return self.__color

    def found(self,foundTime):
        self.__found = foundTime
    def getFound(self):
        return self.__found

    def finished(self,finishedTime):
        self.__finished=finishedTime

    def getFinished(self):
        return self.__finished
    def getU(self):
        return self.__number



time=0

for i in range(numNodes):
    V.append(i)

VA=[]
for u in V:
    VA.append(NColor(u))


def dfsVisit(adj,u): # u is an object in VA
    global time
    time +=1

    u.found(time)

    u.color("gray")


    for vn in adj[u.getU()]:

        for k in VA:
            if k.getU()==vn:# find the neighber node vn
                if k.getColor() == "white":
                    
                    dfsVisit(adj,k)
                elif k.getColor() == "gray":
                    global cycle
                    cycle=1
                    return True

    u.color("black")
    
    time +=1
    u.finished(time)

    return


def DFS(adj):
    for u in VA:
        u.color("white")
    for u in VA:
 
        if u.getColor() == "white":

            dfsVisit(adj,u)# u is an object in VA
    if cycle == 1:
        return True
    
# you can also call DFS and return true of fal

if DFS(adj)==True:
    print("True")
else:
    print("False")





