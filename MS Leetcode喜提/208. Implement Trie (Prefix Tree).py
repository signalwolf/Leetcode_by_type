class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr_dict = self.trie
        for letter in word:
            curr_dict = curr_dict.setdefault(letter, {})
        curr_dict['end'] = 'end'

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr_dict = self.trie
        for letter in word:
            if letter in curr_dict:
                curr_dict = curr_dict[letter]
            else:
                return False
        else:
            if 'end' in curr_dict:
                return True
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr_dict = self.trie
        for letter in prefix:
            if letter in curr_dict:
                curr_dict = curr_dict[letter]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)