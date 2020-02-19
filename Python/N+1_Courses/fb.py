# Find the average length of word in sentence
sentence = "Hi my name is Bob"
words = sentence.split()
print(words)
average = sum(len(word) for word in words) / len(words)
print(average)

# string problems
# lower, upper, etc.

# Validate the ip address
def validate(ip):
    valid_digit = set('0123456789')
    a = ip.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

print(validate('127.0.0.b'))

# for a list array=[['D'],['A','B'],['A','C'],['C','A']] find the number of followers
# D = 0, A = 2, C = 1
def count(pairs):
    d = {}
    for pair in pairs:
        if len(pair) == 1 and pair[0] not in d:
            d[pair[0]] = 0
        else:
            if pair[0] not in d:
                d[pair[0]] = 1
            else:
                d[pair[0]] += 1
    return d

print(count([['D'],['A','B'],['A','C'],['C','A']]))
