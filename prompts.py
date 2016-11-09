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
        "answer": "O(NlogN). Explanation: Sorting of an array is finding a specific permutation of that array. We know there are n! permutations of any given sequence of values,and every permutation requires our algorithm to handle it differnetly,  so even if we had perfect splits, we still would have a tree of height log(n!) = O(Nlogn)"
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
        "prompt": "",
        "title": "Randomized Quicksort Implementation",
        "answer": "",
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
        "prompt": "",
        "title": "Mergesort Implementation",
        "answer": "",
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
        "answer": "kilo, mega, giga, tera, peta",
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
        "prompt": "",
        "title": "Checking for Parity with Bitwise Operators",
        "answer": "",
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
        "title": "AVL Trees",
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
]

