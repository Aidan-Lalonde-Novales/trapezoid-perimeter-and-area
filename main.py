# Created By Aidan
# Created Oct 5th 2020
# 
# Code that asks for the measurements of a trapezoid, then calculates the perimeter and the area.
game.splash("Lets calculate the area and perimeter of a trapezoid.")
bottom_base = game.ask_for_number("Enter the length of the bottom base (cm)")
top_base = game.ask_for_number("Enter the length of the top base (cm)")
left_side = game.ask_for_number("Enter the length of the left side (cm)")
right_side = game.ask_for_number("Enter the length of the right side (cm)")
height = game.ask_for_number("Enter the height (cm)")
perimeter = bottom_base + (top_base + (left_side + right_side))
game.splash("The perimeter of the trapezoid:" + ("" + str(bottom_base)) + "cm by " + ("" + str(top_base)) + "cm by " + ("" + str(left_side)) + "cm by " + ("" + str(right_side)) + "cm is " + ("" + str(perimeter)) + "cm.")
area = (top_base + bottom_base) / 2 * height
game.splash("The area of the trapezoid:" + ("" + str(bottom_base)) + "cm by " + ("" + str(top_base)) + "cm divided by 2 by " + ("" + str(height)) + "cm is " + ("" + str(area)) + "cm2. ")