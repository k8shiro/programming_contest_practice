import re

s = 'ab???abbb?'
parts = re.findall(r'[a-zA-Z]+|\?+', s)
print(parts)