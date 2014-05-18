"""
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case
Problem found here:
http://oj.leetcode.com/problems/anagrams/
"""

"""
Note. Both of my solutions return a list of lists of anagrams (since that
seemed like the more useful output to me).  However LeetCode expects a single
list of words which are anagrams of other words in any order.  So these
solutions will not be accepted on the site.
"""



"""
My first solution, this was not fast enough because primarily I had
not thought of sorting the strings and using them as keys for a dict.
I still rather like the map based word matching that I used here though.
"""
class Solution1:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        sizes = {}
        anags = []
        for str in strs:
            str = str.strip()
            if len(str) not in sizes:
                sizes[len(str)] = []
            sizes[len(str)].append((str, self.dictifyWord(str)))
        for num, word_tuples in sizes.iteritems():
            matches = self.matchWords(word_tuples)
            for match in matches:
                if match != []:
                    anags.append(match)
        return anags
    
    def dictifyWord(self, word):
        out = {}
        for letter in word:
            if letter in out:
                out[letter] += 1
            else:
                out[letter] = 1
        return out
            
    def matchWords(self, word_dicts):
        matched = []
        while len(word_dicts) > 1:
            (word1, dict1) = word_dicts.pop()
            if dict1:
                found = []
                for word2, dict2 in word_dicts:
                    if dict2 and dict1 == dict2:
                        found.append(word2)
                        dict2.clear()
                if found:
                    found.append(word1)
                    matched.append(found)
        return matched

"""
My second solution, this passes the test on LeetCode
"""
class Solution2:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        word_list = {}
        for word in strs:
            ordered = ''.join(sorted(word.strip()))
            if ordered not in word_list:
                word_list[ordered] = []
            word_list[ordered].append(word.strip())
        all_anags = []
        for key, words in word_list.iteritems():
            if len(words) > 1:
                all_anags.append(words)
        return all_anags

#test
sol1 = Solution1()
sol2 = Solution2()
f = open('anagram_test_words.txt', 'r')
matches1 = sol1.anagrams(f)
print 'This is all of the anagrams found by my first solution:'
for match in matches1:
    print match
f.close()
f = open('anagram_test_words.txt', 'r')
matches2 = sol2.anagrams(f)
print '\nThis is all of the anagrams found by my second solution:'
for match in matches2:
    print match
f.close()
