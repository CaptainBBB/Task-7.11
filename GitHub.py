t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def func_decorator(func):
    def wrapper(multiple_hyphens):
        new_string = func(multiple_hyphens)
        if '---' in new_string:
            return new_string.replace('---', '-')
        else:
            return new_string
    return wrapper


@func_decorator
def do_translit(a_string):
    for letter in a_string.lower():
        for a_key, a_value in t.items():
            if letter == a_key:
                a_string = a_string.lower().replace(letter, a_value)
                break
            elif letter in ": ;.,_":
                a_string = a_string.replace(letter, '-')
    return a_string


s = input()
print(do_translit(s))