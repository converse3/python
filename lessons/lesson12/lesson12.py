import re

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
result = re.match("DC", s)
print(result)

result = re.search("DC", s)
print(result)

result = re.findall("DC", s)
print(result)

result = re.split("/", s, maxsplit=3)
print(result)

result = re.sub("A", "O", s)
print(result)

result = re.fullmatch("A", s)
print(result)