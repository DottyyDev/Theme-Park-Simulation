import random
import f
# All things you may want dynamic for the simulation

# (In terms of the 36 time units in a sim day)
lifetime_wait_time = 12
couple_years_wait_time= 8
scaredy_cat_wait_time = 8
blogger_wait_time = 2 
yearly_pass_wait_time = 1

popsize = 100
nor = 6 # Number of rides
noa = 2 # Number of activities
avg_time_r = .1 # Average time a ride takes
avg_time_a = .25 # Average Time an activity takes

max_time: 36

pop = []
rides = []

x = 0
# Procedural generation of the population of people, feel free to make more
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
x = 0

# Procedural generation of rides
while x <= nor:
  i = random.randint(avg_time_r*100-5,avg_time_r*100+10)/100 # Big line of code basically making a number close to .1 of a time(2 minutes)
  r = random.randint(1+i*5,5+i*5) # Popularity of the ride, slightly influenced by the length
  n = random.randint(2*(i+1),8(i+2))*5 # How many people can be on the ride at once, in increments of 5 because i dont want weird numbers, long ride more people
  if x == 0:
    r = 6 # garuntees theres at least one of "the big rides" incase rng hates you 
  rides.append([x,i,n,r])
  x+=1
  
while x <= noa: # yes i literally just copy pasted this
  i = random.randint(avg_time_a*100-5,avg_time_a*100+20)/100 # Big line of code basically making a number close to .25 of a time(5 minutes)
  r = random.randint(1+i*5,5+i*5) # Popularity of the activity, slightly influenced by the length
  n = random.randint(2,8)*5 # How many people can be on the ride at once, in increments of 5 because i dont want weird numbers
  if x == 0:
    r = 6 # garuntees theres at least one of "the big rides" incase rng hates you 
  rides.append([x,i,r,n])
  x+=1  
# Across x(probably gonna be about 36) increments of time, the population will to activities and rides. 
time = 0

while time <= max_time:
    selpop = 0 # The person selected for the next action
    
    
