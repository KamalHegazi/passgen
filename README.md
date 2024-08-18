# passgen
CLI tool that generates secure, random passphrases. It allows users to specify the desired length of the password, ensuring it meets various security requirements. The script uses Python’s built-in libraries to create a mix of uppercase and lowercase letters, digits, and special characters.

# Installation

**1. Clone the repository :** 
```
git clone https://github.com/KamalHegazi/passgen.git
```

**2. Navigate to the project directory :**
```
cd passgen
```
# Usage
<br>

| Command | Description |
| --- | --- |
| `-h / --help` | Show help menu |
| `-l / --lenght` | Define length Of the Passphrase (16 by Default) |

<br>

**- Basic usage :**
```
python passgen.py
```
**- Example output :**
```
KR^.*l*$g?F]3v*)
```
**- Save output to file :**
```
python passgen.py --length 32 > myPass.txt
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License


> [!NOTE]
> **This project is licensed under the MIT License. See the LICENSE file for details.**
