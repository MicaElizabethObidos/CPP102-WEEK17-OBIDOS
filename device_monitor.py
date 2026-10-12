def get_initial_readings():
    readings = [28, 31, 35, 37, 29]
    return readings

def classify_reading(reading, warning_limit, critical_limit):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"

def display_menu():
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()

def display_readings(readings):
    print("CURRENT READINGS")
    print("----------------")

    for i in range(len(readings)):
        print("Reading", i + 1, ":", readings[i], "°C")
    print()

def is_whole_number(text):
    if text == "":
        return False
    if text[0] == "-":
        return len(text) > 1 and text[1:].isdigit()
    return text.isdigit()

def add_reading(readings, lowest, highest):
    text = input("Enter new reading: ")

    if text == "":
        print("\nInvalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
    else:
        reading = int(text)

        if reading < lowest or reading > highest:
            print("\nInvalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(reading)
            print("\nReading added successfully.")
    print()

def display_classifications(readings, warning_limit, critical_limit):
    print("READING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(reading, "°C ->", category)
    print()

def compute_total(readings):
    total = 0

    for reading in readings:
        total = total + reading
    return total

def compute_average(readings):
    total = compute_total(readings)
    number_of_readings = len(readings)
    return total / number_of_readings

def find_minimum(readings):
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum

def find_maximum(readings):
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum

def count_category(readings, warning_limit, critical_limit, category):
    count = 0

    for reading in readings:
        current_category = classify_reading(reading, warning_limit,critical_limit)
        if current_category == category:
            count = count + 1
    return count

def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def display_summary(readings):
    number_of_readings = len(readings)

    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, 30, 35, "NORMAL")
    warning_count = count_category(readings, 30, 35, "WARNING")
    critical_count = count_category(readings, 30, 35, "CRITICAL")

    normal_percentage = normal_count / number_of_readings * 100
    warning_percentage = warning_count / number_of_readings * 100
    critical_percentage = critical_count / number_of_readings * 100

    status = determine_overall_status(
        warning_count, critical_count)

    print("MONITORING SUMMARY")
    print("------------------")
    print("Number of readings  :", number_of_readings)
    print("Total of readings   :", total)
    print("Average temperature : {:.2f} °C".format(average))
    print("Minimum temperature :", minimum, "°C")
    print("Maximum temperature :", maximum, "°C")
    print()

    print("NORMAL   : {} ({:.2f}%)".format(normal_count, normal_percentage))
    print("WARNING  : {} ({:.2f}%)".format(warning_count, warning_percentage))
    print("CRITICAL : {} ({:.2f}%)".format(critical_count, critical_percentage))
    print()

    print("Overall Status:", status)
    print()

def main():
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35
    choice = ""

    while choice != "5":
        display_menu()
        choice = input("Enter choice: ")
        print()

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            display_classifications(
                readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            print()
main()
