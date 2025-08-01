class Linked_list:
    def __init__(self, head_node):
        self.head = head_node    # Instance variable
        self.length = 0
    
    # Instance method
    def get_length (self):
        count = 1
        current = self.head
        while current.next!=None:
            current = current.next
            count+=1
        return count

    def __str__(self):
        return f"Linked list(head='{self.head}', length={self.get_length()})"
    
class Node:
    #class variable: shared by all instances

    def __init__(self,value,next):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"value={self.value}, next={self.next}"

lst = ["a","b","c","d","e","f"]

ll = Linked_list(None)
previous = Node(-1,None)
for ind,i in enumerate(lst):
    current_node = Node(i,None)
    if ind == 0:
        ll.head = current_node
    else:
        previous.next = current_node
    previous = current_node

n = ll.get_length()//2
a = ll.head

for _ in range(n-1):
    a = a.next
b = a.next
previous = a
current = a.next
for _ in range(n):
    next = current.next 
    current.next = previous
    previous,current = current,next

a.next = previous
b.next = None

    

print(str(ll))


