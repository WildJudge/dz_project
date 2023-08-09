def convert_to_uppercase(input_string):
    """Функция принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return input_string.upper()


def capitalize_words(input_string):
    """Заглавными буквами пишется первая буква каждого слова во входной строке"""
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
