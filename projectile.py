import math

def horizontal_velocity():
    try:
        initial_hvelocity = round(float(input("Enter the initial horizontal velocity of the projectile: ")))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    print("The average horizontal velocity during flight is:", initial_hvelocity,"m/s" )
    return

def vertical_velocity():
    try:
        initial_vvelocity = float(input("Enter the initial vertical velocity of the projectile: "))
        time_elapsed = float(input("Enter time elapsed: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    average_vvelocity = round(initial_vvelocity - (9.81 * time_elapsed), 2)
    print("The average vertical velocity during flight is:", average_vvelocity,"m/s")
    return

def horizontal_distance():
    try:
        initial_hvelocity = float(input("Enter the initial horizontal velocity of the projectile: "))
        time_elapsed = float(input("Enter time elapsed: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    horizontal_distance = round((initial_hvelocity * time_elapsed), 2)
    print("The horizontal distance of the projectile is:", horizontal_distance,"m")
    return

def maximum_height():
    try:
        initial_vvelocity = float(input("Enter the initial vertical velocity of the projectile: "))
        angle = float(input("Enter the angle of projection: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    angle_rad = math.radians(angle)
    maximum_height = round(((initial_vvelocity**2 * math.sin(angle_rad)**2) / (2 * 9.8)), 2)
    print("The maximum height reached by the projectile is:", maximum_height,"m")
    return

def range():
    try:
        velocity = float(input("Enter the velocity of the projectile: "))
        angle = float(input("Enter the angle of projection: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    angle_rad = math.radians(angle)
    range = round(((velocity**2) * math.sin(2 * angle_rad) / 9.8), 2)
    print("The total distance covered by the projectile is:", range,"m")
    return

def total_time():
    try:
        velocity = float(input("Enter the velocity of the projectile: "))
        angle = float(input("Enter the angle of projection: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    angle_rad = math.radians(angle)
    total_time = round((((2*velocity) * math.sin(angle_rad)) / 9.8), 2)
    print("The total time elapsed throughout the projectile's flight is:", total_time,"s")
    return

def full_analysis():
    try:
        velocity = float(input("Enter launch velocity: "))
        angle = float(input("Enter angle (degrees): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    angle_rad = math.radians(angle)
    t_total = round((2 * velocity * math.sin(angle_rad)) / 9.8, 2)
    max_height = round((velocity**2 * (math.sin(angle_rad)**2)) / (2 * 9.8), 2)
    rng = round(((velocity**2) * math.sin(2 * angle_rad)) / 9.8, 2)
    print(f"\nTotal Time: {t_total}s\nMax Height: {max_height}m\nRange: {rng}m\n")


x = True
while x:
    y = True
    
    while y:
        ask1 = input("""
    Standard Units:
    Distance - Meters (m)
    Time - Seconds (s)
    Velocity - Meters per Second (m/s)
    Acceleration - Meters per Second Squared (m/s^2)
    Are your units expressed in standard form?(y/n): """)

        if ask1 == 'n':
            unit = input("""
    [1] Distance
    [2] Time
    [0] Main Menu
    Which unit is not in standard form?: """)
            
            if unit == '1':
                initial_unit = str(input("Enter the unit given (full): "))
                if initial_unit.lower() == "feet":
                    try:
                        initial_distance = float(input("Enter the distance: "))
                    except ValueError:
                        print("Invalid input. Try again.")
                        continue
                    final_distance = round((initial_distance * 0.304800004), 2)
                    print("The distance in standard form is: ", final_distance,"m")
                    y = True
                elif initial_unit.lower() == "yard":
                    try:
                        initial_distance = float(input("Enter the distance: "))
                    except ValueError:
                        print("Invalid input. Try again.")
                        continue
                    final_distance = round((initial_distance * 0.9144), 2)
                    print("The distance in standard form is: ", final_distance,"m")
                    y = True
                elif initial_unit.lower() == "kilometer":
                    try:
                        initial_distance = float(input("Enter the distance: "))
                    except ValueError:
                        print("Invalid input. Try again.")
                        continue
                    final_distance = round((initial_distance / 1000), 2)
                    print("The distance in standard form is: ", final_distance,"m")
                    y = True
            elif unit == '2':
                initial_unit = str(input("Enter the unit given (full): "))
                if initial_unit.lower() == "minutes":
                    try:
                        initial_duration = float(input("Enter the time elapsed: "))
                    except ValueError:
                        print("Invalid input. Try again.")
                        continue
                    final_duration = round((initial_duration / 60), 2)
                    print("The time elapsed in standard form is: ", final_duration,"s")
                    y = True
                elif initial_unit.lower() == "hour":
                    try:
                        initial_duration = float(input("Enter the time elapsed: "))
                    except ValueError:
                        print("Invalid input. Try again.")
                        continue
                    final_duration = round((initial_duration / 3600), 2)
                    print("The time elapsed in standard form is: ", final_duration,"s")
                    y = True

    ask2 = input("""
[1] Horizontal Velocity
[2] Vertical Velocity
[3] Horizontal Distance
[4] Maximum Height
[5] Range
[6] Total Time of Flight
[7] Full Analysis
                 
What do you need?: """)
        

    if ask2 == '1':
        horizontal_velocity()
    elif ask2 == '2':
        vertical_velocity()
    elif ask2 == '3':
        horizontal_distance()
    elif ask2 == '4':
        maximum_height()
    elif ask2 == '5':
        range()
    elif ask2 == '6':
        total_time()
    elif ask2 == '7':
        full_analysis()
    else:
        x = True

    choice = input("Would you like to perform another calculation? (y/n): ")
    if choice.lower() != 'y':
        print("Goodbye!")
        break




