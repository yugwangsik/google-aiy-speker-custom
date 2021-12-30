import re

string = "에어컨 온도 도로 틀어줘"
test = re.sub(r'[^0-9]', '', string)
str1 = "아아" + test + "이이이이"
print(str1)
print(type(test))
