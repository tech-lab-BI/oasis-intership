BMI_CATEGORIES = {
    "Underweight": (None, 18.5),
    "Normal": (18.5, 25),
    "Overweight": (25, 30),
    "Obese": (30, None)
}

def calculate_bmi(weight, height):
    """Calculate BMI"""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """Classify BMI into a category"""
    for category, (lower, upper) in BMI_CATEGORIES.items():
        if (lower is None or bmi >= lower) and (upper is None or bmi < upper):
            return category
    return "Unknown"

def main():
    """Command-line BMI calculator"""
    print("BMI Calculator")
    print("-------------")

    # Prompt user for weight (in kg)
    while True:
        try:
            weight = float(input("Enter your weight (in kg): "))
            if weight <= 0:
                print("Weight must be a positive number. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number. Try again!")

    # Prompt user for height (in m)
    while True:
        try:
            height = float(input("Enter your height (in m): "))
            if height <= 0:
                print("Height must be a positive number. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number. Try again!")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()