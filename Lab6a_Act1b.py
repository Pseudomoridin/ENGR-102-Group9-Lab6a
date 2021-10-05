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

# input
length = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))

# Top area is just a square
total = 0
total += (n * length) ** 2

# Each side is just a triangle
## I no longer understand this part in the slightest, hopefully it works
### This does not work, keeping it here to tell me what not to do
#### total += (n * length) ** 2 * 4

# Please work
total += 4 * (n / 2) * (1 + n) * length ** 2

# output
print("You need {:.2f} square meters of gold foil to cover the pyramid".format(total))