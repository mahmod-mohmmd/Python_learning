# 🏦 Bank Account Management System

A comprehensive Python-based bank account management system with a command-line interface. This project demonstrates fundamental programming concepts including user authentication, data management, and transaction processing.

---

## 📋 Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Technical Details](#technical-details)
- [Future Enhancements](#future-enhancements)

---

## ✨ Features

### 🔐 Authentication
- **User Registration**: Create a new account with username and secure password (minimum 6 characters)
- **User Login**: Secure authentication with 3 login attempts limit
- **Password Management**: Change password with old password verification

### 💰 Banking Operations
- **Check Balance**: View your current account balance in EGP (Egyptian Pound)
- **Deposit**: Add funds to your account with validation
- **Withdraw**: Withdraw money with balance verification
- **Transfer**: Send money to other registered users securely
- **Logout**: Secure session termination

---

## 📸 Screenshots

### Main Menu
```
1. Enter To Program
2. Exit
```

### Authentication Menu
```
=============================================
========== Welcom To Python Bank ============
=============================================
 1. Register
 2. Login
 3. Exit
```

### Bank Operations Menu
```
================================
========== Bank Menue ==========
================================
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Change Password
6. Logout
7. Main Menue
```

---

## 🗂️ Project Structure

```
Projects/02/
│
├── Bank_Account_Management_System.py  # Main application file
└── README.md                           # This file
```

---

## 📦 Requirements

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

---

## 🚀 Installation

### Option 1: Clone the Repository
```bash
git clone https://github.com/mahmod-mohmmd/Python_learning.git
cd Python_learning/Projects/02/
```

### Option 2: Download Directly
Download the `Bank_Account_Management_System.py` file from the repository.

---

## ▶️ How to Run

1. **Open terminal/command prompt**

2. **Navigate to the project directory:**
   ```bash
   cd Python_learning/Projects/02/
   ```

3. **Run the program:**
   ```bash
   python Bank_Account_Management_System.py
   ```
   or
   ```bash
   python3 Bank_Account_Management_System.py
   ```

4. **Follow the on-screen prompts** to perform banking operations

---

## 📖 Usage Guide

### Step 1: Start the Program
```
1. Enter To Program
2. Exit
Choice (1/2): 1
```

### Step 2: Register or Login
```
1. Register
2. Login
3. Exit
Choice (1/2/3): 1
```

### Step 3: Registration
- Enter your username (will be capitalized)
- Create a password (minimum 6 characters)
- Confirm registration

### Step 4: Login
- Enter your username
- Enter your password
- You have 3 attempts maximum

### Step 5: Banking Operations
Once logged in, choose from:

| Option | Operation | Description |
|--------|-----------|-------------|
| 1 | Check Balance | View your current balance |
| 2 | Deposit | Add money to your account |
| 3 | Withdraw | Withdraw money from your account |
| 4 | Transfer | Send money to another user |
| 5 | Change Password | Update your account password |
| 6 | Logout | Exit your account |
| 7 | Main Menue | Return to main menu |

### Example Workflow

```
START
  ↓
Enter Program (1)
  ↓
Register New Account
  ↓
Login with Credentials
  ↓
Perform Banking Operations (Deposit, Withdraw, Transfer, etc.)
  ↓
Logout (6)
  ↓
Exit Program (2)
  ↓
END
```

---

## 🔧 Technical Details

### Code Architecture

**Main Functions:**

| Function | Purpose |
|----------|---------|
| `main()` | Entry point of the application |
| `mainManue()` | Authentication menu |
| `bankMenue()` | Main banking operations menu |
| `Register()` | User registration logic |
| `Login()` | User authentication |
| `checkBalance()` | Display account balance |
| `deposit()` | Handle deposit operations |
| `withdraw()` | Handle withdrawal operations |
| `transfer()` | Handle money transfer between users |
| `changePassword()` | Update user password |
| `logout()` | End user session |

### Data Storage

```python
users = {
    "Username": {
        "Password": "password123",
        "Balance": 5000
    }
}
```

**Key Points:**
- Data stored in dictionary (volatile - lost on exit)
- Single global `userName` variable tracks current user
- No database persistence

### Validation

- ✅ Username uniqueness checked
- ✅ Password minimum length (6 characters)
- ✅ Login attempts limited (3 tries)
- ✅ Withdrawal amount verified against balance
- ✅ Transfer recipient existence verified
- ✅ Self-transfer prevented

---

## 🎯 Currency

- **Currency**: EGP (Egyptian Pound)
- All amounts are displayed in EGP format

---

## 🚀 Future Enhancements

### Short Term
- [ ] Add persistent data storage (JSON file)
- [ ] Implement transaction history
- [ ] Add transaction receipt printing
- [ ] Email confirmation for transfers

### Medium Term
- [ ] Add password hashing (security improvement)
- [ ] Create GUI with Tkinter or PyQt
- [ ] Add account recovery functionality
- [ ] Implement admin panel

### Long Term
- [ ] Migrate to database (SQLite/MySQL)
- [ ] Add web interface (Flask/Django)
- [ ] Implement REST API
- [ ] Add multi-factor authentication (MFA)
- [ ] Banking fee calculations
- [ ] Loan and investment features

---

## ⚠️ Important Notes

### Current Limitations

1. **Data Loss**: All user data is lost when the program exits
   - Solution: Save to JSON or database file

2. **No Password Encryption**: Passwords are stored in plain text
   - Solution: Implement password hashing (use `hashlib` or `bcrypt`)

3. **No Transaction History**: Only current balance is tracked
   - Solution: Maintain transaction log

4. **Single User Session**: Only one user can be logged in at a time
   - Solution: Implement multi-user concurrent sessions

### Security Recommendations

- Use password hashing for production
- Implement proper session management
- Add role-based access control
- Use HTTPS if converted to web application
- Add logging for all transactions

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests with improvements!

### Suggested Improvements
- Add more banking features
- Improve error handling
- Optimize code structure
- Add comprehensive unit tests
- Refactor with object-oriented programming (OOP)

---

## 📝 License

This project is open source and available for educational purposes.

---

## 👨‍💻 Author

Created by **mahmod-mohmmd** as a Python learning project

---

## 📧 Support

For issues or questions about this project, please open an issue on GitHub.

---

## ⭐ If You Found This Helpful

Please consider giving this repository a star ⭐ on GitHub!

---

**Last Updated**: 2026  
**Status**: Active Development
