ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
elevens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
hundreds = {9: "", 6: "thousand", 3: "million", 0: "billion"}


# Convert a given numeric to English words(US Notation)
def say(number):
    # Handling Corner Cases
    if number == 0:
        return 'zero'
    if number >= 1e12:
        raise ValueError("You can only have so much of something")
    number_string = str(int(number)).zfill(12)
    words = []
    # Break the number into groups of 3 ones, thousands, millions, billions
    for idx in range(0, 12, 3):
        batch = number_string[idx:idx + 3]
        if batch == "000":
            continue

        # Convert the current 3 digits to a word. (sub-name)
        hundreds_digit = bool(batch[0] != '0')
        if hundreds_digit:
            words += [f"{ones[int(batch[0])]} hundred"]
        if batch[1] == '1':
            if (idx > 8) and (not hundreds_digit) and (words != []):
                hundreds_digit = True
            words += [f"{'and ' if hundreds_digit else ''}{elevens[int(batch[1:])-10]}"]
        elif batch[1:] != "00":
            if (idx > 8) and (not hundreds_digit) and (words != []):
                hundreds_digit = True
            words += [f"{'and ' if hundreds_digit else ''}" + f"{tens[int(batch[1])]}-{ones[int(batch[2])]}".strip("-")]
        if idx < 9:
            words[-1] += f" {hundreds[idx]}"
    return " ".join(words)
