class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

def cons(head, tail=None):
    return LinkedList(head, tail)

def listToString(list):
    if list is None:
        return ""
    if list.tail is None:
        return str(list.head)
    return str(list.head) + " " + listToString(list.tail)

def myMap(fn, list):
    if list is None:
        return None
    return cons(fn(list.head), myMap(fn, list.tail))

def myReduce(fn, accm, list):
    if list is None:
        return accm
    return myReduce(fn, fn(accm, list.head), list.tail)

def myReduceRight(fn, accm, list):

    if list is None:
        return accm
    return fn(list.head, myReduceRight(fn, accm, list.tail))

def xTimesTwoPlusY(x, y):
    return x * 2 + y

def printXAndReturnY(x, y):
    print(x)
    return y

def unfoldCaculation(x, y):
    print()

if __name__ == '__main__':
    exampleList = cons(1, cons(2, cons(3, cons(4))))
    result = myReduceRight(xTimesTwoPlusY, 0, exampleList)
    print(result)
    myReduceRight(printXAndReturnY, 0, exampleList)
   