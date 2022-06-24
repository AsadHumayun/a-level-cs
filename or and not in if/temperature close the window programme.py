tmp = int(input("Enter the temperature "))
hmd = int(input("Enter the humidity "))

window = False #False (if closed)

if window == False:
    if tmp >= 25 or (hmd >= 50):
        print("Close the window!")
        window = True
else: 
    if tmp <= 10 and (hmd >= 50):
        print("Open the window")
        window = False

'''
The task description, as I INTERPRETED it.

Ask the user to input the temperature and humidity. 
If the window is NOT closed, and the temperature >= 25, or the humidity is >= 50, CLOSE the window.
    - [if the window is open],
        - if the temperature <= 10 AND the humidity is >=50, close the window.
'''