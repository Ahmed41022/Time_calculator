def get_amount():
    """Prompt the user to enter the amount and convert it to a float."""
    try:
        amount = float(input("Enter amount: "))
        return amount
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
        exit()

def get_currency():
    """Prompt the user to enter the currency type and validate it."""
    currency = input("Enter Currency, EGP or USD: ").strip().upper()
    if currency not in ["EGP", "USD"]:
        print("Invalid input. Please enter either 'EGP' or 'USD' for the currency.")
        exit()
    return currency

def convert_currency(amount, currency):
    """Convert the amount to EGP if the currency is USD."""
    if currency == 'USD':
        amount = amount * 49
    return amount

def calculate_time(amount):
    """Calculate the time based on the amount of money."""
    time_hours = int(amount // 100)
    time_mins = int((amount % 100) * 0.6)
    return time_hours, time_mins

def main():
    """Main function to execute the script."""
    money = get_amount()
    currency = get_currency()
    money = convert_currency(money, currency)
    time_hours, time_mins = calculate_time(money)

    print(f"Amount: {money} {currency}")
    print(f"Time: {time_hours} hours and {time_mins} minutes")

if __name__ == "__main__":
    main()
