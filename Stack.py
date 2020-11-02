from SinglyLinkedList import Node 
from SinglyLinkedList import LinkedList 

class Stack:
    '''
    Inherits from the LinkedList class. 
    '''

    def __init__(self):
        LinkedList.__init__(self)
    
    def __len__(self):
        return LinkedList.__len__(self)
    
    def _isEmpty(self):
        return LinkedList._isEmpty(self)    
    
    def push(self, item):
        return LinkedList.addFirst(self, item)
    
    def pop(self): 
        '''
        Removes the top item and returns it
        '''
        last = self.tail.data
        LinkedList.removeFirst(self)
        return last
    
    def peek(self):
        return LinkedList.peekFirst(self) 
    
    def search(self, item): 
        return LinkedList.search(self, item) 
    
    def __str__(self):
        '''
        prints the values at each node of the list within set brackets
        and puts arrow (<--) between the values at each node
        '''
        if self._isEmpty():
            return 'Empty Stack'
        elif self.size == 1:
            return '{' + str(self.head.data) + '}'
        else:
            trav = self.head
            res = str(trav.data)

            while not trav.next == None:
                res += ' <-- {}'.format(trav.next.data)
                trav = trav.next

            return '{' + res + '}'    


if __name__ == '__main__':

    print('\n\n\nTesting initialization of the Stack')
    print('-------------------------------------------')
    try:
        stack = Stack()
        print('Success')
    except:
        print('There is a problem with the initialization of the Stack')

    print('\n\n\nTesting push')
    print('-------------------------------------------')

    for item in (-1, 's', [1, 2]):
        print('Before pushing {}, the stack is {}'.format(item, stack))
        print('Its size is {}'.format(len(stack)))
        print('Is it Empty?: {}'.format(stack._isEmpty()))
        stack.push(item)
        print('After pushing {}, the stack is {}'.format(item, stack))
        print('---------\n')
    
    print('\n\n\nTesting peek and pop')
    print('-------------------------------------------')

    for item in (-1, 's', [1, 2]):
        print('Peeking the top item in the stack {} is {}'.format(stack, stack.peek()))
        print('Poped item is {}'.format(stack.pop()))
        print('After popping, the stack is {}'.format(stack))
        print('---------\n')
    
    print('\n\n\nTesting search')
    print('-------------------------------------------')
    print('When stack is empty.')
    stack = Stack()
    print('Searching 34 in the stack {}'.format(stack))
    try:
        print(stack.search(34))
    except ValueError:
        print('Successful ValueError')
    except:
        print('THERE IS A PROBLEM WITH SEARCH in EMPTY STACK')
    print('---------\n')
    print('When stack is NOT empty.')
    for item in (-1, 's', [1, 2]):
        stack.push(item)
    
    for item in ('s', 34, -1, [1,2]):
        print('Searching {} in the stack {}'.format(item, stack))
        try:
            print(stack.search(item))
        except IndexError:
            print('Successful IndexError')
        except:
            print('THERE IS A PROBLEM WITH SEARCH in EMPTY STACK')
        print('---------\n')
    


