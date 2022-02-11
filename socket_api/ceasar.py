import string

def encrypted(d: str):
    ceaser = {s:s1 for s, s1 in zip(string.ascii_letters, string.ascii_letters[5:]+string.ascii_letters[:5])}
    rez = ''
    for i in d:
        rez += ceaser.get(i, i)
    return rez
