def transpose(input_lines):
    if not input_lines:
        return ""
    input_lines = input_lines.split("\n")
    max_len = max(len(line) for line in input_lines)
    lines = (line.ljust(max_len) for line in input_lines)
    expected = ("".join(column) for column in zip(*lines))
    return "\n".join(expected)
