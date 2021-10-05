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

# Finds the area for each individual layer
def get_layer_gold_foil(layer_number, cube_side_length):
    if layer_number == 1:
        return (cube_side_length ** 2) * 5
    this_layer_area = (cube_side_length * layer_number) ** 2
    previous_layer_area = (cube_side_length * (layer_number-1)) ** 2
    return ((cube_side_length ** 2) * layer_number * 4) + (this_layer_area - previous_layer_area)

# input
side_length = float(input("Enter the side length in meters: "))
layer_num = int(input("Enter the number of layers: "))

# Getting total area
total_area = 0
for x in range(1,layer_num+1):
    total_area += get_layer_gold_foil(x, side_length)

print("You need {:.2f} square meters of gold foil to cover the pyramid".format(total_area))