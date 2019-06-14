import re
text=input()
c=len(text)-len(re.findall('[\w]',text))
print(c)
