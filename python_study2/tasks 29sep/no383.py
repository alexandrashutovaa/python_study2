#Given two strings ransomNote and magazine,
#return true if ransomNote can be constructed 
#by using the letters from magazine 
#and false otherwise.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c = 0
        arr = (ransomNote)
        for x in arr:
            if magazine.count(x) < ransomNote.count(x):
                c+=1
        if c>0:
            return False
        else:
            return True
        