def is_isogram(string):
    new_string=string.lower().replace(" ","").replace("-","")
    isogram=0
    for char in new_string:
      if new_string.count(char)==1:
          isogram+=1
    if len(new_string)==isogram: 
        return True
    else:    
        return False  
