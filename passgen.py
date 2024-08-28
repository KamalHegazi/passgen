from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from datetime import datetime
import argparse
import secrets


# Define character sets
CHAR_SETS = {
    'upper': ascii_uppercase,
    'lower': ascii_lowercase,
    'digits': digits,
    'symbols': punctuation
}


def generate_pass(length: int, use_upper: bool, use_lower: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generate a secure password.

    :param length: Length of the password.
    :param use_upper: Include uppercase letters.
    :param use_lower: Include lowercase letters.
    :param use_digits: Include digits.
    :param use_symbols: Include symbols.
    :param output: Output the generated password to file.
    :return: Generated password.
    """

    chars = ''

    if use_upper:
        chars += CHAR_SETS['upper']

    if use_lower:
        chars += CHAR_SETS['lower']

    if use_digits:
        chars += CHAR_SETS['digits']

    if use_symbols:
        chars += CHAR_SETS['symbols']

    if not chars:
        raise ValueError("Error: At least one character set must be selected.")


    # Ensure at least one character from each selected set is included
    password = []

    if use_upper:
        password.append(secrets.choice(CHAR_SETS['upper']))

    if use_lower:
        password.append(secrets.choice(CHAR_SETS['lower']))

    if use_digits:
        password.append(secrets.choice(CHAR_SETS['digits']))

    if use_symbols:
        password.append(secrets.choice(CHAR_SETS['symbols']))


    # Fill the rest of the password length with random choices
    while len(password) < length:
        password.append(secrets.choice(chars))

    # Shuffle the password list to ensure randomness
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)


def log_message(level: str, message: str) -> None:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{timestamp} - {level} - {message}")


def main() -> None:
    parser = argparse.ArgumentParser(description='Welcome! This tool helps you create strong, random passwords to enhance your security.')
    
    parser.add_argument('--length', '-l', type=int, default=16, dest='length',
                        help="Define the length of the passphrase (16 by default)")
    parser.add_argument('--no-upper', action='store_false', dest='use_upper',
                        help="Exclude uppercase letters from the passphrase")
    parser.add_argument('--no-lower', action='store_false', dest='use_lower',
                        help="Exclude lowercase letters from the passphrase")
    parser.add_argument('--no-digits', action='store_false', dest='use_digits',
                        help="Exclude digits from the passphrase")
    parser.add_argument('--no-symbols', action='store_false', dest='use_symbols',
                        help="Exclude symbols from the passphrase")
    parser.add_argument('--output', '-o', type=str,
                        help="Output the generated password to a text file")

    args = parser.parse_args()
    length = args.length

    

    if length <= 0:
        log_message("ERROR", "Error: Length must be a positive integer.")

        return

    try:
        password = generate_pass(length, args.use_upper, args.use_lower, args.use_digits, args.use_symbols)
        log_message("INFO", f"Generated password: {password}")

        if args.output:
            with open(args.output, 'a') as file:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{timestamp} - {password}\n")
            log_message("INFO", f"Password written to {args.output}")

    except ValueError as e:
        log_message("ERROR", str(e))


if __name__ == "__main__":

    main()
