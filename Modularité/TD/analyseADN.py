from typing import Union


def presence_de_A(sequence: str) -> bool:
    """
    Usage: presence_de_A(sequence)
    Entries: An ADN sequence (a String with only A, C, T and G)
    Return: True if the sequence contain a A, False else
    Units tests :
        no "A" found:
        >>> presence_de_A("CTTGT")
        False

        "A" found:
        >>> presence_de_A("ACCTG")
        True
    """
    if "A" in sequence:
        return True
    return False

def position_de_AT(sequence: str) -> Union[int, None]:
    """
    Usage: presence_de_AT(sequence)
    Entries: An ADN sequence (a String with only A, C, T and G)
    Return: The index of the "AT" segment, None if not found
    Units tests :
        no "AT" found:
        >>> position_de_AT("GACGTA")

        "AT" found:
        >>> position_de_AT("CTTATGCT")
        3
        >>> position_de_AT("GATATAT")
        1
    """
    count = 0
    for i in sequence:
        if (count + 1) == len(sequence):
            break
        if i == "A" and sequence[count+1] == "T":
            return count
        count += 1
    return None

def position(code: str, sequence: str) -> Union[int, None]:
    """
    Usage: position(code, sequence)
    Entries: An ADN code and an ADN sequence (a String with only A, C, T and G)
    Return: The index of the ADN code segment, None if not found
    Units tests :
        code found:
        >>> position("CCG", "CTCCGTT")
        2

        no code found:
        >>> position("ACCG", "CTCCGTT")
    """
    for i in range(len(sequence)):
        if (i + len(code)) > len(sequence):
            break
        if code[0] == sequence[i]:
            res = True
            for y in range(len(code)):
                if code[y] != sequence[i+y]:
                    res = False
            if res:
                return i
    return None

def lire_seqADN(file: str) -> str:
    """
    Usage: lire_seqADN(file)
    Entries: A file in the current directory
    Return: The content of the file as a String
    Units tests :
        file found:
        >>> lire_seqADN("unit_test.txt")
        'Test passed'

        no file found:
        >>> lire_seqADN("xxxx")
        File not found: xxxx
    """
    try:
        return open(file).read()
    except IOError:
        print(f"File not found: {file}")


def _test():
    """
    Testing all the file
    """
    from doctest import testmod
    testmod()

if __name__ == '__main__':
    _test()