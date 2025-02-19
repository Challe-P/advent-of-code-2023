"""Solution for 1a"""

import aocd


def main():
    """Main function for day 1a of 2023"""
    data = aocd.get_data(day=1, year=2023).split()
    digits = []
    for line in data:
        first_digit = ""
        last_digit = ""
        line = list(line)
        for char in line:
            if char.isnumeric():
                first_digit = char
                break
        line.reverse()
        for char in line:
            if char.isnumeric():
                last_digit = char
                break
        digits.append(first_digit + last_digit)
    digits = [int(i) for i in digits]
    answer = sum(digits)
    print(answer)


if __name__ == "__main__":
    main()
