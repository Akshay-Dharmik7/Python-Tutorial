# domains = [
#     'www.google.com',
#     'openai.com',
#     'localhost',
#     'WWW.FACEBOOK.COM'
# ]

# cleaned = [
#     # tranformation
#     d.lower().replace('www.', '')

#     # loop
#     for d in domains

#     # data filtering
#     if '.' in d
# ]

# print(cleaned)

# # In comprehension 
# # - filtering steps are option

# cleaned2 = [
#     # tranformation
#     d.lower().replace('www.', '')

#     # loop
#     for d in domains

#     # data filtering
#     # if '.' in d
# ]


# print(cleaned2)


Students_Name = [
    '  Akshay Dharmik  ',
    'SubhOdh Charan',
    '@Ram Shekhar   '
]

# List comprehension

# Cleaned = [
#     # Data tranformation
#     s.strip().lower().replace('@', '')

#     # loop
#     for s in Students_Name

#     # filtering
# ]

# print(Cleaned)
# ------------------------------------------------------

Cleaned = [
    # Data tranformation
    s.strip().lower().replace('@', '')

    # loop
    for s in Students_Name

    # filtering
    if 's' in s
]

print(Cleaned)

# ------------------------------------------------------
# cleaned = []
# for s in Students_Name:
#     # if s.strip().startswith('a'):
#        cleaned.append(s.strip()) 

# print(cleaned)