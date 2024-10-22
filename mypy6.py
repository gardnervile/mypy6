import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def on_password_change(edit, new_password):
    checks = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    successful_checks = [check(new_password) for check in checks]
    score = len([result for result in successful_checks if result]) * 2

    rating_text.set_text(f"Рейтинг пароля: {score}")


ask = urwid.Edit("Введите пароль: ")
rating_text = urwid.Text("Рейтинг пароля: 0")

menu = urwid.Pile([ask, rating_text])
menu = urwid.Filler(menu, valign='top')

urwid.connect_signal(ask, 'change', on_password_change)

urwid.MainLoop(menu).run()