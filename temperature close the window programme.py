tmp = int(input("Enter the temperature "))
hmd = int(input("Enter the humidity "))

window = False

if window == False:
    if tmp >= 25 or (hmd >= 50):
        print("Close the window!")
        window = True
else: 
    if tmp <= 10 and (hmd >= 50):
        print("Close the window")
        window = False