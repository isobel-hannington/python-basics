# 🐍 Python basics

**Small interactive Python programs built with variables, input, type casting, conditions and loops.**

Two Google Colab notebooks from Week 6 of my bootcamp. The course set short real-world scenarios, such as a reception desk greeting or a theme park "lucky number", and I wrote every program: converters, calculators, a security keypad, a prime checker and FizzBuzz.

For the pandas notebooks from the same week, see [python-pandas-exercises](https://github.com/isobel-hannington/python-pandas-exercises).

## 🔎 At a glance

| | |
|---|---|
| **Tools** | Python 3, Google Colab |
| **Notebooks** | Day 1: Python basics (6 programs). Day 2: conditions and loops (7 programs, plus FizzBuzz) |
| **Bootcamp week** | Week 6 (October 2026), Level 3 Data Technician Skills Bootcamp, Leep Talent |
| **Type** | Scenario exercises set by the course. I wrote all the programs. |
| **Colab links** | [Day 1 notebook](https://colab.research.google.com/drive/1p4Em54cQsqtZWO4XPGt_r9U_xCQ-17oj?usp=sharing) · [Day 2 notebook](https://colab.research.google.com/drive/1Z9JhK_a0CzQt0qisn4c7vVyw05hvEM1x?usp=sharing) |

## 💡 Skills demonstrated

**✔️ Python fundamentals**
- Variables holding text, whole numbers and decimals
- `input()` to read what the user types, and `print()` with f-strings (visitor greeting)
- Type casting with `int()` and `float()` (tile calculator, temperature converter, access code)
- Formatting numbers with `:.2f` (the tile cost)
- Arithmetic, including floor division (`//`) and modulus (`%`)

**✔️ Control flow**
- `if`, `elif` and `else` with comparisons and `and` (access code check, divisibility checker, FizzBuzz)
- `for` loops with `range()` (factorial, FizzBuzz), including `for` with `else` (prime checker) and nested `for` loops (number staircase)
- A `while` loop with a counter (keypad that locks after three wrong codes)
- `while True` with `break` and `continue` (menu calculator)

**✔️ Problem-solving and logic**
- Turning a written scenario into step-by-step logic (every program)
- Splitting a number into its digits with `//` and `%` (lucky number, four-digit reverser)
- Guarding against wrong input: a limit on attempts, an invalid menu choice and a divide-by-zero check (keypad, menu calculator)

## 📗 Exercises covered

| Notebook | What I built |
|---|---|
| [Day 1: Python basics](notebooks/day1-python-basics.ipynb) | A visitor greeting, a tile area and cost calculator, a temperature converter, a miles and kilometres converter, a digit-sum "lucky number" and a four-digit reverser |
| [Day 2: conditions and loops](notebooks/day2-conditions-and-loops.ipynb) | A keypad that locks after three wrong codes, a divisibility checker, a menu calculator, a sum of 1 to n, a prime checker, a factorial calculator, a number staircase and FizzBuzz |

## 🧩 Code highlights

### Variables, `input()` and `print()`

![Greeting program](images/01-greeting-input-print.png)

`input()` stores each answer in a variable, and an f-string drops both into one `print()` message.

### Type casting and calculations

![Tile calculator](images/02-tile-calculator.png)

`input()` always returns text, so `float()` converts each answer before the maths. `:.2f` formats the cost as money: £117.60 for a 3.5m by 2.8m kitchen.

### Floor division and modulus

![Lucky number and reverser](images/04-floor-division-modulus.png)

`//` drops the remainder and `%` keeps it, so together they split a number into its digits: 258 gives a lucky number of 15, and 2587 reverses to 7852.

### A `while` loop with a counter

![Three attempts](images/06-three-attempts-while-loop.png)

The loop keeps asking while there are attempts left and the code is wrong. `int()` turns each typed code into a number to compare with 123, `count` goes up after each wrong code, and the alert follows three failures.

### `while True`, `break` and `continue`

![Menu calculator](images/07-menu-calculator.png)

The menu repeats until the user picks 5 and `break` ends the loop. An invalid choice triggers `continue`, and an `if` checks for zero before dividing so the program can't crash.

### A `for` loop with `break` and `else`

![Prime checker](images/08-prime-checker.png)

The loop stops at the first number that divides exactly. The `else` only runs if no divisor was found, which means the number is prime. I tested six numbers: 7 is prime, and 767 isn't (it's 13 × 59).

### Nested `for` loops

![Number staircase](images/09-staircase-nested-loops.png)

The outer loop counts the rows and the inner loop prints each row's numbers, so every line is one number longer than the last.

### FizzBuzz

![FizzBuzz code](images/10-fizzbuzz.png)

Print 1 to 100, with "fizz" for multiples of 3, "buzz" for multiples of 5 and "fizzbuzz" for both. Checking for "both" first matters: otherwise 15 would print "fizz" and never reach "fizzbuzz".

## 🎓 Key learning outcomes

- Cast input before calculating, because `input()` always returns text.
- Put conditions in order from most to least specific, as in FizzBuzz.
- Test with several inputs, not just one.

## 🧠 What I'd change

- **Format numbers for people.** The tile area prints as 9.799999999999999. Using `:.2f`, as I did for the cost, would show 9.80.
- **Check input before converting it.** A word typed where a number is expected makes `int()` stop with an error. Wrapping it in `try` and `except` would let the program ask again.

## 🛠️ Tools and technologies

- **Python 3:** every program in both notebooks
- **Google Colab:** writing and running the notebooks, and sharing them by link

## 📁 Repository contents

| File or folder | What it is |
|---|---|
| `Data_Technician_Workbook_Week_6.docx` | My completed Week 6 workbook, with the Colab link for each notebook and my FizzBuzz code and output |
| `notebooks/` | The Day 1 and Day 2 notebooks, downloaded from Colab with their output saved |
| `fizzbuzz/fizzbuzz.py` | FizzBuzz as a standalone script |
| `images/` | Screenshots of code and output from the notebooks |
