# Dictionary Methods:
## 1)  get(key, default):
Returns value for key (or default if missing)  
Example: d.get('name', 'Unknown')

## 2) keys():
Returns all keys  
Example: d.keys() → dict_keys(['a', 'b'])

## 3) values():
Returns all values  
Example: d.values() → dict_values([1, 2]).

## 4) items():
Returns key-value pairs  
Example: d.items() → dict_items([('a',1), ('b',2)]).

## 5) pop(key, default):
Removes & returns value (or default).  
Example: d.pop('name', None).

## 6)popitem():
Removes & returns last key-value pair.  
Example: d.popitem().

## 7)clear():
Removes all items.  
Example: d.clear().

## 8) update(d2):
Merges another dictionary.  
Example: d.update({'c': 3}).

## 9) setdefault(key, default):
Returns value; sets if missing.  
Example: d.setdefault('age', 25). 

## 10) copy():
Returns a shallow.  
Example: copyd2 = d.copy()

# Dictionary Membership & Lookup:
## 1) in:
Checks if key exists'name'.  
Example: in d → True.

## 2) not in:
Checks if key doesn't exist.  
Example: 'age' not in d → True. 

## 3) d[key]:
Access value by key.  
Example: d['name']. 

## 4) d[key] = value.
Set/update key-value pair.  
Example: d['age'] = 30. 

## 5) del d[key]:
Delete a key-value pair.  
del d['name']

Dictionary Membership & Lookup:
OperationDescriptionExampleinChecks if key exists'name' in d → Truenot inChecks if key doesn't exist'age' not in d → Trued[key]Access value by keyd['name']d[key] = valueSet/update key-value paird['age'] = 30del d[key]Delete a key-value pairdel d['name']

# Commonly used built-in functions on dictionaries:
## 1) len(d):
Number of key-value pairs.  
Example: len({'a': 1, 'b': 2}) → 2.

## 2) sorted(d):
Returns sorted list of keys.  
Example: sorted({'c': 3, 'a': 1}) → ['a', 'c'].

## 3) sorted(d.values()): 
Sorted list of values.  
Example: sorted({'a': 3, 'b': 1}.values()) → [1, 3].

## 4) sorted(d.items()):
Sorted list of key-value pairs.  
Example: sorted(d.items()). 

## 5) enumerate(d):
Index-key pairs.  
Example: for i, k in enumerate(d).

## 6) zip(d.keys(), d.values()): 
Pairs keys with values.  
Example: zip(d.keys(), d.values()). 

## 7) dict(iterable):
Converts iterable to dict.  
Example: dict([('a', 1), ('b', 2)]).  

## 8) all(d):
True if all keys are truthy.  
Example: all({'a': 1, 'b': 0}) → True.

## 9) any(d):
True if any key is truthy.  
Example: any({0: 1, 1: 2}) → True