'''1 часть – написать программу в соответствии со своим вариантом задания. 
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), 
сравнив по времени их выполнение.
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.

2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

Усложнение: ограничение на длину слова (не более 10 символов).
Целевая функция: нахождение самой короткой лексемы.'''

import timeit
import itertools

endings = {
    'Единственное': {
        'именительный': '',
        'родительный': 'а',
        'дательный': 'у',
        'винительный': '',
        'творительный': 'ом',
        'предложный': 'е'
    },
    'Множественное': {
        'именительный': 'ы',
        'родительный': 'ов',
        'дательный': 'ам',
        'винительный': 'ы',
        'творительный': 'ами',
        'предложный': 'ах'
    }
}

word = "компьютер"

def gen_lex_dict(word):
    lexs = []
    for number, cases in endings.items():
        for ending in cases.values():
            lexeme = f"{word}{ending}"
            if len(lexeme) <= 10:
                lexs.append(lexeme)
    return lexs

def find_shortest(lexemes, base_word):
    return min([lex for lex in lexemes if lex != base_word], key=len)

def gen_lex_it(word):
    s_end = ['', 'а', 'у', '', 'ом', 'е']
    p_end = ['ы', 'ов', 'ам', 'ы', 'ами', 'ах']
    all_end = itertools.chain(s_end, p_end)

    lexs = [f"{word}{ending}" for ending in all_end if len(f"{word}{ending}") <= 10]
    return lexs

t_d = timeit.timeit(lambda: gen_lex_dict(word), number=1)
r_d = gen_lex_dict(word)
shortest_d = find_shortest(r_d, word)

t_i = timeit.timeit(lambda: gen_lex_it(word), number=1)
r_i = gen_lex_it(word)
shortest_i = find_shortest(r_i, word)

print("Сгенерированные лексемы (словарь):")
print(r_d)
print(f"Время выполнения (словарь): {t_d:.5f} сек")
print(f"Самая короткая лексема (словарь): {shortest_d}")

print("Сгенерированные лексемы (itertools):")
print(r_i)
print(f"Время выполнения (itertools): {t_i:.5f} сек")
print(f"Самая короткая лексема (itertools): {shortest_i}")
