class Node:
    def __init__(self, ID, name, score):
        self.ID = ID
        self.name = name
        self.score = score
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertSortedById(self, ID, name, score):
        new_node = Node(ID, name, score)
        if not self.head or self.head.ID > ID:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        while curr.next and curr.next.ID < ID:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def displayById(self):
        curr = self.head
        while curr:
            print(curr.ID, curr.name, curr.score)
            curr = curr.next

    def displayByScore(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(Node(curr.ID, curr.name, curr.score))
            curr = curr.next

        for i in range(len(nodes)):
            for j in range(0, len(nodes)-i-1):
                if nodes[j].score > nodes[j+1].score:
                    nodes[j], nodes[j+1] = nodes[j+1], nodes[j]

        for node in nodes:
            print(node.ID, node.name, node.score)

    def update(self, ID, name, score):
        curr = self.head
        while curr:
            if curr.ID == ID:
                curr.score += score
                return
            curr = curr.next

        self.insertSortedById(ID, name, score)

def readFileAndInsertToList(filename, linkedList):
    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            ID = int(parts[0])
            name = ' '.join(parts[1:-1])
            score = int(parts[-1])
            linkedList.insertSortedById(ID, name, score)

def readFileAndUpdateList(filename, linkedList):
    with open(filename, 'r') as f:
        for line in f:
            parts = line.split()
            ID = int(parts[0])
            name = ' '.join(parts[1:-1])
            score = int(parts[-1])
            linkedList.update(ID, name, score)


linkedList = LinkedList()

readFileAndInsertToList('data1.dat', linkedList)

readFileAndUpdateList('data2.dat', linkedList)

print("Show Case 1")
linkedList.displayById()

print("\nShow Case 2")
linkedList.displayByScore()
