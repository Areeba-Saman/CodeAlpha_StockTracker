
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_quantity(symbol):
    """Keep asking until the user enters a valid positive whole number."""
    while True:
        value = input(f"Enter quantity of {symbol}: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Please enter a whole number greater than 0.")


def save_to_file(portfolio, total):
    """Save the portfolio summary to a .txt file."""
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("=" * 40 + "\n")
        for symbol, quantity, price, value in portfolio:
            file.write(f"{symbol}: {quantity} x ${price} = ${value}\n")
        file.write("=" * 40 + "\n")
        file.write(f"Total Investment: ${total}\n")
    print("Portfolio saved to portfolio.txt")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = []   # list of (symbol, quantity, price, value)
    total = 0

    while True:
        symbol = input("Enter stock name (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Stock not found. Please choose from the available stocks.")
            continue

        quantity = get_quantity(symbol)
        price = STOCK_PRICES[symbol]
        value = price * quantity
        portfolio.append((symbol, quantity, price, value))
        total += value
        print(f"Added {quantity} x {symbol} = ${value}\n")

    if not portfolio:
        print("No stocks entered. Goodbye!")
        return

    print("\n--- Portfolio Summary ---")
    for symbol, quantity, price, value in portfolio:
        print(f"{symbol}: {quantity} x ${price} = ${value}")
    print(f"Total Investment: ${total}")

    choice = input("\nSave result to a file? (y/n): ").strip().lower()
    if choice == "y":
        save_to_file(portfolio, total)


if __name__ == "__main__":
    main()