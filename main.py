# Define a list of numbers
numbers = [5, 2, 9, 1, 7]

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted list
print("Sorted numbers in ascending order:", sorted_numbers)

# Sort the list in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)

# Print the sorted list in descending order
print("Sorted numbers in descending order:", sorted_numbers_desc)











# # Function to add two numbers
# def add(x, y):
#     return x + y
#
#
# # Function to subtract two numbers
# def subtract(x, y):
#     return x - y
#
#
# # Function to multiply two numbers
# def multiply(x, y):
#     return x * y
#
#
# # Function to divide two numbers
# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y
#
#
# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
#
# while True:
#     choice = input("Enter choice (1/2/3/4): ")
#
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#
#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))
#     else:
#         print("Invalid Input")
#
#     next_calculation = input("Do you want to perform another calculation? (yes/no): ")
#     if next_calculation.lower() != 'yes':
#         break
#
#





#import rembg

# from rembg import remove
# from PIL import Image
#
# input_path="C:\\Users\\AbdullahAmir\\Downloads\\redd.jpg"
#
# #input_path="C:\\Users\\AbdullahAmir\\Downloads\\my data\\66535326.jpg"
#
# output_path="C:\\Users\\AbdullahAmir\\Documents\\calculator\\calculator\\output_path\\redd.png"
# #output_path="C:\\Users\\AbdullahAmir\\Documents\\calculator\\calculator\\output_path\\66535326.png"
#
# image_input=Image.open(input_path)
# output=remove(image_input)
# output.save(output_path)
