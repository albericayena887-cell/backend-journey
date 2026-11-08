import re

text = "Order 4271 shipped on 2026-03-14"

m = re.search(r"\d+", text)            # find the first run of digits
# print(m)                                # <re.Match object; span=(6, 10), match='4271'>
# print(m.group())                        # '4271'
# print(m.span())                         # (6, 10)  (the start and end index)


s = "Order 66 shipped 2026-03-14 to ada@dev.io"
mx = re.findall(r"\w+", text)
print(mx)   # ['Order', '4271', 'shipped', 'on', '2026', '03', '14']