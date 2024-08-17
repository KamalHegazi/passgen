import argparse
import random
import os

random.seed(os.urandom(1024))

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*)}(]{[|/?><.,-_+=';:"


def generate_pass(length):
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description='Passphrase generator tool')
    parser.add_argument('--length', '-l', type=int, default=16,
                        help="Define length of the passphrase (16 by default)")
    args = parser.parse_args()
    length = args.length
    print(generate_pass(length))


if __name__ == "__main__":
    main()
