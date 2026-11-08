import re


text = "Order 4271 shipped on 2026-03-14"
mx = re.sub(r"\d", "#", text)
print(mx)