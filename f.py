import random
"""
most of the thing in here represent human behaviors that occur in a park, there could be a lot more and feel free to make those as i am just one guy imagining scenarios
like everything in this project, feel free to make this more compelex
"""
# You cant get a value from a list in a list, this is my workaround 
def fetch(list,place):
  fetchur = list
  return list[place]


def wake(c, time, max_time): # decides whether or not the person will wake up and go to the park at a given time
  if c == 1:
     # This is based on a float/fraction, so the numbers are between 0 and 1
      i = random.randint(1,3-4(time/max_time)) #once in a lifetimers are more likely to start early
      if i == 1:
        return True
      else:
        return False
    
  elif c == 2:
     # This is based on a float/fraction, so the numbers are between 0 and 1
      i = random.randint(1,9-4(time/max_time)) # Every few yearers will come around noon, tending to be more early
      if i == 1:
        return True
      else:
        return False


  elif c == 3:
     # This is based on a float/fraction, so the numbers are between 0 and 1
      i = random.randint(1,12-4(time/max_time)) # Year passers come a little earlier than noon since its still a bit a of a drive
      if i == 1:
        return True
      else:
        return False      
      
  if c == 4:
     # This is based on a float/fraction, so the numbers are between 0 and 1
      i = random.randint(1,16-4(time/max_time)) # Bloggers only come around prime time
      if i == 1:
        return True
      else:
        return False
