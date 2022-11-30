#User function Template for python3

#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        if head.next is not None and head.next.next is not None:
            dct = {}
            i=0
            head_tmp = head
            while(head_tmp.next is not None):
                dct[i]=head_tmp
                i += 1
                head_tmp=head_tmp.next
            
            dct[i]=head_tmp
            head_tmp = head
            n = i
            
            i = 1
            left=1
            right=n
            while(i<=n):
                if i%2==1:
                    head_tmp.next=dct[right]
                    right-=1
                    i+=1
                else:
                    head_tmp.next=dct[left]
                    left+=1
                    i+=1
                head_tmp=head_tmp.next
            head_tmp.next=None
        
        
            
        
        
        
            
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends