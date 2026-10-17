# py_project.7----Moduler-Packger

# 🧰 Multi-Utility Toolkit

### PR. 7 – Moduler & Packager | Python Modules & Packages Project

A menu-driven, Python-based toolkit that brings together **standard modules**, **custom modules** and **packages** to handle everyday tasks: date & time operations, maths, random data, unique IDs and file handling. The whole project is built to demonstrate Python's modular structure in a clean, practical 

CREAT BY : AYUSH JIVANI


LANGUAGE : PYTHON


EXPLAIN VIDEO LINK :https://drive.google.com/file/d/16G7XykyGZIY4XLfbBWzq9m4R1sMqMiUI/view?usp=drive_link

REPOSITORIES LINK :https://github.com/ayushjivani082/py_project.7----Moduler-Packger/tree/76aa0c737bb49ca44c4b17d9a8bc344d5dd3f243/7.%20Moduler%20%26%20Packger

---

## 📑 Table of Contents
1. [Features](#-features)
2. [Project Structure](#-project-structure)
3. [Flow of Development](#-flow-of-development)
4. [How to Run](#-how-to-run)
5. [User Guide](#-user-guide)
6. [Sample Output](#-sample-output)
7. [Concepts Demonstrated](#-concepts-demonstrated)
8. [Module-wise Description](#-module-wise-description)
9. [Real-Life Use Case](#-real-life-use-case)
10. [Error Handling](#-error-handling)
11. [Assumptions](#-assumptions)
12. [Benefits](#-benefits)

---

## ✨ Features

| # | Menu Option | What it does | Built with |
|---|---|---|---|
| 1 | **Datetime and Time Operations** | Show current date/time, find difference between two dates, format dates with `strftime`, stopwatch, countdown timer | `datetime`, `time` |
| 2 | **Mathematical Operations** | Factorial, compound interest, trigonometry (sin/cos/tan), area of geometric shapes | `math` + `shapes`, `geometry` packages |
| 3 | **Random Data Generation** | Random number, list, password, OTP, random sampling from a dataset, dice game simulation | `random`, `string` |
| 4 | **Generate Unique Identifiers (UUID)** | UUID4, invoice/record IDs, multiple UUIDs at once | `uuid` |
| 5 | **File Operations (Custom Module)** | Create, write, read and append files | custom `file_utils` |
| 6 | **Explore Module Attributes (`dir()`)** | Explore attributes of any built-in or custom module dynamically | `dir()`, `importlib` |
| 7 | **Exit** | Closes the program with a thank-you message | — |

Extra touches: a time-based greeting (Good Morning / Afternoon / Evening) and automatic **activity logging** to `toolkit_log.txt`.

---

## 📁 Project Structure


PythonProject/
│
├── main.py             → Main program (menu + program flow)
├── math_utils.py       → Math functions
├── string_utils.py     → String functions (password, OTP, UUID)
├── helper.py           → Helper functions (random data, dir() explorer)
├── greet.py            → Greeting module
├── README.md           → Project documentation
│
├── shapes/             → Package: basic shapes
│   ├── __init__.py
│   ├── circle.py
│   └── rectangle.py
│
├── utilities/          → Package: date/time & file handling
│   ├── __init__.py
│   ├── file_utils.py
│   └── date_utils.py
│
└── geometry/           → Package: advanced geometry
    ├── __init__.py
    ├── circle.py
    └── triangle.py


---

## 🔄 Flow of Development


Project Start → Requirements Analysis → Create Modules
      → Organize into Packages → Testing & Integration → Final Output


**How the program works**
1. `main.py` starts, greets the user and shows the main menu.
2. The chosen option calls the matching module or package.
3. Every module has its own menu with a **Back to Main Menu** option.
4. `__name__ == "__main__"` makes sure each file can also be run on its own.
5. `dir()` lets the user inspect any module while the program is running.
6. `__init__.py` marks each folder as a package and simplifies imports.
7. Exit (option 7) ends the program cleanly.

---

## ▶️ How to Run

**Requirements:** Python 3.6 or above. Nothing else to install.


# 1. Go to the project folder
cd PythonProject

# 2. Start the toolkit
python main.py


> On some systems use `python3 main.py`.

**Run any module on its own** (thanks to the `__name__ == "__main__"` block):

python math_utils.py
python helper.py
python utilities/date_utils.py
python shapes/circle.py


---

## 📖 User Guide

1. Run `python main.py`. The welcome banner and main menu appear.
2. Type the **number** of the option you want and press **Enter**.
3. Inside any sub-menu, choose a task, or pick **Back to Main Menu** to return.
4. **Dates** must be entered as `YYYY-MM-DD` (example: `2025-01-04`).
5. **Stopwatch:** press Enter to start, press Enter again to stop.
6. **Countdown timer:** enter the number of seconds.
7. **File operations:** create a file first, then write, read or append to it.
8. **Explore module:** type any module name, e.g. `math`, `random`, `uuid`, `string_utils`, `shapes.circle`.
9. Choose **7** from the main menu to exit.

All actions are recorded in `toolkit_log.txt` in the folder you run the program from.

---

## 🖥️ Sample Output

**Main menu**

============================
Good Morning!
Welcome to Multi-Utility Toolkit
============================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
============================
Enter your choice: 1


**Datetime and Time Operations**

Current Date and Time: 2025-01-04 10:15:30
Friendly format      : Saturday, 04 January 2025, 10:15:30 AM
============================
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days


**Mathematical Operations**

Enter a number: 5
Factorial: 120

Enter principal amount: 1000
Enter rate of interest (in %): 5
Enter time (in years): 2
Compound Interest: 1102.50
(Total amount = 1102.50, Interest earned = 102.50)

**Random Data Generation**

Enter password length: 8
Generated Password: Kd8@qzP!


**Unique Identifiers (UUID)**

Generated UUID: f47ac10b-58cc-4372-a567-0e02b2c3d479


**File Operations (Custom Module)**

Enter file name: example.txt
File created successfully!

Enter file name: example.txt
Enter data to write: This is a sample file.
Data written successfully!

Enter file name: example.txt
File Content:
This is a sample file.


**Explore Module Attributes (`dir()`)**

Enter module name to explore: math
Available Attributes in math module:
['acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'ceil', 'comb', 'copysign', 'cos', ...]


**Exit**

============================
Thank you for using the Multi-Utility Toolkit!
============================


> Values such as passwords, OTPs and UUIDs are random, so yours will differ.

---

## 🎓 Concepts Demonstrated

| Concept | Where it is used |
|---|---|
| **Built-in modules** | `datetime`, `time`, `math`, `random`, `string`, `uuid`, `os`, `sys`, `importlib` |
| **Custom modules** | `math_utils.py`, `string_utils.py`, `helper.py`, `greet.py`, `file_utils.py`, `date_utils.py` |
| **Packages** | `shapes/`, `utilities/`, `geometry/` |
| **`__init__.py`** | Marks each folder as a package and imports its modules for easy access |
| **Import styles** | `import x`, `from x import y`, `from x import y as z` |
| **Renaming with `as`** | `from shapes import circle as shape_circle` |
| **`__name__ == "__main__"`** | Every module can run on its own *and* be imported safely |
| **`dir()`** | Option 6 – dynamic module exploration |
| **Exception handling** | `try / except` for invalid input and file errors |
| **File handling** | `open()` with `x`, `w`, `r`, `a` modes and `with` statements |

---

## 🧩 Module-wise Description

| File | Purpose |
|---|---|
| `main.py` | Entry point. Shows the menu, routes choices to modules, writes logs. |
| `greet.py` | Time-based greeting, welcome and goodbye messages. |
| `math_utils.py` | Factorial, compound interest, trigonometry and the area menu (uses `shapes` and `geometry`). |
| `string_utils.py` | Random password, OTP and all UUID features. |
| `helper.py` | Random number, list, sampling, dice game, and the `dir()` module explorer. |
| `shapes/circle.py` | Circle area and circumference. |
| `shapes/rectangle.py` | Rectangle area and perimeter. |
| `geometry/circle.py` | Circle arc length and sector area. |
| `geometry/triangle.py` | Triangle area, hypotenuse and perimeter. |
| `utilities/date_utils.py` | Current date/time, date difference, `strftime` formatting, stopwatch, countdown. |
| `utilities/file_utils.py` | Create / write / read / append files and write activity logs. |

---

## 💼 Real-Life Use Case

A small business owner can use this toolkit in daily operations:

- ⏱️ Calculate working hours and deadlines with the **date/time** tools.
- 🔐 Generate **random passwords** for team members.
- 🧾 Assign **unique IDs** to invoices using UUID.
- 📝 Save notes, logs and outputs into **text files**.
- 🔍 Explore the toolkit's own capabilities using **`dir()`**.

---

## 🛡️ Error Handling

The program is designed so it **does not crash** on wrong input:

- Invalid menu choice → message shown, menu repeats.
- Wrong date format → asks again until a valid date is entered.
- Non-numeric input → friendly message instead of a traceback.
- Negative factorial, zero/negative counts → clear explanation.
- Creating an existing file / reading a missing file → handled safely.
- Unknown module name in `dir()` explorer → "Module not found" message.
- `Ctrl + C` → program stops gracefully.

---

## 📝 Assumptions

- Dates are entered in `YYYY-MM-DD` format.
- Date difference is shown in days (absolute value).
- Compound interest uses `A = P × (1 + r/100)^t`. The final amount is shown as the result (1000, 5 %, 2 years → `1102.50`), and the interest earned is shown separately.
- Trigonometric angles are entered in degrees.
- Passwords must be at least 4 characters and always contain an uppercase letter, a lowercase letter, a digit and a symbol.
- OTP is a 6-digit number.
- Random sampling uses a small built-in sample dataset of names.
- The Random menu has two extra options (sampling and dice game) before "Back", as the requirement mentions them.
- Files created through File Operations and `toolkit_log.txt` are saved in the folder from which the program is run.

---

## 🏆 Benefits

- ♻️ Better code reusability
- 🧱 Organized and maintainable code
- 👥 Easy collaboration in larger projects
- 📈 Scalable and flexible structure
- 🐞 Easier testing and debugging

---

<p align="center"><b>Better Code = Better Tomorrow</b> 🚀</p>
