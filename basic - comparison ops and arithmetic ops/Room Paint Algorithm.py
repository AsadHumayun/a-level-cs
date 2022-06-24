width = float(input("Please enter the width of the room"))
length = float(input("Please enter the length"))
height = float(input("Please enter the height"))
areaOfUnpainted = float(input("Please enrter area of unpainted areas"))

ttlar0 = float((width * height * 4) + (length * height))
ttlar0 = ttlar0 - areaOfUnpainted
sqm = 10.5 # this being the cost of the paint, per square metre
cost = ttlar0 * sqm * 2

print(f"Total cost ${cost}\nLitres needed: {ttlar0/11}")