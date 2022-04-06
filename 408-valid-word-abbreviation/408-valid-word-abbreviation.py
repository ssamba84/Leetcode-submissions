class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = -1
        wi = i = 0
        while i < len(abbr):
            c = abbr[i]
            if c.isalpha():
                if c != word[wi]:
                    return False
                i += 1
                wi += 1
            else:
                previ = i
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                if abbr[previ] == '0':
                    return False
                wi += int(abbr[previ:i])
                #print (wi, word[wi], abbr[i])
            
            if wi == len(word) and i == len(abbr):
                return True
            
            if wi >= len(word):
                return False
        return (wi == len(word))