## Function
def arbitrary_args_function(*kids):
    print("The youngest kid is", kids[2])
arbitrary_args_function("Alex", "Son", "Tom")

def arbitrary_key_function(**kids):
    print("The youngest kid is", kids["lname"])
arbitrary_key_function(lname="Aku", rname="Micro")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(5)
