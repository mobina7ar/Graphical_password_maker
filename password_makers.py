from random import randint, choices, shuffle
from string import ascii_uppercase, ascii_lowercase, punctuation


def make_password(password_length, flags):
    l = sum(flags)
    e = password_length // 1
    password = []
    level = 0

    if flags[0] == True:
        level = level + 1
        upper_number = randint(1, e - (l - level))
        upper_select = choices(list(ascii_uppercase), k=upper_number)
        password.extend(upper_select)
        if level == l:
            need = password_length - len(password)
            more = choices(list(ascii_uppercase), k=need)
            password.extend(more)

    if flags[1] == True:
        level = level + 1
        remaining = password_length - len(password)
        lower_number = randint(1, remaining - (l - level))
        lower_select = choices(list(ascii_lowercase), k=lower_number)
        password.extend(lower_select)
        if level == l:
            need = password_length - len(password)
            more = choices(list(ascii_lowercase), k=need)
            password.extend(more)

    if flags[2] == True:
        level = level + 1
        remaining = password_length - len(password)
        number_number = randint(1, remaining - (l - level))
        number_select = choices(list("0123456789"), k=number_number)
        password.extend(number_select)
        if level == l:
            need = password_length - len(password)
            more = choices(list("0123456789"), k=need)
            password.extend(more)

    if flags[3] == True:
        level = level + 1
        remaining = password_length - len(password)
        simbol_number = randint(1, remaining - (l - level))
        simbol_select = choices(list(punctuation), k=simbol_number)
        password.extend(simbol_select)
        if level == l:
            need = password_length - len(password)
            more = choices(list(punctuation), k=need)
            password.extend(more)

    shuffle(password)
    final_password = "".join(password)
    return final_password


if __name__ == "__main__":
    p = make_password(20, [True, True, True, True])
    print(p)
