# 🔐 Passgen
Welcome! This tool helps you create strong, random passwords to enhance your security. It’s built with Python and leverages the secrets module for cryptographic randomness.

# 🚀 Features
- **Customizable Length:** Define the length of your password.

- **Character Sets:** Choose to include/exclude uppercase letters, lowercase letters, digits, and symbols.

- **Secure:** Uses the secrets module for generating cryptographically secure passwords.

- **Logging:** Provides informative logging to track the password generation process.

- **Output the generated password to a file**

# 🛠️ Installation
Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/yourusername/secure-password-generator.git
cd secure-password-generator
```

Setup the tool by running the `setup.sh` as following:
```sh
chmod +x setup.sh & sudo ./setup.sh
```


# 📦 Usage
Run the script with the desired options:

**Command-Line Options:**

- `--length` or `-l`: Define the length of the password (default is 16).
- `--no-upper`: Exclude uppercase letters from the password.
- `--no-lower`: Exclude lowercase letters from the password.
- `--no-digits`: Exclude digits from the password.
- `--no-symbols`: Exclude symbols from the password.
- `--output` or `-o`: Output the generated password to a text file.

# 🧩 Example
Generate a 20-character password without uppercase letters and digits:

```sh
passgen --length 20 --no-symbols --output passwords.txt
```

# 📜 License
This project is licensed under the GNU General Public License v2.0 License. See the LICENSE file for details.

# 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

# 📧 Contact
For any inquiries, please contact : `kamalhegazi05@gmail.com`
