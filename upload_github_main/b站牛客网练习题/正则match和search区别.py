import re

text = 'pythontab'
m = re.match(r'\w+', text)
if m:
    print(m.group(0))
else:
    print('not match')