trials = 0
do = 0
total = 0

print("please enter a positive interger")
n = float(input())
print("""Please give my your winning dice combo \n"2-12 please" """)
x = float(input())
print("Do that again, or just enter the same number")
y = float(input())

while (trials < n):
  firstDi = math.floor(6*random.random()) + 1
  secondDi = math.floor(6*random.random()) + 1
  #print("the first dice is ", firstDi, "the second dice is ", secondDi)#line for testing 
  total = firstDi + secondDi
  if (total == x or total == y):
    do +=1
    #print ("we have a desired outcome") # line for testing 
  trials+= 1
  #print("the dice were", total, "this is round",trials) # line for testing 
print (do/trials)

