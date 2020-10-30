# Create Dynamic Array

import ctypes


class DynamicArray:
    '''
    A Dynamic Array Data Structure

    Attributes:
        n (INT) : number of elements in the arra (length)
        capacity (INT) : the length of the actual array
        A (LIST) : the items of the array
    '''

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def make_array(self, capacity):
        '''
        Creates a static array of size capacity

        Parameters
        ----------
        capacity : INT
            The size of the array to be created

        Returns
        -------
        LIST
            A list as a container to store the items in our
            dynmic array

        '''
        return (capacity * ctypes.py_object)()

    def __len__(self):
        '''
        Returns the size of the array (INT)

        '''
        return self.n

    def __getitem__(self, k):
        '''
        Returns the element at the kth index

        Parameters
        ----------
        k : INT
            Index

        Returns
        -------
        Anyting
            The item sitting at the kth index of our array

        '''
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')

        return self.A[k]

    def _double(self):
        '''
        Doubles the capacity of our array
        '''
        new_cap = 2 * (self.capacity)
        new_arr = self.make_array(new_cap)

        for k in range(self.n):
            new_arr[k] = self.A[k]
        self.A = new_arr
        self.capacity = new_cap

    def _shrink(self):
        '''
        Shrinks the capacity of our array to half
        '''
        new_cap = (self.capacity) // 2
        new_arr = self.make_array(new_cap)

        for k in range(self.n):
            new_arr[k] = self.A[k]
        self.A = new_arr
        self.capacity = new_cap

    def append(self, item):
        '''
        Adds item to the end of our array

        Parameters
        ----------
        item : Anything
            the items to be pushed to the array

        Returns
        -------
        None.

        '''
        if self.n == self.capacity:
            self._double()

        self.A[self.n] = item
        self.n += 1

    def insertAt(self, ind, elt):
        '''
        Inserts an item at a specified index of the array
        and shifts the items to the right

        Parameters
        ----------
        ind : INT
            Index of the array
        elt : Anything
            the item to be inserted

        Returns
        -------
        LIST
            Our array with a new item at index ind

        '''
        if ind < 0 or ind > self.n:
            return IndexError('Index is out of bound')

        if self.capacity == self.n:
            self._double()

        for i in range(self.n - 1, ind - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[ind] = elt
        self.n += 1

    def _removeAt(self, ind):
        '''
        Removes the item at a specified index

        Parameters
        ----------
        ind : INT
            The index of the item to be removed

        Returns
        -------
        LIST
            returns the array with one less item

        '''

        if self.n == 0:
            print('Array is empty.')
            return self

        if ind >= self.n or ind < 0:
            return IndexError('Index out of bound')

        if ind == self.n - 1:
            self.n -= 1
            self.A[ind] = None

        else:
            for i in range(ind, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.A[self.n - 1] = None
            self.n -= 1

    def pop(self):
        '''
        Deletes the last item in the array and
        returns the array with one less item back

        '''
        if self.n == 0:
            print('Array is empty.')
            return self

        if self.n == (self.capacity) // 2:
            self._shrink()

        last = self.A[self.n - 1]
        self._removeAt(self.n - 1)
        return last

    def delete(self, item):
        '''
        Removes a specified item from the list and
        returns the array with one less item
        '''
        if self.n == 0:
            print('Array is empty.')
            return self

        if self.n == (self.capacity) // 2:
            self._shrink()

        for ind in range(self.n - 1):
            if self.A[ind] == item:
                return self._removeAt(ind)

        print('The item is not in the list')
        return self

    def __str__(self):
        '''
        prints the array within set brackets
        and puts comma between the items of the array
        '''
        if self.n == 0:
            return '[]'
        else:
            res = str(self.A[0])
        for i in range(1, self.n):
            res += ', {}'.format(self.A[i])

        return '[' + res + ']'


if __name__ == '__main__':

    print('\nTesting initialization of the Dynmaic Array')
    print('-------------------------------------------')
    try:
        arr = DynamicArray()
        print(arr)
        print('Success')
    except:
        print('There is a problem with the initialization of the Dynamic Array')

    print('\nTesting append')
    print('-------------------------------------------')
    print('Before test, array is {}'.format(arr))

    length = 9
    try:
        for i in range(length):
            arr.append(i)
            print('after appending {}, array is {}'.format(i, arr))
        print('Success')
    except:
        print('There is a problem with append()')

    print('\nTesting arr')
    print('-------------------------------------------')
    try:
        print(arr)

        if len(arr) == length:
            print('Success')
        else:
            print('len results is wrong')
    except:
        print('There is a problem with len()')

    print("\nTesting insertAT()")
    print('-------------------------------------------')
    print('Before test, array is {}'.format(arr))
    try:
        arr.insertAt(15, 'insertion')
        print('after inserting at index 15, array is {}'.format(arr))
        arr.insertAt(2, 'insertion')
        print('after inserting at index 2, array is {}'.format(arr))

        print('Success')
    except:
        print('There is a problem with insertAt()')

    print('\nTesting delete()')
    print('-------------------------------------------')
    print('Before test, array is {}'.format(arr))
    try:
        arr.delete(1)
        print('after deleting 1, array is {}'.format(arr))
        print('Success')

    except:
        print('There is a problem with delete()')

    print('\nTesting pop()')
    print('-------------------------------------------')
    print('Before test, array is {}'.format(arr))
    try:
        last = arr.pop()
        print('The popped item is {}'.format(last))
        print('after pop(), array is {}'.format(arr))
        print('Success')
    except:
        print('There is a problem with pop()')
