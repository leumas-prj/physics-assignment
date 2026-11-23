# 1. CALCULATION OF GRAVITATIONAL POTENTIAL
def gravitational_potential():
    G = 6.674e-11
    mass = float(input("Enter mass of the planet in kg: "))
    distance = float(input("Enter distance from the planet's centre in meters: "))

    if distance > 0:
        potential = -(G * mass) / distance
        print("Gravitational Potential =", potential, "J/kg")
    else:
        print("Distance must be greater than zero")


# 2. CALCULATION OF CENTRIPETAL ACCELERATION
def centripetal_acceleration():
    velocity = float(input("Enter velocity in m/s: "))
    radius = float(input("Enter radius in meters: "))

    if radius > 0:
        acceleration = velocity ** 2 / radius
        print("Centripetal Acceleration =", acceleration, "m/s2")
    else:
        print("Radius must be greater than zero")


# 3. CALCULATION OF SPECIFIC LATENT HEAT
def latent_heat():
    heat = float(input("Enter heat energy in Joules: "))
    mass = float(input("Enter mass in kg: "))

    if mass > 0:
        result = heat / mass
        print("Specific Latent Heat =", result, "J/kg")
    else:
        print("Mass must be greater than zero")


# 4. CALCULATION OF MAGNIFICATION
def magnification():
    image_height = float(input("Enter image height in cm: "))
    object_height = float(input("Enter object height in cm: "))

    if object_height != 0:
        result = image_height / object_height
        print("Magnification =", result)
    else:
        print("Object height cannot be zero")


# 5. CALCULATION OF CAPACITANCE
def capacitance():
    charge = float(input("Enter electric charge in Coulombs: "))
    voltage = float(input("Enter voltage in Volts: "))

    if voltage != 0:
        result = charge / voltage
        print("Capacitance =", result, "Farads")
    else:
        print("Voltage cannot be zero")


# MAIN PROGRAM
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Gravitational Potential")
    print("2. Centripetal Acceleration")
    print("3. Specific Latent Heat")
    print("4. Magnification")
    print("5. Capacitance")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        gravitational_potential()
    elif choice == "2":
        centripetal_acceleration()
    elif choice == "3":
        latent_heat()
    elif choice == "4":
        magnification()
    elif choice == "5":
        capacitance()
    else:
        print("Invalid selection. Choose between 1 and 5.")

    again = input("\nDo you want to perform another operation? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break