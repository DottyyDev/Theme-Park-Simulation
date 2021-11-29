import random

# All things you may want dynamic for the simulation

# (In terms of the 36 time units in a sim day)
lifetime_wait_time = 12
couple_years_wait_time= 8

blogger_wait_time = 2 
yearly_pass_wait_time = 1






pop = []
popsize = 10
x = 0
while x <= popsize:
# This for loop creates 5 different catogories of people, each more petty than the last
# 1 - Once in a lifetime: determined to ride certain rides
# 2 - Every couple years: Will go for the big rides as long as they arent crazy long waits
# 3 - ScaredyCat - only go for minor ride and basic activities, wait doesnt matter too much
# 4 - Yearly Pass - They can always go for a ride later if its too long, because they come a lot
# 5 - Blogger - in the middle of the yearly pass and the every couple years, will wait a little longer than yearly pass and goes exclusivly on the popular rides
  i = random.randint(1,10)

  if i == 3 or i == 4:
    pop.append([x,1])

  elif i == 5 or 6 or 7 or 8 or 9:
    pop.append([x,2])

  elif i == 5:
    pop.append([x,3])
    # ScaredyCat

  elif i < 3:
    pop.append([x,4])
    # Yearly pass

  elif i == 10:
    pop.append([x,5])
    # Blogger
  x += 1

# Across 36 increments of time, the population will to activities and rides. 
_time = 0


