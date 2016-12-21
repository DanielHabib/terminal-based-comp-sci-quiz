TYPE_QUESTION = "question"
TYPE_IMPLEMENTATION = "implementation"

TOPIC_DESIGN_PATTERN = "design pattern"

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
        "answer": "The most significant bit or high order bit is the bit in a binary number with the greatest value"
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
        "answer": "Integer division is division in which the fractional part (remainder) is discarded "
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
        ASCII defines 128 characters(Letters, Numbers, Symbols), which map to the numbers 0–127. Unicode defines (less than) 2^21 characters, which, similarly, map to numbers 0–2^21 (though not all numbers are currently assigned, and some are reserved).

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
    {
        "id": 26,
        "type": TYPE_QUESTION,
        "title": "Permutation Intuition",
        "prompt": "What is a permutation? How many different Permutations are there of a set of n unique elements? ",
        "answer": """
            A Permutation is a way, especially one of several possible variations, in which a set or number of things can be ordered or arranged. There are N! permutations of N unique elements
        """,
    },
    {
        "id": 27,
        "type": TYPE_QUESTION,
        "title": "Compiler Intuition",
        "prompt": "What is a compiler",
        "answer": """
        A compiler is a special program that processes statements written in a particular programming language and turns them into machine language or "code" that a computer's processor uses.
        """,
    },
    {
        "id": 28,
        "type": TYPE_QUESTION,
        "title": "Interpreted Vs Compiled Intuition",
        "prompt": "What is the difference between a compiled language and an interpretted language?",
        "answer": """
        In a compiled implementation, the original program is translated into native machine instructions, which are executed directly by the hardware.
        In an interpreted implementation, the original program is translated into something else. Another program, called "the interpreter", then examines "something else" and performs whatever actions are called for. Depending on the language and its implementation, there are a variety of forms of "something else". From more popular to less popular, "something else" might be"""
    },
    {
        "id" : 29,
        "type": TYPE_IMPLEMENTATION,
        "prompt": "Longest Common Subsequence Implementation",
        "title": "Longest Common Subsequence Implementation",
        "funcName": "lcss",
        "description": "Return the Longest Common Subsequence between two arrays",
        "arguments": ["a", "b"],
        "test": {
            "input": [[1,2,3,4,5,6,7], [4, 6, 7, 8, 23, 5]],
            "output": [4,6,7],
        },
    },
    {
        "id": 30,
        "type": TYPE_QUESTION,
        "title": "Optimality Principle Intuition",
        "prompt": "What is the principle of optimality?",
        "answer": """
           In reference to Dynammic Programming, This means that partial Solutions can be optimally extended with regard to the state after the partial solution, instead of the specifics around the partial solution.
        """,
    },
    {
        "id": 31,
        "type": TYPE_QUESTION,
        "title": "Dynammic Programming Efficiency Intuition",
        "prompt": "How can we determine the runtime of any dynammic programming algorithm?",
        "answer": """
            The number of Partial Solutions * How Long it Takes to evaluate each Partial Solution
        """,
    },
    {
        "id": 32,
        "type": TYPE_QUESTION,
        "title": "Backtracking Intuition",
        "prompt": "What is Backtracking?",
        "answer": """
        A systematic way to iterate through all the possible configurations of a search space
        """,
    },
    {
        "id": 33,
        "type": TYPE_QUESTION,
        "title": "LSB Intuition",
        "prompt": "What is the Least Significant Bit?",
        "answer": """
            The Least Significant bit is the bit in a binary integer that determines the parity.  
        """,
    },
    {
        "id": 34,
        "type": TYPE_QUESTION,
        "title": "Mutex Vs Semaphore Intuition",
        "prompt": "Name an instance when you would use a mutex, and a situation when you would use a binary semaphore",
        "answer": """
         Mutex is for exclusive access to a resource. A Binary semaphore should be used for Synchronization
        """,
    },
    {
        "id": 35,
        "type": TYPE_QUESTION,
        "title": "TCO Intuition",
        "prompt": "What is Tail Call Optimization?",
        "answer": """
            TCO (Tail Call Optimization) is the process by which a compiler can make a call to a function and take no additional stack space. The only situation in which this happens is if the last instruction executed in a function f is a call to a function g. This can be used to make some recursive algorithms not require any additional space maintaining a callstack
        """,
    },
    {
        "id": 36,
        "type": TYPE_QUESTION,
        "title": "Open Addressing Intuition",
        "prompt": "What is Open Addressing? What method can we use to prevent Primary Clustering?",
        "answer": """
        Open Addressing is a method of collision resolution where we look for open slots in an array to place one of the key/value pairs that collided.
        There are methods of probing we can use, linear probing does a linear search for nearby open slots, this works but can result in Primary Clustering. 
        Primary Clustering is when multiple different hashindexes share large segments of probing segments. To remedy this we can leverage Random Probing.
        Contrary to its name random probing leverages a Pseudo Random Sequence of array positions to tell us which slot to check next. For instance if the first slow in the random sequence array is two we would add two to the calculated hash index, if there is a collision there we would add the next value in the random Sequence to the initially calculated hash index

        """,
    },
    {
        "id": 37,
        "type": TYPE_QUESTION,
        "title": "Decision Problem Intuition",
        "prompt": "What is a Decision Problem?",
        "answer": """
            The problem of finding a way to decide whether a formula or class of formulas is true or provable within a given system of axioms.
        """,
    },
    {
        "id": 38,
        "type": TYPE_QUESTION,
        "title": "Deterministic Intuition",
        "prompt": "What is the difference between a deterministic and nondeterministic algorithm?",
        "answer": """
            NonDeterministic algorithms that even when given the same input values can exhibit different behaviors on different runs. 
            An algorithm that solves a problem in nondeterministic polynomial time can run in polynomial time or exponential time depending on the choices it makes during execution 

            """,
    },
    {
        "id": 39,
        "type": TYPE_QUESTION,
        "title": "Standard Deviation Intuition",
        "prompt": "What is the standard deviation?",
        "answer": """
                Quantity calculated to indicate the extent of deviation for a group as a whole.
                For a finite set of numbers, the standard deviation is found by taking the square root of the average of the squared deviations of the values from their average value. 
            """,
    },
    {
        "id": 40,
        "type": TYPE_QUESTION,
        "title": "Adjacency Matrix Intuition",
        "prompt": "When would you use an Adjacency Matrix as the underlying implementaton of A Graph? Why would you avoid using one?",
        "answer": """
            Adjacency Matrixes are useful when you frequently need to check edge existence, O(1), or update an existing edge, O(1).
            Another reason to consider using an adjacency matrix would be if the {number of edges} is close to the {number of vertexes}^2
            Adjacency Matrixes waste a lot of space on sparse arrays and are very slow when it comes to adding and removing vertexes.
            Adjacency Matrixes are useful if you know you will have a fixed number of nodes, or you are able to allocate memory at the begininng of operations for all future vertexes
            Graph traversals on Adjacency Matrixes run in quadratic time,O(N^2), because every slot in the matrix needs to be visited
            """,
    },
    {
        "id": 41,
        "type": TYPE_QUESTION,
        "title": "Adjacency List Intuition",
        "prompt": "When would you use an Adjacency List as the underlying implementaton of A Graph? Why would you avoid using one?",
        "answer": """
            Adjacency Lists are powerful when we plan on adding/removing nodes from our Graph.
            Adjacency lists allow for traversals in O(V+E)
            Adjacency Lists are powerful on spase graphs, only requiring O(V+E) additional space

            Adjacency Lists remove edges slowly O(E)
            """,
    },
    {
        "id": 42,
        "type": TYPE_QUESTION,
        "title": "Abstract Data Type Intuition",
        "prompt": "What is an abstract data type? How does it compare to a datastructure?",
        "answer": """
                An Abstract datatype is defined by its behavior (semantics) from the point of view of a user of the data, specifically in terms of possible values, possible operations on data of this type, and the behavior of these operations
                A data structure is more concerned with the actual underlying implementation and consist of concrete representations of data
            """,
    },
    {
        "id": 43,
        "type": TYPE_QUESTION,
        "title": "Topological Sort Intuition",
        "prompt": "What is a Topological Sort?",
        "answer": """
            A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
            """,
    },
    {
        "id": 44,
        "type": TYPE_QUESTION,
        "title": "Singleton Intuition",
        "topic": TOPIC_DESIGN_PATTERN,
        "prompt": "What is the singleton design pattern?",
        "answer": """
            Singleton pattern restricts the instantiation of a class and ensures that only one instance of the class exists in the application.
            """,
    },
    {
        "id": 45,
        "type": TYPE_QUESTION,
        "title": "Design Pattern Intuition",
        "topic": TOPIC_DESIGN_PATTERN,
        "prompt": "What is a design pattern? Why are they useful?",
        "answer": """
        A design Pattern is a guideline for identifying and solving  common design problems.
            They help solve common design problems based on the collected intelligence of the software engineering community, and they provide a concise vocabulary for discussing design problems and their solutions.
            """,
    }
]
