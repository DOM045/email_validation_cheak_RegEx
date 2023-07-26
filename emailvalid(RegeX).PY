import re
txt=input("enter email ")
#^ :- start with
#\ :- special chara
#? :- zero or one occurrence
#\w:- Returns a match where the string contains any word characters
# {} :- postion of full stop
#$ :- full stop position from last
email_condition="^[a-z]+[\._]?[a-z 0-9] + [@]\w + [.]\w{2,3}$"
#search fun :-	Returns a Match object if there is a match anywhere in the string
if re.search(email_condition,txt):
    print("Right email enter by user")
else:
    print("Wrong email enter bt user")