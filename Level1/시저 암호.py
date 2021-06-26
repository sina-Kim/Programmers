from string import ascii_lowercase, ascii_uppercase

def solution(s, n):
    encoder = dict()
    encoder[' '] = ' '
    for lowercase in ascii_lowercase:
        val = ord(lowercase)
        if val + n > ord('z'):  encoder[lowercase] = chr(val + n - ord('z') - 1 + ord('a'))
        else:                   encoder[lowercase] = chr(val + n)
    for uppercase in ascii_uppercase:
        val = ord(uppercase)
        if val + n > ord('Z'):  encoder[uppercase] = chr(val + n - ord('Z') - 1 + ord('A'))
        else:                   encoder[uppercase] = chr(val + n)

    return ''.join([encoder[ch] for ch in s])