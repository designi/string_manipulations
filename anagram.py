

class anagram:
    def __init__(self,word):
        self.word = word
    
    def __str__(self):
        return self.word
    
    def prepAnagram(self,word):
        r = ''
        for w in word:
            try:
                assert int(w)
            except:
              if w.isalnum():
                  r+=w
        return r
    
    def anagrams(self,word):
        mapping = {}
        i = 0
        w = self.prepAnagram(word)
        for l in w:
            mapping[i] = l
            i+=1
        return mapping

if __name__ == '__main__':
    word = 'n!1ck'
    a = anagram(word)
    print(a.anagrams(word))