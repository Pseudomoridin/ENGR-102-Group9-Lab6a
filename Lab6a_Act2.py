# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 5A Activity 2
# Date:         September 29, 2021

#yoooooo

prime = True
totalPrime = 0
for i in range (2, 101):
    for j in range(2, 50):
        if i % j == 0 and i != j:
            prime = False
    if prime == True:
        print("{} is prime".format(i))
        totalPrime += 1
    else:
        print("{} is not prime".format(i))
    prime = True
print("There are {} prime numbers between 2 and 100".format(totalPrime))