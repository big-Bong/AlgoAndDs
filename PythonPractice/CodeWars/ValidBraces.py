def validBraces(string):
  dict = {"(":")","[":"]","{":"}"}
  stack = []
  for elem in string:
      if(elem not in dict):
          if(not stack or stack[-1] != elem):
              return False
          else:
              stack.pop()
      else:
          stack.append(dict[elem])
          
          
  
  return len(stack) == 0