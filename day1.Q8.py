def isNumeric(s):
   s = s.strip()
   try:
      s = float(s)
      return True
   except:
      return False
print(isNumeric("0.2"))
print(isNumeric("xyz"))
print(isNumeric("Hello"))
print(isNumeric("-2.5"))
print(isNumeric("10"))
