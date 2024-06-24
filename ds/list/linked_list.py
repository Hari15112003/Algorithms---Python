class linkedlist:
    def __init__(self):
        self.data = None
        self.next=None
    
    def insertAtBegining(headPtr , newdata):
        obj = linkedlist()
        obj.data= newdata
        obj.next = headPtr
        headPtr= obj
        return obj
    
    def printNode(node):
        while node!=None:
            print(node.data)
            node=node.next


if __name__ == '__main__':
    head = None
    head = linkedlist.insertAtBegining(head, 22)
    head = linkedlist.insertAtBegining(head, 23)
    head = linkedlist.insertAtBegining(head, 26)
    head = linkedlist.insertAtBegining(head, 29)
    linkedlist.printNode(head)