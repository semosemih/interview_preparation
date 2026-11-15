# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.


# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

#1. Sorting
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s)!= len(t):
            return False
        return sorted(s) == sorted(t)


#2. Hash Map
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if(len(s)!=len(t)):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
#             Python'da "Köşeli Parantez" Ne Anlama Gelir?
# Java'daki .put(key, value) metodunda parantezin içine iki şeyi virgülle ayırıp yazarsın: put(anahtar, değer).

# Python'da ise bu iş konumla (yerle) çözülür. Eşittir (=) işaretinin solunda ve sağında olmana göre Python o parantezin ne anlama geldiğini şak diye anlar:

# Köşeli Parantez Eşittirin Solundaysa (countS[s[i]]):

# Python der ki: "Bunu eşittir'in soluna yazdığına göre, bu kesinlikle Key (Anahtar) adresidir!"

# Zaten köşeli parantezin içine yazdığın şey (s[i]) kelimenin içindeki harftir. Python onun Key olduğunu oradan anlar.

# Sağdaki Değer (1 + ...):

# Eşittirin sağında kalan her şey ise o Key'in Value (Değer)'i olmak zorundadır. Çünkü sol taraf adres, sağ taraf ise o adrese taşınacak kargodur.

# Yani Java'daki o iki parametreli yapı Python'da şöyle bir rol paylaşımına dönüşür:

# Java: countS.put( Anahtar, Değer ) (Hepsi parantezin içinde, ikiz kardeş gibi yan yana)

# Python: countS[ Anahtar ] = Değer (Biri parantezin içinde sol tarafta, diğeri eşittirin sağında)
            countT[t[i]] = 1 + countT.get(t[i] , 0) #buradaki 0 aslinda default olarak atanan degerdir
        return countS == countT
    #"Acaba countS'teki bütün harfler countT'de var mı?" -> Evet, var.
    # "Peki bu harflerin sayıları (value) tutuyor mu? 
    # ('a': 3 ikisinde de var mı?, 'n': 1 ikisinde de var mı? vb.)" 
    # -> Evet, hepsi tutuyor!