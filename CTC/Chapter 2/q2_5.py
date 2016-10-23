class List:
    val =0
    next = None
    def __init__(self,val):
        self.val = val
        self.next = None

def add_lists(list1 , list2):
    if list1 == None:
        return list2
    if list2 == None:
        return list1

    result = None
    sum = 0
    carry = 0
    curr = list1
    curr2 = list2
    while curr != None and curr2 != None:
        sum = carry + curr.val + curr2.val
        carry = sum/10
        sum = sum%10
        node = List(sum)
        if result == None:
            result = node
        else:
            result.next = node
        curr = curr.next
        curr2 = curr2.next

    while curr != None:
        sum = carry + curr.val
        carry = sum/10
        sum = sum%10
        node = List(sum)
        result.next = node
        curr = curr.next

    while curr2 != None:
        sum = carry + curr2.val
        carry = sum / 10
        sum = sum % 10
        node = List(sum)
        result.next = node
        curr2 = curr2.next

    if carry != 0:
         node = List(carry)
         result.next = node

    return result