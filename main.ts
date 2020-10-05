// Created By Aidan
// Created Oct 5th 2020
// 
// Code that asks for the measurements of a trapezoid, then calculates the perimeter and the area.
game.splash("Lets calculate the area and perimeter of a trapezoid.")
let bottom_base = game.askForNumber("Enter the length of the bottom base (cm)")
let top_base = game.askForNumber("Enter the length of the top base (cm)")
let left_side = game.askForNumber("Enter the length of the left side (cm)")
let right_side = game.askForNumber("Enter the length of the right side (cm)")
let height = game.askForNumber("Enter the height (cm)")
let perimeter = bottom_base + (top_base + (left_side + right_side))
game.splash("The perimeter of the trapezoid:" + ("" + bottom_base) + "cm by " + ("" + top_base) + "cm by " + ("" + left_side) + "cm by " + ("" + right_side) + "cm is " + ("" + perimeter) + "cm.")
let area = (top_base + bottom_base) / 2 * height
game.splash("The area of the trapezoid:" + ("" + bottom_base) + "cm by " + ("" + top_base) + "cm divided by 2 by " + ("" + height) + "cm is " + ("" + area) + "cm2. ")
game.splash("Done")
