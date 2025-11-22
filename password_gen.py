#!/usr/bin/python3

import argparse

class pw_gen:
    def __init__(self):
        self.special_chars = [
            '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
            '_', '+', '=', '{', '}', '[', ']', '\'', '|', ',', '<', '.', '>',
            '?', '/'
        ]
        self.english_letters_numbers = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            0 , 1, 2, 3, 4, 5, 6, 7, 8, 9,
        ]
        self.list_of_characters = self.english_letters_numbers + self.special_chars

    def read_bytes(self, dev_random, rounds):
        i = 0
        data_bytes = None
        while i < rounds:
            data_bytes = dev_random.read(32)
            i += 1
        return data_bytes

    def has_atleast_n_special_chars(self, password, pw_len):
        count = 0
        n = pw_len / 3
        for pw_item in password:
            if pw_item in self.special_chars:
                count += 1
        if count < n:
            return False

        return True

    def generate(self, slow_mode, pw_len, store=True):
        password = ""
        dev_random = open("/dev/random", 'rb')
        i = 0
        rounds = 0
        while i < pw_len:
            if slow_mode:
                rounds = 32

            data_bytes = self.read_bytes(dev_random, rounds)
            int_val = int.from_bytes(data_bytes, byteorder='big', signed=False)
            index = int_val % len(self.list_of_characters)
            password += str(self.list_of_characters[index])
            i += 1

        if self.has_atleast_n_special_chars(password, pw_len):
            print("need to regen.. weak password")
            return (password, False)

        return (password, True)

if __name__ == "__main__":
    cmdargs = argparse.ArgumentParser(description="Password Generator")
    cmdargs.add_argument('-l', '--password_len', type=int, default=16, help="Length of password")
    args = cmdargs.parse_args()
    password = ""

    if args.password_len < 10:
        print("password length is below 10 characters! Please for the generation use anything above 10")
        exit(100)

    pw_gen = pw_gen()
    while True:
        password, res = pw_gen.generate(True, args.password_len, store=True)
        if res == True:
            break

    print("password is :" + password)
