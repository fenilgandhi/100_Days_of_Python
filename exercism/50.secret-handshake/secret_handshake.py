secret = {
	1: "wink",
	2: "double blink",
	4: "close your eyes",
	8: "jump"
}
reverse_secret = dict([(b, a) for a, b in secret.items()])


def handshake(code):
	actions = []
	reverse = False
	if (code >= 16):
		code = code % 16
		reverse = True
	idx = 8
	while (code > 0):
		if (code >= idx):
			actions += [secret[idx]]
			code %= idx
		idx //= 2
	if not reverse:
		actions = actions[::-1]
	return actions


def secret_code(actions):
	code = []
	for action in actions:
		code += [reverse_secret[action]]
	if (len(code) > 1) and (code[1] < code[0]):
		code += 16
	return sum(code)
