TYPE_QUESTION = "question"
TYPE_IMPLEMENTATION = "implementation"

prompts = [
    {
        "id": 1,
        "type": TYPE_QUESTION,
        "prompt": "How many bits are in 11.3 PetaByte",
        "answer": "~90 Quadrillion",
    },
    {
        "id": 2,
        "type": TYPE_QUESTION,
        "prompt": "What is the largest lower bound asymptotic time complexity function of Quicksort?",
        "answer": "O(NlogN). Explanation: Sorting of an array is finding a permutation of that array. We know there are n! permutations of any given sequence of values, so even if we had perfect splits, we still would have a tree of height log(n!) = O(Nlogn)"
    },
    {
        "id":3,
        "type": TYPE_QUESTION,
        "prompt": "What is A*? What is an issue that can occur when using this heuristic?",
        "answer": "A* is a greedy graph traversal that tries to find the path the fastest from point a->b. At every point we look at the adjenct vertexes and evaluate them using some function(Usually the distance formula) the best value is the one we pursue. A* can get stuck at local minimum"
    },
    {
        "id" : 4,
        "type": TYPE_IMPLEMENTATION,
        "prompt": "Write out Quicksort",
        "answer": "",
        "funcName": "quicksort",
        "input": ["arr"],
        "test": {
            "input": [1,5,2,6,3],
            "output": [1,2,3,5,6],
        }
    }
]
