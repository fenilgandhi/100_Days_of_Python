import math 

def encode(plain_text):
    # Normalise the plain_text
    plain_text = ''.join([c.lower() for c in plain_text if c.isalnum()])

    # Find a c
    lp = len(plain_text)
    if lp < 2:
    	return plain_text
    
    # Matrix size
    c = math.ceil(lp ** 0.5)
    r = c if lp > (c * (c-1)) else (c-1)
    plain_text += " " * (r * c - lp)
    result = [plain_text[i::c] for i in range(c)]

    # Join the words with a space
    result = " ".join(result)
    return result
