print('''
             MENU
      ------------------
    1. area  of circle
    2. circumference of circle
    3. area of rectangle
    4. perimeter of rectangle
    5. quit
      
      ''')
    
choice = input("choose an option: ")
intChoice = int(choice)

pi = 3.1415926535

if intChoice == 1:
    radius = input("whats the radius of the circle: ")
    intRad = int(radius)

    area = pi * intRad ** 2
    print(f"the area is {area}!")

elif intChoice == 2:
    radius = input("whats the radius of the circle: ")
    intRad = int(radius)

    circumference = 2 * pi * intRad

    print(f"the circumference is {circumference}!")

elif intChoice == 3:
    length = input("whats the length of the rectangle: ")
    width = input("whats the width of the rectangle: ")

    intLength = int(length)
    intWidth = int(width)

    area = intLength * intWidth

    print(f"the area is {area}!")

elif intChoice == 4:
    length = input("whats the length of the rectangle: ")
    width = input("whats the width of the rectangle: ")

    intLength = int(length)
    intWidth = int(width)

    perimeter = 2 * (intLength + intWidth)

    print(f"the perimeter is {perimeter}!")
elif intChoice == 5:
    print("program terminated.")
    
