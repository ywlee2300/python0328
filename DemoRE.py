#DemoRE.py

import re

print(dir(re))


result = re.search("[0-9]*th", "  35th")
print(result)
result = re.match("[0-9]*th", "  35th")
print(result)
#print(result.group())

print(bool(re.search("apple", "this is apple")))
print(bool(re.search("\d{4}", "올해는 2022년")))