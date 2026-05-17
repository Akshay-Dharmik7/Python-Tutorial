# Set Methods:
## 1) add(x):
Adds an elements.  
Example: add(4)

## 2) remove(x):
Removes element (raises error if missing)  
Example: s.remove(3)

## 3) discard(x):
Removes element (no error if missing)  
Example: s.discard(3)  

## 4) pop():
Removes & returns arbitrary element  
Example: s.pop()

## 5) clear():
Removes all elementss.  
Example: clear()

## 6) copy():
Returns a shallow  
copys2 = s.copy()

# Set Comparison & Membership:
## 1) union(s2) or |:
All elements in either set.  
Example: s1 | s2 or s1.union(s2)

## 2) intersection(s2) or &:
Elements in both sets.  
Example: s1 & s2 or s1.intersection(s2).

## 3) difference(s2) or -:
Elements in s1 but not s2.  
Example: s1 - s2 or s1.difference(s2).

## 4) symmetric_difference(s2) or ^: 
Elements in either but not both.  
s1 ^ s2 or s1.symmetric_difference(s2).

## 5)  issubset(s2) or <=:
Is s1 a subset of s2?  
s1 <= s2 or s1.issubset(s2).

## 6) issuperset(s2) or >=:
Is s1 a superset of s2?  
s1 >= s2 or s1.issuperset(s2)

## 7)  isdisjoint(s2):
Do sets have no common elements?  
s1.isdisjoint(s2)