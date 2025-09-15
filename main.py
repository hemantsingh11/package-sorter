def sort(width, height, length, mass):
    volume = width * height * length
    if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        bulky = True
    else:
        bulky = False
    if mass >= 20:
        heavy = True
    else:
        heavy = False
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


w = float(input("Width (cm): "))
h = float(input("Height (cm): "))
l = float(input("Length (cm): "))
m = float(input("Mass (kg): "))

print("This package goes to:", sort(w, h, l, m))

assert sort(10, 10, 10, 1) == "STANDARD"
assert sort(150, 10, 10, 1) == "SPECIAL"
assert sort(10, 10, 10, 20) == "SPECIAL"
assert sort(150, 10, 10, 20) == "REJECTED"
assert sort(100, 100, 100, 0) == "SPECIAL"
assert sort(100, 100, 100, 20) == "REJECTED"
print("All the tests passed! Pls Hire me :)")
