class Solution:
    def segregate(self, head):
        l=[]
        temp=head 
        while temp:
            l.append(temp.data)
            temp=temp.next 
        l.sort()
        node = Node(l[0])
        temp=node 
        for i in range(1,len(l)):
            new_node=Node(l[i])
            temp.next=new_node 
            temp=new_node 
        return node
