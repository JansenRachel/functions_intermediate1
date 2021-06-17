import random
def randInt(min=0, max=100):
    num = random.random()*(max-min) + min
    return round(num)

print(randInt())
# print(randInt(max=35))
# print(randInt(min=66))
# print(randInt(min=16, max=85))

print(randInt(max=5))
print(randInt(min=95))
print(randInt(min=20, max=25))

