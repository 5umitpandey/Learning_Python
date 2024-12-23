#https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1?page=1&difficulty=School,Basic&sortBy=submissions

def printNos(self,n):
        if( n > 0 ):
            self.printNos(n-1)
            print(n, end=" ")
