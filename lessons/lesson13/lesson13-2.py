import re

s = "Привет! Как дела? А у меня нормально"
result = re.findall(r"[бвгджзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ]\w+", s)
print(result)