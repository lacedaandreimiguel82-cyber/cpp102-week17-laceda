def valid_integer(value):
    return value.isdigit()


def collect_readings():
    data = []

    print("=" * 42)
    print("       SMART TEMPERATURE CONTROL")
    print("=" * 42)

    while True:
        amount = input("How many readings do you want to record? ")

        if valid_integer(amount) and int(amount) > 0:
            amount = int(amount)
            break

        print("Please enter a positive whole number.")

    for position in range(1, amount + 1):
        while True:
            entry = input(f"Temperature #{position}: ")

            if valid_integer(entry) and 0 <= int(entry) <= 100:
                data.append(int(entry))
                break

            print("Invalid! Temperature must be from 0 to 100.")

    print("\nInitial readings successfully recorded!")
    return data


def show_dashboard():
    print("\n" + "=" * 42)
    print("           CONTROL CENTER")
    print("=" * 42)
    print("  [1] Display All Temperatures")
    print("  [2] Record New Temperature")
    print("  [3] Check Temperature Status")
    print("  [4] View System Report")
    print("  [5] Shut Down")
    print("=" * 42)


def temperature_status(temp):
    if temp < 30:
        return "NORMAL"
    elif temp <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def show_temperatures(data):
    print("\n--- TEMPERATURE LOGBOOK ---")

    if not data:
        print("No temperature records available.")
        return

    for position, temp in enumerate(data, start=1):
        print(
            f"Sensor {position:02}: {temp:3} °C"
            f" | {temperature_status(temp)}"
        )


def record_temperature(data):
    while True:
        entry = input("Enter temperature to record: ")

        if valid_integer(entry) and 0 <= int(entry) <= 100:
            data.append(int(entry))
            print("New temperature successfully recorded.")
            return

        print("Enter a whole number between 0 and 100.")


def inspect_temperatures(data):
    print("\n--- SENSOR STATUS INSPECTION ---")

    if not data:
        print("No readings available for inspection.")
        return

    for temp in data:
        status = temperature_status(temp)

        if status == "NORMAL":
            indicator = "[OK]"
        elif status == "WARNING":
            indicator = "[!]"
        else:
            indicator = "[ALERT]"

        print(f"{indicator} {temp} °C --> {status}")


def calculate_average(data):
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


def count_status(data, status):
    total = 0

    for temp in data:
        if temperature_status(temp) == status:
            total += 1

    return total


def system_condition(warnings, criticals):
    if criticals > 0:
        return "ACTION NEEDED"
    elif warnings > 0:
        return "UNDER OBSERVATION"
    else:
        return "OPERATING NORMALLY"


def generate_report(data):
    print("\n" + "=" * 42)
    print("          SYSTEM PERFORMANCE REPORT")
    print("=" * 42)

    total = sum(data)
    quantity = len(data)
    average = calculate_average(data)

    normal = count_status(data, "NORMAL")
    warning = count_status(data, "WARNING")
    critical = count_status(data, "CRITICAL")

    print(f"Total sensor records : {quantity}")
    print(f"Combined temperature : {total} °C")
    print(f"Average temperature : {average:.2f} °C")

    if quantity > 0:
        print(f"Lowest temperature  : {min(data)} °C")
        print(f"Highest temperature : {max(data)} °C")

        print("\n--- STATUS DISTRIBUTION ---")

        for label, count in [
            ("NORMAL", normal),
            ("WARNING", warning),
            ("CRITICAL", critical)
        ]:
            percentage = count / quantity * 100
            print(f"{label:<10}: {count:>3} ({percentage:.2f}%)")

    print("\n--- FINAL SYSTEM ASSESSMENT ---")
    print(f"Condition: {system_condition(warning, critical)}")
    print("=" * 42)


def main():
    readings = collect_readings()

    while True:
        show_dashboard()
        option = input("Select an operation (1-5): ")

        if option == "1":
            show_temperatures(readings)

        elif option == "2":
            record_temperature(readings)

        elif option == "3":
            inspect_temperatures(readings)

        elif option == "4":
            generate_report(readings)

        elif option == "5":
            print("\nSystem shutting down...")
            print("Thank you for using Smart Temperature Control!")
            break

        else:
            print("Invalid selection. Choose an option from 1 to 5.")


main()