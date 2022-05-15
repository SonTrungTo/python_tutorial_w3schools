str1 = """ Whatever you are, I am
the best.
"""

print(str1)

for x in "banana":
  print(x)

print(len("baba"))

txt = "The best things in life are free!"
print("expensive" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

a = "Hello, World!"
print(a.replace("A", "J"))

p1 = 123
p2 = 456
p3 = 789
txt = "I want {2} dollars for {0} cows without {1} dollars for tax "
print(txt.strip().format(p1, p2, p3))

print(a.replace("H", "J"))
