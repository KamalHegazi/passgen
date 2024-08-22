import argparse
import secrets
import logging

# Define character sets
CHAR_SETS = {
    'upper': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    'lower': "abcdefghijklmnopqrstuvwxyz",
    'digits': "0123456789",
    'symbols': "~`!@#$%^&*)}(]{[|/?><.,-_+=';:"
}

def generate_pass(length: int, use_upper: bool, use_lower: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generate a secure password.

    :param length: Length of the password.
    :param use_upper: Include uppercase letters.
    :param use_lower: Include lowercase letters.
    :param use_digits: Include digits.
    :param use_symbols: Include symbols.
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
    password = [secrets.choice(chars) for _ in range(length)]
    if use_upper:
        password[0] = secrets.choice(CHAR_SETS['upper'])
    if use_lower:
        password[1] = secrets.choice(CHAR_SETS['lower'])
    if use_digits:
        password[2] = secrets.choice(CHAR_SETS['digits'])
    if use_symbols:
        password[3] = secrets.choice(CHAR_SETS['symbols'])
    
    # Shuffle the password list to ensure randomness
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    parser = argparse.ArgumentParser(description='Passphrase generator tool')
    parser.add_argument('--length', '-l', type=int, default=16,
                        help="Define the length of the passphrase (16 by default)")
    parser.add_argument('--no-upper', action='store_false', dest='use_upper',
                        help="Exclude uppercase letters from the passphrase")
    parser.add_argument('--no-lower', action='store_false', dest='use_lower',
                        help="Exclude lowercase letters from the passphrase")
    parser.add_argument('--no-digits', action='store_false', dest='use_digits',
                        help="Exclude digits from the passphrase")
    parser.add_argument('--no-symbols', action='store_false', dest='use_symbols',
                        help="Exclude symbols from the passphrase")
    
    args = parser.parse_args()
    length = args.length
    
    if length <= 0:
        logging.error("Error: Length must be a positive integer.")
        return
    
    try:
        password = generate_pass(length, args.use_upper, args.use_lower, args.use_digits, args.use_symbols)
        logging.info(f"Generated password: {password}")
    except ValueError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
