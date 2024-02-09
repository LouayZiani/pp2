# Task 3:

def solve(numheads, numlegs):
    for chicken in range(numheads+1):
        rabbit = numheads-chicken
        if 2*chicken + 4*rabbit == numlegs:
            return chicken, rabbit
    

answer = solve(numheads=35, numlegs=94)
if answer:
    chicken, rabbit = answer
    print("chickens: ",chicken)
    print("rabbits: ",rabbit)
  