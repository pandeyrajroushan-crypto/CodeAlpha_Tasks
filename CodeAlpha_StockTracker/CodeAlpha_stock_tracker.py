"""
Simple Stock Portfolio Tracker
Key concepts: dictionary, input/output, basic arithmetic, file handling
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in dollars)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 145,
    "MSFT": 410,
    "NFLX": 650,
    "META": 480,
}


def show_available_stocks():
    """Display the list of stocks and their prices."""
    print("\nAvailable stocks:")
    print("-" * 28)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price:,.2f}")
    print("-" * 28)


def get_portfolio_input():
    """Collect stock symbols and quantities from the user."""
    portfolio = []  # list of dicts: {"symbol": ..., "quantity": ..., "price": ..., "value": ...}

    print("\nEnter stock symbol and quantity (type 'done' as symbol to finish).")

    while True:
        symbol = input("\nStock symbol: ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f">> '{symbol}' not found in price list. Please choose from the available stocks.")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()

        if not qty_input.isdigit() or int(qty_input) <= 0:
            print(">> Please enter a valid positive whole number for quantity.")
            continue

        quantity = int(qty_input)
        price = STOCK_PRICES[symbol]
        value = price * quantity

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value
        })

        print(f">> Added: {quantity} share(s) of {symbol} @ ${price:,.2f} = ${value:,.2f}")

    return portfolio


def display_summary(portfolio):
    """Print a summary table and total investment value."""
    if not portfolio:
        print("\nNo stocks entered. Nothing to summarize.")
        return 0

    print("\n" + "=" * 50)
    print("           PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"{'Symbol':<10}{'Qty':<8}{'Price':<12}{'Value':<12}")
    print("-" * 50)

    total_value = 0
    for entry in portfolio:
        print(f"{entry['symbol']:<10}{entry['quantity']:<8}"
              f"${entry['price']:<11,.2f}${entry['value']:<11,.2f}")
        total_value += entry["value"]

    print("-" * 50)
    print(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}")
    print("=" * 50)

    return total_value


def save_to_file(portfolio, total_value):
    """Optionally save the portfolio summary to a .txt or .csv file."""
    choice = input("\nSave results to a file? (y/n): ").lower().strip()

    if choice != "y":
        return

    file_format = input("Choose format - txt or csv: ").lower().strip()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if file_format == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for entry in portfolio:
                writer.writerow([entry["symbol"], entry["quantity"], entry["price"], entry["value"]])
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total_value])
        print(f">> Saved to {filename}")

    elif file_format == "txt":
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 50 + "\n")
            f.write(f"{'Symbol':<10}{'Qty':<8}{'Price':<12}{'Value':<12}\n")
            f.write("-" * 50 + "\n")
            for entry in portfolio:
                f.write(f"{entry['symbol']:<10}{entry['quantity']:<8}"
                        f"${entry['price']:<11,.2f}${entry['value']:<11,.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"TOTAL INVESTMENT VALUE: ${total_value:,.2f}\n")
        print(f">> Saved to {filename}")

    else:
        print(">> Unrecognized format. Skipping save.")


def main():
    print("=" * 50)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    show_available_stocks()
    portfolio = get_portfolio_input()
    total_value = display_summary(portfolio)

    if portfolio:
        save_to_file(portfolio, total_value)

    print("\nThanks for using the Stock Portfolio Tracker. Goodbye!")


if __name__ == "__main__":
    main()
