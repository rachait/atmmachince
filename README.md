# ATM Program

This is a simple Python-based ATM simulation program that allows users to perform basic banking operations such as withdrawing money, depositing money, checking balance, and viewing transaction history. The program is designed to be user-friendly and incorporates error handling to ensure a smooth user experience. It also uses `numpy` to manage transaction histories.

## Features

- **Withdraw:** Withdraw a specified amount of money from your account.
- **Deposit:** Deposit a specified amount of money into your account.
- **Check Balance:** View your current account balance.
- **Transaction History:** View a history of your transactions, including deposits and withdrawals.
- **Exit:** Safely exit the ATM program.

## Requirements

- Python 3.x
- `numpy` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/atm-program.git
    cd atm-program
    ```

2. **Install the required dependencies:**

    Ensure you have Python 3 and `numpy` installed. You can install `numpy` using pip:

    ```bash
    pip install numpy
    ```

3. **Run the program:**

    ```bash
    python atm_program.py
    ```

## Usage

When you run the program, you will be prompted to enter your account name. The ATM will then provide you with a set of options to perform banking operations:

1. **WITHDRAW:** Allows you to withdraw money from your account. If you try to withdraw more than your current balance, you will receive an "Insufficient funds" message.
2. **DEPOSIT:** Allows you to deposit money into your account. The deposited amount is added to your current balance.
3. **BALANCE:** Displays your current account balance.
4. **TRANSACTION HISTORY:** Displays a list of all transactions (both deposits and withdrawals) in the order they occurred.
5. **EXIT:** Exits the program.

The program also warns you if your balance falls below $5000 after any transaction.

## Code Structure

- **atm_program.py:** The main file containing all the logic for the ATM operations.
- **README.md:** This file, which provides an overview of the project.

