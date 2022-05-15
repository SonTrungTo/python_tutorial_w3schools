thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "orange", "banana"))
print(thistuple)

# Unpacking
fruits = ("apple", "mango", "banana", "pineapple", "grapes", "sword")
(red, *tropic, pink, weapon) = fruits
print(red, tropic, pink, weapon)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
print(tuple1 * 2)
print(tuple2 * 2)
