print("Calculate the area of a wall.")

Feed = input("Enter the width in meters: ")
Width = float(Feed)

Feed = input("Enter the height in meters: ")
Height = float(Feed)
def display_number(value):
    return int(value) if isinstance(value, float) and value.is_integer() else value


Width = display_number(Width)
Height = display_number(Height)
print(f"Width is {Width} m and height is {Height} m.")

Area = Width * Height
print(f"The wall will be {display_number(Area)} square meters.")