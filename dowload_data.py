#!.python_env/bin/python

# # COPYBOOK, AGE, ANTHOLOGY
# 0 = No ( or is not true )
# 1 = Yes aka is true ( for AGE it means ADULT BOOK )

# Language: This is what language the books are dependent on the number:
# 1 = Unknown
# 2 = English
# 3 = Japanese
# 4 = Chinese
# 5 = Korean
# 6 = French
# 7 = German
# 8 = Spanish
# 9 = Italian
# 10 = Russian

# FRQ: Frequency, aka how common things are.
# This shows up on 'DATA' types for books when querying those.

# For AUTHOR, and CIRCLES thees are the following ( A, C )
# 0 = Not Set
# 1 = Guest
# 2 = Main

# For EVERYTHING else:
# 0 = Not Set
# 1 = Very few
# 2 = Some
# 3 = Many
# 4 = Most
# 5 = All

from mugimugi.client.synchronous import SearchObject

for p in SearchObject(authors=["Nakajima Yuka"]).fetch_all():
    for child in p.getroot():
        print(child.tag, child.attrib)
        print(child.items())
