# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Twitter.
# 
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# 
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# 
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

import json

class Trie:
    def __init__(self, words):
        self.data = {}

        for word in words:
            self.add_word(word)

    def __repr__(self):
        return json.dumps(self.data, indent=2)

    def add_word(self, word):
        node = self.data

        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]

        node["*"] = True
                
    def search(self, prefix):
        level = self.data
        for c in prefix:
            if c not in level:
                return []
            level = level[c]

        words = []

        def dfs(node, stack):
            for key, value in node.items():
                if key == "*":
                    words.append("".join(stack))
                else:
                    stack.append(key)
                    dfs(value, stack)
                    stack.pop()

        dfs(level, [c for c in prefix])
        return words

trie = Trie(["dog", "deer", "deal"])
assert trie.search("de") == ["deer", "deal"]
