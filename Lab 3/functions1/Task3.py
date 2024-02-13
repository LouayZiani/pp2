# Task 3:

def solve(number_heads, number_legs):
    for chicken in range(number_heads):
        rabbit = number_heads-chicken
        if 2*chicken + 4*rabbit == number_legs:
            return chicken, rabbit
    

answer = solve(number_heads=35, number_legs=94)
if answer:
    chicken, rabbit = answer
    print("There are",chicken, "chickens")
    print("There are",rabbit, "rabbits")
  
