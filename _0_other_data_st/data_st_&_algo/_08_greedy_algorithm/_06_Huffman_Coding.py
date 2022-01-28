"""
Huffman Coding

Huffman Coding is a technique of compressing data to reduce its size without losing any of the details. It was first
    developed by David Huffman.

Huffman Coding is generally useful to compress the data in which there are frequently occurring characters.

How Huffman Coding works?
Suppose the string below is to be sent over a network.

            B C A A D D D C C A C A C A C

            Initial string

Each character occupies 8 bits. There are a total of 15 characters in the above string. Thus, a total of 8 * 15 = 120
    bits are required to send this string.

Using the Huffman Coding technique, we can compress the string to a smaller size.

Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.

Once the data is encoded, it has to be decoded. Decoding is done using the same tree.

Huffman Coding prevents any ambiguity in the decoding process using the concept of prefix code ie. a code associated
    with a character should not be present in the prefix of any other code. The tree created above helps in
    maintaining the property.

Huffman coding is done with the help of the following steps.

1. Calculate the frequency of each character in the string.

                        1  6  5  3
                        B  C  A  D

                        Frequency of string

2. Sort the characters in increasing order of the frequency. These are stored in a priority queue Q.

                        1  3  5  6
                        B  D  A  C

                        Characters sorted according to the frequency


3. Make each unique character as a leaf node.

4. Create an empty node z. Assign the minimum frequency to the left child of z and assign the second minimum frequency
    to the right child of z. Set the value of the z as the sum of the above two minimum frequencies.


                            4  5  6
                            .  A  C

                                 4
                               /  \
                              1    3
                              B    D

                              Getting the sum of the least numbers


5. Remove these two minimum frequencies from Q and add the sum into the list of frequencies (* denote the internal nodes
    in the figure above).

6. Insert node z into the tree.

7. Repeat steps 3 to 5 for all the characters

                        6   9
                        C   .


                            9
                           /  \
                          4    5
                        /  \   A
                       1    3
                       B    D

                       Repeat steps 3 to 5 for all the characters.


                       15
                       .

                         15
                        /   \
                       6     9
                      C     /  \
                          4    5
                        /  \   A
                       1    3
                       B    D

                       Repeat steps 3 to 5 for all the characters.


8. For each non-leaf node, assign 0 to the left edge and 1 to the right edge.



                         15
                     0  /   \  1
                       6     9
                      C   0 /  \ 1
                          4    5
                       0 /  \1 A
                       1    3
                       B    D

                       Assign 0 to the left edge and 1 to the right edge




For sending the above string over a network, we have to send the tree as well as the above compressed-code. The total
    size is given by the table below.



Character	    Frequency	Code	Size
A	            5	        11	    5*2 = 10
B	            1	        100	    1*3 = 3
C	            6	        0	    6*1 = 6
D	            3	        101	    3*3 = 9

4 * 8 = 32 bits	15 bits	 	        28 bits

Without encoding, the total size of the string was 120 bits. After encoding the size is reduced to 32 + 15 + 28 = 75.

Decoding the code
For decoding the code, we can take the code and traverse through the tree to find the character.

Let 101 is to be decoded, we can traverse from the root as in the figure below.

                         15
                     0  /    \  [1]
                       6      9
                      C   [0]/   \ 1
                          4       5
                       0 /  \[1]  A
                       1    3
                       B    D

                       Decoding


Huffman Coding Algorithm

create a priority queue Q consisting of each unique character.
sort then in ascending order of their frequencies.
for all the unique characters:
    create a newNode
    extract minimum value from Q and assign it to leftChild of newNode
    extract minimum value from Q and assign it to rightChild of newNode
    calculate the sum of these two minimum values and assign it to the value of newNode
    insert this newNode into the tree
return rootNode
"""


# Node of a Huffman Tree
class Nodes:
    def __init__(self, probability, symbol, left=None, right=None):
        # probability of the symbol
        self.probability = probability

        # the symbol
        self.symbol = symbol

        # the left node
        self.left = left

        # the right node
        self.right = right

        # the tree direction (0 or 1)
        self.code = ''


""" A supporting function in order to calculate the probabilities of symbols in specified data """


def CalculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) is None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols


""" A supporting function in order to print the codes of symbols by travelling a Huffman Tree """
the_codes = dict()


def CalculateCodes(node, value=''):
    # a huffman code for current node
    newValue = value + str(node.code)

    if node.left:
        CalculateCodes(node.left, newValue)
    if node.right:
        CalculateCodes(node.right, newValue)

    if not node.left and not node.right:
        the_codes[node.symbol] = newValue

    return the_codes


""" A supporting function in order to get the encoded result """


def OutputEncoded(the_data, coding):
    encodingOutput = []
    for element in the_data:
        # print(coding[element], end = '')
        encodingOutput.append(coding[element])

    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string


""" A supporting function in order to calculate the space difference between compressed and non compressed data"""


def TotalGain(the_data, coding):
    # total bit space to store the data before compression
    beforeCompression = len(the_data) * 8
    afterCompression = 0
    the_symbols = coding.keys()
    for symbol in the_symbols:
        the_count = the_data.count(symbol)
        # calculating how many bit is required for that symbol in total
        afterCompression += the_count * len(coding[symbol])
    print("Space usage before compression (in bits):", beforeCompression)
    print("Space usage after compression (in bits):", afterCompression)


def HuffmanEncoding(the_data):
    symbolWithProbs = CalculateProbability(the_data)
    the_symbols = symbolWithProbs.keys()
    the_probabilities = symbolWithProbs.values()
    print("symbols: ", the_symbols)
    print("probabilities: ", the_probabilities)

    the_nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in the_symbols:
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))

    while len(the_nodes) > 1:
        # sorting all the nodes in ascending order based on their probability
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)
        # for node in nodes:
        #      print(node.symbol, node.prob)

        # picking two smallest nodes
        right = the_nodes[0]
        left = the_nodes[1]

        left.code = 0
        right.code = 1

        # combining the 2 smallest nodes to create new node
        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right)

        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)

    huffmanEncoding = CalculateCodes(the_nodes[0])
    print("symbols with codes", huffmanEncoding)
    TotalGain(the_data, huffmanEncoding)
    encodedOutput = OutputEncoded(the_data, huffmanEncoding)
    return encodedOutput, the_nodes[0]


def HuffmanDecoding(encodedData, huffmanTree):
    treeHead = huffmanTree
    decodedOutput = []
    for x in encodedData:
        if x == '1':
            huffmanTree = huffmanTree.right
        elif x == '0':
            huffmanTree = huffmanTree.left
        try:
            if huffmanTree.left.symbol is None and huffmanTree.right.symbol is None:
                pass
        except AttributeError:
            decodedOutput.append(huffmanTree.symbol)
            huffmanTree = treeHead

    string = ''.join([str(item) for item in decodedOutput])
    return string


the_data1 = "AAAAAAABBCCCCCCDDDEEEEEEEEE"
# the_data1 = 'BCAADDDCCACACAC'
print(the_data1)
encoding, the_tree = HuffmanEncoding(the_data1)
print("Encoded output", encoding)
print("Decoded Output", HuffmanDecoding(encoding, the_tree))


"""
Huffman Coding Complexity
The time complexity for encoding each unique character based on its frequency is O(nlog n).

Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n). Thus 
    the overall complexity is O(nlog n).

Huffman Coding Applications

Huffman coding is used in conventional compression formats like GZIP, BZIP2, PKZIP, etc.
For text and fax transmissions.
"""