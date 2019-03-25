__version__ = '1.0'
__author__ = 'Sergey Belousov'


def get_allowed_bits(bs: bytes) -> int:
    """
    Возвращает количество бит, в которых можно хранить произвольную информацию.

    Аргументы:
        s – исходная последовательность байтов.
    """

    if len(bs) % 3 == 0:
        return 0
    else:
        return (3 - len(bs) % 3) * 2


def base64enc_inserted(bs: bytes, number: int=0) -> str:
    """
    Возвращает строку base64 (кодированную последовательность байтов s),
    содержащую скрытое число number.

    Аргументы:
        s – исходная последовательность байтов,
        number – число для скрытия (по умолчанию 0).
    """

    bits_can_write = get_allowed_bits(bs)  # Сколько бит можно записать
    blocks_can_write = bits_can_write // 2  # Как много блоков по 6 бит можно записать (количество знаков =)

    # Если нужно записать больше информации, чем возможно
    if bits_can_write < len(bin(number)[2:]):
        raise ValueError("Невозможно записать {} бит в эту строку.".format(len(bin(number)[2:])))

    # Список из блоков по 8 бит
    blocks8_list = [bin(byte)[2:].zfill(8) for byte in bs]

    # Дополнение незначащими блоками
    for i in range(blocks_can_write):
        blocks8_list.append("00000000")

    # Слить все блоки в одну строку
    binary_string = ''.join(blocks8_list)

    # Разбить строку на блоки по 6 бит
    blocks6_list = [binary_string[i:i + 6] for i in range(0, len(binary_string), 6)]

    # Найти блок, который можно модифицировать
    modify_block_idx = len(blocks6_list) - blocks_can_write - 1
    block_to_modify = [i for i in blocks6_list[modify_block_idx]]

    # Подготовить число к записи (добавить лидирующие нули, преобразовать к списку)
    bits_to_write = [i for i in bin(number)[2:].zfill(bits_can_write)]

    # Записать биты в конец блока (в -1, -2, ...)
    # От -1 до -количество_бит_для_записи - 1 с шагом -1
    for i in range(-1, -bits_can_write - 1, -1):
        block_to_modify[i] = bits_to_write[i]

    # Применение изменений
    blocks6_list[modify_block_idx] = ''.join(block_to_modify)

    # Алфавит base64
    alphabet = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"]

    # Конструирование строки base64
    # b64[i] = alphabet[int(i, 2)], где i – блоки по 6 бит
    b64_str = [alphabet[int(i, 2)] for i in blocks6_list if int(i, 2) != 0]
    for i in range(blocks_can_write):
        b64_str.append("=")

    return ''.join(b64_str)


def base64dec_inserted(s: str) -> str:
    """
    Возвращает число, скрытое в строке s, закодированной в base64.

    Аргументы:
        s – строка, закодированная в base64.
    """

    if '=' not in s:
        raise ValueError("Нет скрытой информации.")

    # Алфавит для base64
    alphabet = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"]

    # Количество незначащих битов
    cnt_equal = s.count('=')

    # Информация скрывается в последнем символе строки base64 (не считая символа =)
    last_symbol = s[-cnt_equal-1]
    idx = alphabet.index(last_symbol)

    return bin(idx)[2:][-cnt_equal*2:]
