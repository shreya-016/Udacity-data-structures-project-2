# Project Explanation
Explanation of the different project submodules

## Project 1
For the __LRU_Cache__ problem, after thinking of using different approaches (included previous failures), it has been
decided to use the __OrderedDict()__, specifically the use of the _method_ __pop(key)__ or __del cache[key]__ to do cache eviction based on least recently used value.

### Time and Space complexity
Here Time complexity is O(1) as required in the problem. Here for _space complexity_,if we consider the capacity as n then the *space complexity* will be __O(n)__.

## Project 2
The recursion process, is based on the visit of each folder, on each folder we keep the files that match the desired
pattern and we keep on going deeper on the folder structure by launching subsequent calls to the function.

### Time and Space complexity
In therms of __time complexity__ it is dependant on the number of iterations that are launched that is the __depth__ and __width__ of folders resulting in a __O(d*w)__. 
As for the space complexity it is directly dependent on the number of returns the function does, hence, the number of found files __f__, __O(f)__.

## Project 3
For huffman algorithm we created serveral classes like
1. Node
2. Encoder
3. Tree
4. Decoder 

### Time and Space complexity
In respects to the study of the _time complexity_, would be __O(Ln)__, being _**L**_ the maximum length of a codeword. If I had not used a _built it_ 
function for sorting the input that takes __O(n*log(n))__; ending up the time complexity being __O(n*log(n))__. In 
respects to the _space complexity_, it is directly related to the __size of the employed alphabet__, in this case
**_k_**, resulting in __O(k)__.

## Project 4 

### Time and Space complexity
The time complexity of this algorithm is dependant on the number of iterations that are launched. Being in this case
dependent on __encapsulation of groups__ and __number of users__ of folders, resulting in a __O(g*u)__. As for the 
_space complexity_, it is directly dependent on the number of returns the function does, hence, in this case __O(1)__.

## Project 5
#Here we have bunch of classes 
1. Block
2. Blockchain
3. BlockNode
We have used a linked list here to add and print functions for blockchain. The __time complexity__ here would be __O(n)__ as we are printing the blocks one by one in the
printBlockchain methed.
For __space complexity__ we have n blocks in total and each block has 4 different components like data, hash, previoushash and timestamp, 
so here also the __space complexity__ would be __O(n)__.

## Project 6 
Complexity Analysis:
Operation 1: Union
..................
Note: All elements in the union must be unique.
Union = linked_list_1 + linked_list_2
M = size of the first linked list
N = size of the second linked list

TC: O(M+N)
SC: O(M+N)

This can also be written as:
TC: O(n)
SC: O(n)

Operation 2: Intersection
.........................
Intersection = Unique common nodes between linked_list_1 and linked_list_2.
We create a set of linked_list_1 so that the lookup can be done with O(1).
For every node in linked_list_2, we check if the value is presented in
the set of linked_list_1 or not.

TC: O(n)
SC: O(n)
"""
