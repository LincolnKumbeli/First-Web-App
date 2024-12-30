def confirm_weight():
    while True:
        try:
            weight = float(input("Enter the child's weight in kg: "))
            confirmation = input(f"Is the weight {weight} kg? (yes/no): ").strip().lower()
            if confirmation in ['yes', 'y']:
                return weight
            elif confirmation in ['no', 'n']:
                print("Please enter the weight again.")
            else:
                print("Please respond with 'yes' or 'no'.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_doses(weight):
    doses = {
        "Amoxicillin, Flucloxacillin, Chloramphenicol (25mg/kg)": 25 * weight,
        "Ceftriaxone (50mg/kg)": 50 * weight,
        "Lasix (1mg/kg)": 1 * weight,
        "Lasix (0.5mg/kg)": 0.5 * weight,
        "Hydrocortisone (4mg/kg)": 4 * weight,
        "Flagyl (7.5mg/kg)": 7.5 * weight,
        "Paracetamol (15mg/kg)": 15 * weight
    }
    return doses

def calculate_fluids(weight):
    bolus_fluids = {
        "Bolus (10mL/kg)": 10 * weight,
        "Bolus (15mL/kg)": 15 * weight,
        "Bolus (20mL/kg)": 20 * weight
    }

    if weight <= 10:
        maintenance_rate = 4 * weight
    elif weight <= 30:
        maintenance_rate = (4 * 10) + (2 * (weight - 10))
    else:
        maintenance_rate = (4 * 10) + (2 * 20) + (1 * (weight - 30))

    two_thirds_maintenance_rate = maintenance_rate * 2 / 3
    
    return bolus_fluids, maintenance_rate, two_thirds_maintenance_rate

def main():
    weight = confirm_weight()
    doses = calculate_doses(weight)
    bolus_fluids, maintenance_rate, two_thirds_maintenance_rate = calculate_fluids(weight)

    print("\nDrug Doses (mg):")
    for drug, dose in doses.items():
        print(f"{drug}: {dose:.2f} mg")

    print("\nFluid Requirements:")
    for bolus, volume in bolus_fluids.items():
        print(f"{bolus}: {volume:.2f} mL")
    print(f"Maintenance Rate (4:2:1 Rule): {maintenance_rate:.2f} mL/hour")
    print(f"Two Thirds Maintenance Rate (⅔ MR): {two_thirds_maintenance_rate:.2f} mL/hour")

if __name__ == "__main__":
    main()
