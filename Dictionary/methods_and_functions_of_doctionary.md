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