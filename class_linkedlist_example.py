class Student(object):
    #无论是创建类的构造方法还是实例方法，最少要包含一个参数self。
    def __init__(self, name, age, gender, level, grades=None): #初始参数
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}
    def setGrade(self, course, grade):
        self.grades[course] = grade
    def getGrade(self, course):
        return self.grades[course]
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
'''
前缀带self的变量，就是在整个类的代码块里面类似是作为全局变量，
如果变量前面加了self，那么在任何实例方法（非staticmethod和calssmethod）就都可以访问这个变量了，
如果没有加self，只有在当前函数内部才能访问这个变量。
'''

john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})
john.setGrade("english", 3.5)

print(john.getGrade("english"))
print(jane.getGPA())

#节点类
class Node:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo #存放节点的value
        self.next = next #存放指针
    def __str__(self):
        return str(self.cargo)
print(Node("text"))

'''
节点：每个节点有两个部分，左边部分称为值域，用来存放用户数据；右边部分称为指针域，用来存放指向下一个元素的指针。
head:head节点永远指向第一个节点
tail: tail永远指向最后一个节点
None:链表中最后一个节点的指针域为None值
'''

#如何定义链表?
#可以先定义节点
node1 = Node(1) #cargo=1
node2 = Node(2) #cargo=2
node3 = Node(3) #cargo=3

node1.next = node2
node2.next = node3

#打印整个链表
def printList(node):
    while node:
        print(node)
        node = node.next

printList(node1)

#使用递归(recursion)的方法打印
def printBackward(lists):
    if lists == None:
        return 
    head = lists
    tail = lists.next
    printBackward(tail) #这一行没有print
    print(head)

printBackward(node1)

#更简便
def printBackward(lists):
    if lists == None:return
    printBackward(lists.next)
    print(lists)
printBackward(node1)

#链表的基本操作
#计算链表长度
class Node:
    #功能：输入一个值data，将值变为一个节点
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    def __len__(self):
        #输入头节点，返回链表长度
        curr = self.head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next
        return counter
    def __str__(self):
        res = ""
        ptr = self.head
        while ptr:
            res += f"{ptr.data}" + ", "
            ptr = ptr.next
        res = res.strip(", ")
        if len(res):
            return "[" + res +"]"
        else:
            return "[]"

    def insertToFront(self, data):
        #输入data插入到头节点前，并更改为头节点
        #时间复杂度和空间复杂度均为O(1)
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node
    def append(self, data):
        #输入data，作为节点插入到末尾
        #时间复杂度O(n)，空间O(1)
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = node
        return node
    def find(self, data):
        #查找输入的data所在节点
        #可见时间复杂度为O(n),空间复杂度为O(1)
        if data:
            return None
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None
    def delete (self, data):
        #删除节点
        if data:
            return None
        if self.head:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node:
            if curr_node.data == data:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next
            
if __name__ == '__main__':

    node1 = Node(3, node2)
    node2 = Node(5, node3)
    node3 = Node(7, None)

    lists = LinkedList(node1)
    lists.append(10)

    print(f'The list exmaple is {lists}, length is {len(lists)}')

#我们只是使用self代指调用方法的对象，完成对象和实例方法的第一个参数进行绑定，
#至于实例方法的第一个参数写成a,b,c.....或者this完全不受影响。
#当然，最好还是尊重约定俗成的习惯，使用self。