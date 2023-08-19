# Предположить, что числа в исходном массиве из 9 элементов имеют диапазон[0, 3], и представляют собой,
# например, состояния ячеек поля для игры в крестики-нолики,
# где 0 – это пустое поле, 1 – это поле с крестиком, 2 – это поле с ноликом, 3 – резервное значение.
# Такое предположение позволит хранить в одном числе типа int всё поле 3х3.
# Записать в файл 9 значений так, чтобы они заняли три байта.
#
#
# В продолжение дописать "разворачивание" поля игры крестики-нолики из сохраненного в файле состояния
# (распарсить файл, в зависимости от значений (0-3) нарисовать поле со значками 'х' 'о' '.')
from array import array
import sys

tic_tac_toe = [['.', 'x', 'o'], ['', '', ''], ['', '.', '']]


def encode_field(field: list[list[str]]) -> str:
    decoding = ''
    for row in field:
        for char in row:
            decoding += get_char_encode(char)
    return decoding


def get_char_encode(ch: str) -> str:
    match ch:
        case '':
            return '00'
        case 'o':
            return '01'
        case 'x':
            return '10'
        case '.':
            return '11'
        case '00':
            return ''
        case '01':
            return 'o'
        case '10':
            return 'x'
        case '11':
            return '.'


def encode_str_to_arr(encode: str):
    numbers = [encode[:8], encode[8: 16], encode[16:]]
    a = list(map(lambda el: int(el, 2), numbers))
    write_to_file(a)


def write_to_file(encode: list):
    line = bytearray(encode)
    with open('./-', 'wb') as ouf:
        ouf.write(bytes(line))


def read_file():
    out = []
    with open('./-', 'rb') as inf:
        intro = inf.read()
        for byte in intro:
            out.append(byte)
    return out


def decode_array(decode: list) -> str:
    out = ''
    for (idx, el) in enumerate(decode):
        if idx < 2:
            out += f'{el:08b}'
        else:
            el = f'{el:2b}' if el > 1 else f'{el:02b}'
            out += el
    return out


def create_field_from_string(string: str) -> list[list[str]]:
    out = [['' for i in range(3)] for _ in range(3)]
    count = 0
    for (idx, row) in enumerate(out):
        for (iidx, el) in enumerate(row):
            out[idx][iidx] = get_char_encode(string[(count * 2) : (count * 2 + 2)])
            count += 1
    print(out)
    return out




def main():
    print(tic_tac_toe)
    encode_str_to_arr(encode_field(tic_tac_toe))
    decode = read_file()
    fl = decode_array(decode)
    create_field_from_string(fl)


if __name__ == '__main__':
    main()
