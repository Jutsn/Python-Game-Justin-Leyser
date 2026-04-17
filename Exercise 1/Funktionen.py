import random

def divide_two_floats(float1: float, float2: float):
	if float1 < float2:
		outcome = float1 / float2
	elif float1 > float2:
		outcome = float2 / float1
	else:
		return 1 
	return outcome

print(divide_two_floats(random.uniform(0.00,10.00), random.uniform(0.00,10.00)))