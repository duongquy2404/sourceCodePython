s=input()

def convert(s):
    count_up=0
    count_low=0
    for c in s:
        if c.isupper():
            count_up+=1
        if c.islower():
            count_low+=1
    if count_up>count_low:
        print(s.upper())
    else:
        print(s.lower())

convert(s)