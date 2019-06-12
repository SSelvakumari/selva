a=input()
v=['a','e','i','o','u','A','E','I','O','U']
if(a.isalpha()):
  if(a in v):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
