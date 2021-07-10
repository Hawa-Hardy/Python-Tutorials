weight = int(input("Weight: "))
print("Not case sensitive. Type K for kg or L for pounds")
unit = str(input("K for (g) or (L) for lbs"))

if unit == "l" or unit == "L" :
    convert = weight // 2.20462262
    print("Weight in kg: " + str(convert))

if unit == "K" or unit == "k":
    convert = weight
    print("Weight in kg: " + str(convert))
