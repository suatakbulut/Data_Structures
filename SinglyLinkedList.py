class Node:
    '''
    A Node Class is used to create the nodes of a linked list
    
    Attributes:
        data (ANY TYPE) : the value at a node 
        next (Node) : the next node
    '''
    def __init__(self, data=None, nextt=None):
        self.data = data
        self.next = nextt

    def __str__(self):
        return str(self.data) + ' --> {' + str(self.next) + '}'


class LinkedList:
    '''
    A Singly Linked List Data Structure
    
    Attributes:
        size (INT)  : the length (number of nodes) of the list
        head (Node) : the first node of the list
        tail (Node) : the last node of the list
    '''

    def __init__(self):
        self.size = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)

    def __len__(self):
        '''
        Returns the size of the list (INT)
        '''
        return self.size

    def __str__(self):
        '''
        prints the values at each node of the list within set brackets
        and puts arrow (-->) between the values at each node
        '''
        if self._isEmpty():
            return 'Empty Linked List'
        elif self.size == 1:
            return '{' + str(self.head.data) + '}'
        else:
            trav = self.head
            res = str(trav.data)

            while not trav.next == None:
                res += ' --> {}'.format(trav.next.data)
                trav = trav.next

            return '{' + res + '}'

    def _isEmpty(self):
        '''
        Checks if the list is empty and Returns BOOLEAN value
        '''
        return self.size == 0

    def addFirst(self, item):
        '''
        adds a new node at the beginning of th elist that has item as its value

        Parameters
        ----------
        item : (ANY TYPE)
            The value to be inserted in the new node

        Returns
        -------
        None.

        '''
        node = Node(item)
        if self._isEmpty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def addLast(self, item):
        '''
        adds a new node at the end of the list that has item as its value

        Parameters
        ----------
        item : (ANY TYPE)
            The value to be inserted in the new node

        Returns
        -------
        None.

        '''
        if self._isEmpty():
            self.addFirst(item)
        else:
            node = Node(item)
            self.tail.next = node
            self.tail = node
            self.size += 1

    def add(self, item):
        '''
        adds a new node at the end of th elist that has item as its value

        Parameters
        ----------
        item : (ANY TYPE)
            The value to be inserted in the new node

        Returns
        -------
        None.

        '''
        return self.addLast(item)

    def peekFirst(self):
        '''
        Checks the value at the first node of the list and returns it
        '''
        if self._isEmpty():
            print('Link is empty')
        else:
            return self.head.data

    def peekLast(self):
        '''
        Checks the value at the last node of the list and returns it
        '''
        if self._isEmpty():
            print('Link is empty')
        else:
            return self.tail.data

    def removeFirst(self):
        '''
        Removes the beginning node of the list

        Raises
        ------
        ValueError
            if the list is empty

        Returns
        -------
        None.

        '''
        if self._isEmpty():
            raise ValueError('Empty Linked List')

        elif self.size == 1:
            self.head = Node(None, None)
            self.tail = Node(None, None)
            self.size = 0

        else:
            trav = self.head.next
            self.head = trav
            self.size -= 1

    def removeLast(self):
        '''
        Removes the end node of the list

        Raises
        ------
        ValueError
            if the list is empty

        Returns
        -------
        None.

        '''
        if self._isEmpty():
            raise ValueError('Empty Linked List')

        else:
            trav = self.head

            if self.size == 1:
                self.head = Node(None, None)
                self.tail = Node(None, None)
            else:

                while trav != self.tail:
                    last_trav = trav
                    trav = trav.next

                last_trav.next = None
                self.tail = last_trav
            self.size -= 1

    def search(self, item):
        '''
        Searches the item in the nodes of the list, and returns the node 
        has the item

        Parameters
        ----------
        item : ANY TYPE
            value to be searched in the nodes of the list

        Raises
        ------
        ValueError
            if the list is empty
        IndexError
            if the item is not a value in the nodes of the list

        Returns
        -------
        Node
            The first node in the list that has the item as its value

        '''
        if self._isEmpty():
            raise ValueError('Empty Linked List')

        elif self.head.data == item:
            return self.head

        else:
            trav = self.head
            while trav != self.tail:
                if trav.data == item:
                    return trav
                else:
                    trav = trav.next
            if self.tail.data == item:
                return self.tail
            else:
                raise IndexError('{} is not in the linked list'.format(item))

    def remove(self, item):
        '''
        Removes the first node that has the item as its value 

        Parameters
        ----------
        item : ANY TYPE
            value to be removed

        Raises
        ------
        ValueError
            if the list is empty
        IndexError
            if the item is not a value in the nodes of the list

        Returns
        -------
        LinkedList
            The same linked list after removing the first node with the item in it

        '''
        if self._isEmpty():
            raise ValueError('Empty Linked List')

        elif self.head.data == item:
            self.removeFirst()
            return self

        elif self.size == 1:
            raise IndexError('{} is not in the linked list'.format(item))
        else:
            trav_previous = self.head
            trav = self.head.next

            while trav != self.tail:
                if trav.data == item:
                    trav_previous.next = trav.next
                    self.size -= 1
                    return self
                else:
                    trav_previous = trav
                    trav = trav.next

            if trav.data == item:
                self.removeLast()
            else:
                raise IndexError('{} is not in the linked list'.format(item))
            return self


