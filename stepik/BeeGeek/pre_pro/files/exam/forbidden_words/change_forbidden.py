import re

with open('forbidden_words.txt') as inf:
    stop_list = set(inf.read().split())

with open(input()) as inf:
    text = inf.read()
    output = text
    for forbidden in stop_list:
        if forbidden.lower() in text.lower():
            output = re.sub(forbidden, '*' * len(forbidden), output, flags=re.IGNORECASE)

print(output)
# for line in inf.read().split():
#     print(line)
