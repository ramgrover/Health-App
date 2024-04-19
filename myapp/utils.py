def calculate_days_to_target(current_weight, target_weight, strategy):
    weight_difference = abs(current_weight - target_weight)

    if strategy == "mild":
        days = weight_difference / 0.25  # Assuming 0.25 kg change per day for mild strategy
    elif strategy == "moderate":
        days = weight_difference / 0.5  # Assuming 0.5 kg change per day for moderate strategy
    elif strategy == "quick":
        days = weight_difference / 1.0  # Assuming 1 kg change per day for quick strategy
    else:
        return "Invalid strategy input"

    return int(days)


def calculate_maintenance_calories(weight_kg, height_cm, age, gender, activity):
    # Mifflin-St Jeor Equation for BMR
    if gender.lower() == "male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    elif gender.lower() == "female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        return "Invalid gender"

    # Activity Factor to calculate Total Daily Energy Expenditure (TDEE)
    activity_factors = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    if activity not in activity_factors:
        return "Invalid activity level"

    tdee = bmr * activity_factors[activity]
    return bmr, tdee

def main():
    weight_kg = float(input("Enter weight in kilograms: "))
    height_cm = float(input("Enter height in centimeters: "))
    age = int(input("Enter age in years: "))
    gender = input("Enter gender (male/female): ")
    activity = int(input("Choose from the activity levels:\n1. Sedentary (little or no exercise)\n2. Lightly active (light exercise/sports 1-3 days a week)\n3. Moderately active (moderate exercise/sports 3-5 days a week)\n4. Very active (hard exercise/sports 6-7 days a week)\n5. Extra active (very hard exercise/sports & physical job or 2x training)\nMake a choice: "))

    bmr, maintenance_calories = calculate_maintenance_calories(weight_kg, height_cm, age, gender, activity)
    if isinstance(maintenance_calories, str):
        print(maintenance_calories)
    else:
        print("Basal Metabolic Rate (BMR):", bmr)
        print("Maintenance calories per day:", maintenance_calories)

        # Calculate calories to be consumed per day for different weight loss options
        mild_weight_loss = maintenance_calories - (7700 * 0.25 / 7)
        moderate_weight_loss = maintenance_calories - (7700 * 0.5 / 7)
        extreme_weight_loss = maintenance_calories - (7700 * 1 / 7)

        print("\nCalories consumed per day for:")
        print("Mild weight loss (0.25 kg/week):", mild_weight_loss)
        print("Moderate weight loss (0.5 kg/week):", moderate_weight_loss)
        print("Extreme weight loss (1 kg/week):", extreme_weight_loss)

        # Integrate with the weight_input_form.html and render the results
        # Use an appropriate method to render the HTML with the calculated values
