--------------------------------------------------------------------------------------------------
5.21 Indirect recursion

def ping(i):
if i > 0:
return pong(i - 1)
return "0"
def pong(i):
if i > 0:
return ping(i - 1)
return "1"
print(ping(29))

output: "1"
-------------------------------------------------------------------------------------------------

5.22 String Slicing

word = "bender"
print(word[1:4])

output: "and"
