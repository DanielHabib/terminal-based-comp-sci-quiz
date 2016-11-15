TYPE_QUESTION = "question"
TYPE_IMPLEMENTATION = "implementation"

prompts = [
    {
        "id": 1,
        "type": TYPE_QUESTION,
        "title": "Petabyte Conversion",
        "prompt": "How many bits are in 11.3 PetaBytes",
        "answer": "~90 Quadrillion. 11.3 * (2^50) * 8",
    },
    {
        "id": 2,
        "type": TYPE_QUESTION,
        "title": "Quicksort Lowerbound Intuition",
        "prompt": "What is the largest lower bound asymptotic time complexity function of Quicksort?",
        "answer": "Ω(NlogN) In most academic implementations. Explanation: Sorting of an array is finding a specific permutation of that array. We know there are n! permutations of any given sequence of values,and every permutation requires our algorithm to handle it differnetly,  so even if we had perfect splits, we still would have a tree of height log(n!) = O(Nlogn)"
    },
    {
        "id":3,
        "type": TYPE_QUESTION,
        "title": "A* Intuition",
        "prompt": "What is A*? What is an issue that can occur when using this heuristic?",
        "answer": "A* is a greedy graph traversal that tries to find the path the fastest from point a->b. At every point we look at the adjenct vertexes and evaluate them using some function(Usually the distance formula) the best value is the one we pursue. A* can get stuck at local minimum"
    },
    {
        "id" : 4,
        "type": TYPE_IMPLEMENTATION,
        "prompt": "Quicksort Implementation",
        "title": "Randomized Quicksort Implementation",
        "funcName": "quicksort",
        "description": "Perform quicksort inplace leveraging a random pivot selection to increase the odds of achieving O(nlogn) time complexity.",
        "arguments": ["arr"],
        "test": {
            "input": [[1,5,2,6,3]],
            "output": [1,2,3,5,6],
        }
    },
    {
        "id" : 5,
        "type": TYPE_IMPLEMENTATION,
        "prompt": "Mergesort Implementation",
        "title": "Mergesort Implementation",
        "funcName": "mergesort",
        "description": "Perform mergesort capable of achieving O(nlogn) time complexity.",
        "arguments": ["arr"],
        "test": {
            "input": [[1,5,2,6,3]],
            "output": [1,2,3,5,6],
        },
    },
    {
        "id": 6,
        "type": TYPE_QUESTION,
        "title": "Different Byte Prefixes",
        "prompt": "What are the prefixes and approximate values in order for 2^10, 2^20, 2^30, 2^40 , 2^50 Bytes",
        "answer": "1 thousand - kilo, 1 million - mega, 1 billion - giga, 1 trillion - tera, 1 quadrillion - peta",
    },
    {
        "id": 7,
        "type": TYPE_QUESTION,
        "title": "Mathematical Induction Intuition",
        "prompt": "What is Mathematical Induction? How does it apply to algorithm design?",
        "answer": "Mathematical Induction is a mathematical method that can be used ot prove the correctness of an equation or algorithm. If we want to prove that our algorithm/equation is correct, we start by testing the base case, if that holds then we evaluate the answer at n & n+1",
    },
    {
        "id": 8,
        "type": TYPE_QUESTION,
        "title": "RAM Model of Computation Intuition",
        "prompt": "What is the RAM Model of Computation?",
        "answer": "Its a machine/language independant method for analyzing algorithms. When analyzing algorithms using this method we are only concerned with number of steps an algorithm takes to complete",
    },
    {
        "id": 9,
        "type": TYPE_QUESTION,
        "title": "Spanning Tree Intuition?",
        "prompt": "What is a minimum spanning tree",
        "answer": "A tree that touches all given nodes in a set while achieving the minimum total edge length possible. We can use Primm's algorithm to find it"
    },
    {
        "id": 10,
        "type": TYPE_QUESTION,
        "title": "Signedness Intuition",
        "prompt": "What is the difference between a signed and unsigned integer?",
        "answer": "the difference lies in whether the integer contains a  sign bit. A signed integer uses the leftmost bit to hold onto the sign of the bit vector, allowing for negative numbers. However an unsigned integer with the same length bit-vector can represent values that are 2n + 1 greater  "
    },
    {
        "id": 11,
        "type": TYPE_QUESTION,
        "title": "Significant Bits",
        "prompt": "Where is the most significant bit in a bit vector located?",
        "answer": "the leftmost bit is the most significant bit"
    },
    {
        "id":12,
        "type": TYPE_QUESTION,
        "title": "LRU Cache Intuition",
        "prompt": "What is an LRU Cache?",
        "answer": "A Least Recently Used Cache, is a cache system usually implemented with a dictionary that uses that key as the input of the function and the value as the result of the function with the corresponding input. This is used to help memoize functions to repeat computing the result on function executions with the same input"
    },

    {
        "id":13,
        "type": TYPE_QUESTION,
        "title": "Stablity when Sorting",
        "prompt": "What is the difference between a stable and an unstable sort",
        "answer": "A stabe sort maintains the relative order between equal values, while an unstable sort makes no guarentees about the relative position of equal order elements"
    },
    {
        "id" : 14,
        "type": TYPE_IMPLEMENTATION,
        "prompt": "Parity Intuition",
        "title": "Checking for Parity with Bitwise Operators",
        "funcName": "checkParity",
        "description": "Determine whether `num` is even using only bitwise operators.",
        "arguments": ["num"],
        "test": {
            "input": [37],
            "output": False,
        },
    },
    {
        "id":15,
        "type": TYPE_QUESTION,
        "title": "Depth First Search Tree Intuition on Graphs",
        "prompt": "What is a depth first search tree represenation of an undirected graph? Why is this tree representation useful?",
        "answer": "Running DFS on a graph creates a Tree Representation. While processing the graph, we break edges up into Tree Nodes and Edge Nodes. This can be used to detect cycles and finding articulation vertexes"
    },
    {
        "id":16,
        "type": TYPE_QUESTION,
        "title": "Traveling Salesman Problem Intuition",
        "prompt": "What is the Traveling Salesman Problem? How is it classified with regards to its computational complexity",
        "answer": "The traveling salesman problem is a problem in graph theory requiring the most efficient (i.e., least total distance) Hamiltonian cycle a salesman can take through each of n cities. No general method of solution is known, and the problem is NP-hard."
    },
    {
        "id":17,
        "type": TYPE_QUESTION,
        "title": "AVL Trees Intuition",
        "prompt": "What is an AVL Tree?",
        "answer": "An AVL is a binary tree if for every node X, the difference in the height of X's left and right subtrees is at most 1. AVL trees are used in order to maintain a balanced Binary Tree."
    },
    {
        "id":18,
        "type": TYPE_QUESTION,
        "title": "Integer Division Intuition",
        "prompt": "What is the difference between integer division and regular division",
        "answer": "integer division is equal to using regular division and then flooring to the nearest integer"
    },
    {
        "id": 19,
        "type": TYPE_QUESTION,
        "title": "Anonymous Function Intuition",
        "prompt": "What is an anonymous function?",
        "answer": "An anonymous function is a function that is not stored in a program file, but is associated with a variable whose data type is function_handle. Anonymous functions can accept inputs and return outputs, just as standard functions do. However, they can contain only a single executable statement. ",
    },
    {
        "id": 20,
        "type": TYPE_QUESTION,
        "title": "Unicode/ASCII intuition",
        "prompt": "What is the difference between Unicode And ASCII?",
        "answer": """
        ASCII defines 128 characters(Not Numbers), which map to the numbers 0–127. Unicode defines (less than) 2^21 characters, which, similarly, map to numbers 0–2^21 (though not all numbers are currently assigned, and some are reserved).

        Unicode is a superset of ASCII, and the numbers 0–128 have the same meaning in ASCII as they have in Unicode. For example, the number 65 means "Latin capital 'A'".

        Because Unicode characters don't generally fit into one 8-bit byte, there are numerous ways of storing Unicode characters in byte sequences, such as UTF-32 and UTF-8.
        """,
    },
    {
        "id" : 21,
        "type": TYPE_IMPLEMENTATION,
        "prompt": "Binary Search Implementation",
        "title": "Basic Binary Search Implementation",
        "funcName": "binarySearch",
        "description": "find the index of the value `x` in the given array `arr`",
        "arguments": ["arr", "x"],
        "test": {
            "input": [[1,2,3,4,5,6,7], 4],
            "output": 3,
        },
    },
    {
        "id": 22,
        "type": TYPE_QUESTION,
        "title": "Bit Vector Intuition",
        "prompt": "What is a bit vector?",
        "answer": "A bit array (also known as bitmap, bitset, bit string, or bit vector) is an array data structure that compactly stores bits",
    },
    {
        "id": 23,
        "type": TYPE_QUESTION,
        "title": "Asymptotic Order Intuition",
        "prompt": "Place the Following values in increasing asymptotic order: O(2^n), O(n), O(n!), O(1), O(n^2), O(logn), O(n^3)?",
        "answer": "O(1), O(logn), O(n), O(nlogn), O(n^2), O(n^3), O(2^n), O(n!)",
    },
    {
        "id": 24,
        "type": TYPE_QUESTION,
        "title": "Heuristic Intuition",
        "prompt": "What is a heuristic? Give an example of why someone would use one",
        "answer": "The term heuristic is used for algorithms which find solutions among all possible ones ,but they do not guarantee that the best will be found,therefore they may be considered as approximately and not accurate algorithms.These algorithms,usually find a solution close to the best one and they find it fast and easily.Sometimes these algorithms can be accurate,that is they actually find the best solution, but the algorithm is still called heuristic until this best solution is proven to be the best.The method used from a heuristic algorithm is one of the known methods,such as greediness,but in order to be easy and fast the algorithm ignores or even suppresses some of the problem's demands.",
    },
    {
        "id": 24,
        "type": TYPE_QUESTION,
        "title": "Combinatorics Intuition",
        "prompt": "Explain the study of Combinatorics. How does it apply to programming?",
        "answer": """
       Combinatorics is a branch of mathematics concerning the study of finite or countable discrete structures. Aspects of combinatorics include counting the structures of a given kind and size (enumerative combinatorics), deciding when certain criteria can be met, and constructing and analyzing objects meeting the criteria (as in combinatorial designs and matroid theory), finding `largest`, `smallest`, or `optimal` objects (extremal combinatorics and combinatorial optimization), and studying combinatorial structures arising in an algebraic context, or applying algebraic techniques to combinatorial problems (algebraic combinatorics).
        """,
    },

    {
        "id": 25,
        "type": TYPE_QUESTION,
        "title": "Hamiltonian Path Intuition",
        "prompt": "What is a hamiltonian path",
        "answer": """
            A path in a graph (Directed or Undirected) that visits every vertex exactly once. In addition, it is known as a hamiltonian cycle if it is a cycle.
        """,
    },
]
