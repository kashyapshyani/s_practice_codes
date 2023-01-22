class Solution:
     
    #Function to find if there exists a triplet in the 
    #Aay A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here
        for i in range(0,n):
            for j in range(1,n):
                t1 = A[i]
                t2 = A[j]
                d = X - t1 - t2
                A.pop(i)
                print("j=",j,A)
                A.pop(j)
                if d in A:
                    return True
                else:
                    A.insert(i,t1)
                    A.insert(j,t2)
                    continue


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# import atexit
# import io
# import sys

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register

# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = 5
    # for i in range(t):
    X=10
    n=5
    # n,X=map(int,input().strip().split())
    A=[1,2,4,3,6]
    ob=Solution()
    if(ob.find3Numbers(A,n,X)):
        print(1)
    else:
        print(0)
# } Driver Code Ends