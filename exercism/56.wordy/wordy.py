def calculate(question):
    equation = []
    for match in question.replace("?", "").split(" "):
        if match.isalpha():
            equation += {
                "plus": "+",
                "multiplied": "*",
                "minus": "-",
                "subtracted": "-",
                "divided": "/"
            }.get(match, "")
        elif match.replace("-", "").isdigit():
            equation += [match]
    try:
        if len(equation) < 2:
            raise Exception("Fuckup detected")
        result = eval(" ".join(equation))
    except:
        raise ValueError("It's Math not magic !!!")
    return result


# calculate("What is 4 minus -12?")
