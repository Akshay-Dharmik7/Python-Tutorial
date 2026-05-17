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


# Commonly used built-in functions on sets:
## 1) len(s):
Number of elements.  
Example: len({1,2,3}) → 3.

##  2) sum(s):
Sum of numeric elements.  
Example: sum({1,2,3}) → 6.

## 3) min(s):
Smallest element.  
Example: min({1,2,3}) → 1.

## 4) max(s):
Largest element.  
Example: max({1,2,3}) → 3.

## 5) sorted(s):
Returns sorted list.  
Example: sorted({3,1,2}) → [1,2,3]. 

## 6) any(s):
True if any element is truthy.  
Example: any({0, 1}) → True.

## 7) all(s):
True if all elements are truthy.  
Example: all({1, 2}) → True. 

## 8) enumerate(s):
Index-value pairs.  
Example: for i, v in enumerate(s).

## 9) zip(s1, s2):
Pairs elements from sets.  
Example: zip({1,2}, {'a','b'}).

## 10) set(iterable):
Converts iterable to set.  
Example: set([1,2,2,3]) → {1,2,3}.

#  Set Update Methods (in-place):
## 1) update(s2) or |=:
Add all elements from s2.  
Example: s1.update(s2) or s1 |= s2.

## 2) intersection_update(s2) or &=:
Keep only common elements.  
Example: s1.intersection_update(s2) or s1 &= s2.

## 3) difference_update(s2) or -=:
Remove elements in s2.  
s1.difference_update(s2) or s1 -= s2.

## 4) symmetric_difference_update(s2) or ^=:
Keep only unique elements.  
s1.symmetric_difference_update(s2) or s1 ^= s2