if __name__ == '__main__':

    print('\n\n\nTesting initialization of the Linked List')
    print('-------------------------------------------')
    try:
        link = LinkedList()
        print('Success')
    except:
        print('There is a problem with the initialization of the Linked List')

    print('\n\n\nTesting addFirst, addLast, and add()')
    print('-------------------------------------------')
    link = LinkedList()
    for item in (-1, 's', [1, 2]):
        print('Before addingFirst {}, the linked list is {}'.format(item, link))
        link.addFirst(item)
        print('After addingFirst {}, the linked list is {}'.format(item, link))
        print('---------\n')

    print('-------------------------------------------')
    link = LinkedList()
    for item in (-1, 's', [1, 2]):
        print('Before addLast {}, the linked list is {}'.format(item, link))
        link.addLast(item)
        print('After addLast {}, the linked list is {}'.format(item, link))
        print('---------\n')

    print('-------------------------------------------')
    link = LinkedList()
    for item in (-1, 's', [1, 2]):
        print('Before add {}, the linked list is {}'.format(item, link))
        link.add(item)
        print('After add {}, the linked list is {}'.format(item, link))
        print('---------\n')

    print('\n\n\nTesting peekFirst and peekLast')
    print('-------------------------------------------')
    print('The linked list is {}'.format(link))
    print('The first data in the linked list is {}'.format(link.peekFirst()))
    print('The last data in the linked list is {}'.format(link.peekLast()))
    link = LinkedList()
    print('-------------------------------------------')
    print('The linked list is {}'.format(link))
    print('The first data in the linked list is {}'.format(link.peekFirst()))
    print('The last data in the linked list is {}'.format(link.peekLast()))

    print('\n\n\nTesting removeFirst() and removeLast()')
    print('-------------------------------------------')
    link_first = LinkedList()
    link_last = LinkedList()
    print('When linked list is empty.')
    print('--------------------------')
    print('\nThe first linked list is {}'.format(link_first))
    try:
        print('After removeFirst() applied, the first linked list is :{}'.format(link_first.removeFirst()))
    except ValueError:
        print('The code successfully raised a Value Error')
    else:
        print('FAILED TO RAISED ERROR MESSAGE')

    print('\nThe second linked list is {}'.format(link_last))
    try:
        print('After removeLast() applied, the second linked list is: {}'.format(link_last.removeLast()))
    except ValueError:
        print('The code successfully raised a Value Error')
    else:
        print('FAILED TO RAISED ERROR MESSAGE')

    link_first = LinkedList()
    link_last = LinkedList()
    for item in ('suat', ['a', 2], 51):
        link_first.add(item)
        link_last.add(item)
    print('\n-------------------------------------------')
    print('When linked list is NOT empty.')
    print('------------------------------\n')
    for iter in range(3):
        print('The first linked list is {}'.format(link_first))
        print('After removeFirst() applied, the first linked list is {}'.format(link_first.removeFirst()))
        print('The second linked list is {}'.format(link_last))
        print('After removeLast() applied, the second linked list is {}'.format(link_last.removeLast()))
        print('----------------------------------------')

    print('\n\n\nTesting search()')
    print('-------------------------------------------')
    link = LinkedList()
    print('When linked list is empty.')
    print('--------------------------')
    try:
        print('Searching the value 1 in the empty linked list results in {}'.format(link.search(1)))
    except ValueError:
        print('The code successfully raised a Value Error')
    else:
        print('FAILED TO RAISED ERROR MESSAGE')

    for item in ('suat', ['a', 2], 51):
        link.add(item)

    print('\n-------------------------------------------')
    print('When linked list is NOT empty.')
    print('------------------------------\n')
    for item in ('suat', ['a', 2], 51):
        try:
            print('Searching "{}" in the empty linked list results in {}'.format(item, link.search(item)))
        except:
            error_message = '!!! ERROR in searching {} in the list !!!'.format(item)
            print('\n' + len(error_message) * '-')
            print(error_message)
            print(len(error_message) * '-' + '\n')
    try:
        print('Searching the value 34 in the empty linked list results in {}'.format(link.search(34)))
    except IndexError:
        print('Searching the value 34 in the empty linked list successfully raised an IndexError')
    else:
        print('Searching the value 34 in the empty linked list failed to raise an IndexError')

    print('\n\n\nTesting remove()')
    print('-------------------------------------------')
    print('When linked list is empty.')
    print('--------------------------')
    link = LinkedList()
    try:
        print('Removing "suat" from the empty linked list results in {}'.format(link.remove('suat')))
    except ValueError:
        print('The code successfully raised a Value Error')
    else:
        print('FAILED TO RAISED ERROR MESSAGE')

    for item in ('suat', ['a', 2], 5, 51):
        link.add(item)

    print('\n-------------------------------------------')
    print('When linked list is NOT empty.')
    print('------------------------------\n')
    for item in (5, ['a', 2], 45, 51, 'suat'):
        print('\nOur linked list, before removing {} is {}'.format(item, link))
        try:
            print('Removing {} results in {}'.format(item, link.remove(item)))
        except IndexError:
            print('INDEX ERROR IS RAISED'.format(item, link))
        except:
            print('!!! THERE IS A PROBLEM WITH REMOVE() !!!')
