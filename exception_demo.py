class AgeError(Exception):
   pass

def set(age):
   if age < 0:
       raise AgeError("Age cannot be negative.")
   print(f"Age set to {age}")

try:
   set(-6)
except AgeError as e:
   print(e)