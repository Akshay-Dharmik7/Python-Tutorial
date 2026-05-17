# Tuple has only 2 built-in methods (since tuples are immutable)

## t = (1, 2, 3, 3, 4, 5)

## 1) count(x):
Counts occurrences of a value.  
Example: t.count(3)→2.

## 2) index(x):
Returns index of first occurrence    
Example: t. index(3) → 3

# Commonly used built-in functions that work on tuples:

## 1) len(t):
Number of items.  
Example: len((1,2,3)) → 3  

## 2) sorted(t):
Returns a new sorted list.  
Example: sorted((3,1,2)) → [1,2,3].

## 3) reversed(t):
Returns a reverse iterator.  
Example: tuple(reversed(t)).

## 4) sum(t):
Sum of numeric items.  
Example: sum((1,2,3)) → 6.

## 5) min(t):
Smallest item.  
Example: min((1,2,3)) → 1  

## 6) max(t):
Largest item.  
Example: max((1,2,3)) → 3.

## 7) enumerate(t):
Index-value pairs.  
Example: for i, v in enumerate(t).

##  8) zip(t1, t2):
Pairs elements from tuples.  
Example: zip((1,2), ('a','b'))


## 9) map(fn, t):
Applies function to each item.  
Example: map(str, (1,2,3)).

## 10) filter(fn, t):
Filters items by function.  
Example: filter(None, t).

## 11) any(t):
True if any item is truthy.  
Example: any((0, 1, 0)) → True.

## 12) all(t):
True if all items are truthy.  
Example: all((1, 1, 0)) → False. 

## 13) tuple(iterable):
Converts iterable to tuple.  
Example: tuple([1,2,3])

