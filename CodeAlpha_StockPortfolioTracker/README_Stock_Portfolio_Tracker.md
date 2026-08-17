# Stock Portfolio Tracker

A simple, professional command-line Stock Portfolio Tracker built with Python. The program allows users to select stocks from a predefined price list, enter quantities, calculate investment values, display a portfolio summary, and optionally export the results to TXT or CSV format.

## Features

- Displays a predefined list of available stocks and prices.
- Accepts stock symbols and share quantities from the user.
- Validates stock symbols and quantities.
- Calculates the value of each stock holding.
- Displays a formatted portfolio summary.
- Calculates total investment value.
- Exports portfolio data to:
  - TXT
  - CSV
- Automatically adds a timestamp to exported filenames.
- Uses Python's built-in `csv` module for CSV file handling.
- Uses `datetime` for timestamp generation.

## Supported Stocks

The tracker currently uses the following hardcoded stock prices:

| Symbol | Price |
|---|---:|
| AAPL | $180.00 |
| TSLA | $250.00 |
| GOOG | $140.00 |
| AMZN | $145.00 |
| MSFT | $410.00 |
| NFLX | $650.00 |
| META | $480.00 |

> **Note:** These prices are sample/static values and are not live market prices.

## Technologies Used

- **Python 3**
- `csv` — CSV file creation
- `datetime` — Timestamp generation
- Dictionaries — Stock-price storage
- Lists — Portfolio data storage
- Functions — Modular program structure
- File handling — TXT and CSV export
- Basic arithmetic — Investment calculations

## Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
└── README.md
```

## Requirements

- Python 3.x
- No external Python packages are required.

## How to Run

1. Install Python 3 if it is not already installed.
2. Save the program as:

```text
stock_portfolio_tracker.py
```

3. Open a terminal in the project directory.
4. Run:

```bash
python stock_portfolio_tracker.py
```

On some systems, you may need:

```bash
python3 stock_portfolio_tracker.py
```

## How to Use

### Step 1: View Available Stocks

When the program starts, it displays the available stock symbols and their sample prices.

### Step 2: Enter Stock Details

Enter a valid stock symbol, such as:

```text
AAPL
```

Then enter the number of shares:

```text
Quantity of AAPL: 5
```

The program calculates the holding value automatically:

```text
5 shares × $180.00 = $900.00
```

### Step 3: Add More Stocks

Continue entering stocks until you are finished.

To stop entering stocks, type:

```text
done
```

The program accepts `done` regardless of capitalization because input is converted to uppercase.

### Step 4: Review the Portfolio

The program displays a summary containing:

- Stock symbol
- Quantity
- Price per share
- Holding value
- Total investment value

### Step 5: Export Results

If a portfolio has been entered, the program asks:

```text
Save results to a file? (y/n):
```

If you select `y`, choose either:

```text
txt
```

or:

```text
csv
```

The exported file includes a timestamp, for example:

```text
portfolio_2026-08-17_10-30-00.csv
```

## Example

```text
==================================================
        STOCK PORTFOLIO TRACKER
==================================================

Available stocks:
----------------------------
  AAPL     $180.00
  TSLA     $250.00
  GOOG     $140.00
  AMZN     $145.00
  MSFT     $410.00
  NFLX     $650.00
  META     $480.00
----------------------------

Stock symbol: AAPL
Quantity of AAPL: 5

>> Added: 5 share(s) of AAPL @ $180.00 = $900.00

Stock symbol: MSFT
Quantity of MSFT: 2

>> Added: 2 share(s) of MSFT @ $410.00 = $820.00

Stock symbol: done

==================================================
           PORTFOLIO SUMMARY
==================================================
Symbol    Qty     Price       Value
--------------------------------------------------
AAPL      5       $180.00     $900.00
MSFT      2       $410.00     $820.00
--------------------------------------------------
TOTAL INVESTMENT VALUE: $1,720.00
==================================================
```

## Input Validation

The program handles common invalid inputs:

- Unknown stock symbols are rejected.
- Zero quantities are rejected.
- Negative quantities are rejected.
- Non-numeric quantities are rejected.
- Invalid export formats are rejected.

Example:

```text
>> 'XYZ' not found in price list. Please choose from the available stocks.
```

## Calculation Logic

For each stock:

```text
Investment Value = Stock Price × Quantity
```

The total portfolio value is:

```text
Total Investment Value = Sum of all individual stock values
```

## File Output

### TXT Format

The TXT export creates a readable portfolio report containing the stock details and total investment value.

### CSV Format

The CSV export creates structured data that can be opened in:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc
- Other spreadsheet applications

## Limitations

This project is intentionally designed as a beginner-friendly portfolio tracker.

- Stock prices are hardcoded.
- Prices are not retrieved from a live stock market API.
- There is no database integration.
- The program does not track profit/loss.
- The program does not store historical transactions.
- The program does not include brokerage fees or taxes.
- The program is command-line based.

## Possible Future Improvements

The project can be extended with:

1. Live stock prices using a financial API.
2. Buy and sell transaction tracking.
3. Profit and loss calculations.
4. Portfolio performance charts.
5. Persistent storage using SQLite or another database.
6. User accounts and authentication.
7. A graphical user interface.
8. A web-based dashboard.
9. Support for multiple currencies.
10. Automatic portfolio valuation updates.

## Learning Objectives

This project demonstrates practical use of:

- Dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- String formatting
- Input validation
- Arithmetic operations
- File handling
- CSV writing
- Date and time formatting
- Modular Python programming

## License

This project is intended for educational and personal use. You may modify and extend the source code for learning and development purposes.

## Author

**Stock Portfolio Tracker**

A beginner-friendly Python project demonstrating basic programming, data handling, calculations, and file management.
