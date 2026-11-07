# CodeAlpha_StockPortfolioTracker

A simple stock portfolio tracker built for the CodeAlpha Python Programming Internship (Task 2).

## Features
- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN)
- User enters stock names and quantities
- Input validation for unknown stocks and invalid quantities
- Displays each holding and the total investment value
- Optionally saves the result to `portfolio.txt`

## How to Run
1. Install Python 3 from python.org
2. Download `stock_tracker.py`
3. Open a terminal in the file's folder and run:
```
python stock_tracker.py
```

## Example
```
Enter stock name (or 'done' to finish): AAPL
Enter quantity of AAPL: 3
Enter stock name (or 'done' to finish): MSFT
Enter quantity of MSFT: 2
Enter stock name (or 'done' to finish): done

--- Portfolio Summary ---
AAPL: 3 x $180 = $540
MSFT: 2 x $330 = $660
Total Investment: $1200
```

## Concepts Used
Dictionary, input/output, basic arithmetic, file handling

## Author
Areeba Saman
