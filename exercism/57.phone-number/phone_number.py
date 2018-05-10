class Phone(object):
    def __init__(self, phone_number):
        phone_number = [char for char in phone_number if char.isdigit()]
        if phone_number[:1] == ['1']:
            phone_number = phone_number[1:]
        if len(phone_number) != 10:
            raise ValueError("Insufficient Digits")
        if (int(phone_number[0]) > 1) and (int(phone_number[3]) > 1):
            self.number = "".join(phone_number)
        else:
            raise ValueError("Typo on a telephone")

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        number = self.number
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
