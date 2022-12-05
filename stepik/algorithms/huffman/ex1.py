def encode_line(decode: dict, line: str) -> str:
    out = ''
    pointer = 0
    code = ''

    for i, char in enumerate(line):
        code += char
        if code in decode:
            out += decode.get(code)
            code = ''
    print(out)


def main():
    count_chars, length_line = map(int, input().split())

    decode = dict()

    for _ in range(count_chars):
        char, code = input().split(': ')
        decode[code] = char

    line = input()

    print(line, decode)

    encode_line(decode, line)


if __name__ == '__main__':
    main()
