#!/usr/bin/python3

class pw_gen:
    def __init__(self):
        self.list_of_characters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            0 , 1, 2, 3, 4, 5, 6, 7, 8, 9,
            '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
            '_', '+', '=', '{', '}', '[', ']', '\'', '|', ',', '<', '.', '>',
            '?', '/'
        ]

    def read_bytes(self, dev_random, rounds):
        i = 0
        data_bytes = None
        while i < rounds:
            data_bytes = dev_random.read(32)
            i += 1
        return data_bytes

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

        print("password is :" + password)

if __name__ == "__main__":
    pw_gen = pw_gen()
    pw_gen.generate(True, 20, store=True)
