# 🔐 Python Brute Force Password Cracker

A Python-based brute-force password cracking program designed to demonstrate how password guessing works through automated character combinations.

## 📌 About the Project

The **Python Brute Force Password Cracker** is an educational Python project that demonstrates the concept of brute-force password attacks.

The program prompts the user to enter a password and systematically generates possible character combinations until it finds a matching password.

It also calculates the number of guesses generated and measures the execution time.

🎯 This project highlights the importance of strong passwords and introduces fundamental cybersecurity concepts.

## ✨ Features

- 🔑 **Automated Password Guessing:** Generates possible password combinations automatically.
- 🔤 **Character Combinations:** Uses lowercase letters, numbers, and special characters.
- 🔢 **Guess Counter:** Displays the number of generated guesses.
- ⏱️ **Execution Time:** Measures and displays how long the program takes to run.
- 🐍 **Simple Implementation:** Developed using Python's built-in libraries.

## 🛠️ Technologies Used

- 🐍 Python 3
- ⏳ Python `time` module

## 📂 Project Structure

```text
Python-Brute-Force-Password-Cracker/
│
├── Main.py
├── README.md
└── LICENSE
```

## ⚙️ Getting Started

Follow these steps to run the project locally.

### Prerequisites

You will need:

Python & Git installed on your computer.

A code editor such as Visual Studio Code.

### 1️⃣ Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/BJomo001/Python-Brute-Force-Password-Cracker.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Python-Brute-Force-Password-Cracker
```

### 3️⃣ Run the Program

Execute the following command:

```bash
python Main.py
```

Alternatively, use:

```bash
python3 Main.py
```

## 💻 How It Works

1. 🔐 The program prompts the user to enter a password.
2. 🔤 It initializes a character set containing lowercase letters, numbers, and special characters.
3. 🔄 It generates possible character combinations, increasing their length.
4. 🎯 It compares generated combinations against the entered password.
5. 📊 It displays the number of guesses and total execution time.

## 📸 Example Output

```text
Please enter your password: abc

abc : 123 Guesses

Runtime: 0.002 seconds
```

*Note: This output is illustrative. Actual results depend on the entered password and execution environment.*

## ⚠️ Important Notes

- 🔡 The current implementation generates combinations using lowercase letters, numbers, and special characters.
- 🔠 Uppercase letters are defined in the source code but are not currently included in the combination set.
- 📏 The search is limited to password combinations of up to 12 characters.
- 💾 Generating and storing large numbers of combinations can consume significant memory and processing time.

## 🎓 Learning Objectives

Through this project, you will explore:

- 🐍 Basic Python programming.
- 🔁 Loops and list comprehensions.
- 📝 String manipulation.
- 🔐 Brute-force algorithms.
- 🛡️ Cybersecurity fundamentals.
- ⏱️ Measuring program execution time.

## 🛡️ Security and Ethical Use

This project is developed strictly for educational purposes and authorized cybersecurity learning.

It should only be used in controlled environments and for testing passwords that you own or have explicit permission to assess.

🚫 Never use brute-force techniques to gain unauthorized access to systems, accounts, or networks.

## 🚀 Future Improvements

Potential enhancements include:

- 🔠 Adding uppercase letters to the character set.
- ⚡ Improving memory efficiency and execution speed.
- 📏 Implementing customizable password-length options.
- 📊 Displaying real-time guessing progress.
- 🔍 Supporting alternative password-generation strategies.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

## 👨‍💻 Author

**BJomo001**

🐙 GitHub: [@BJomo001](https://github.com/BJomo001)

---

⭐ If you find this project interesting, consider giving the repository a star!

🔐 *Learning Python. Exploring Cybersecurity. Building Secure Systems.*
