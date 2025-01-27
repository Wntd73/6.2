'''1 часть – написать программу в соответствии со своим вариантом задания. 
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), 
сравнив по времени их выполнение.
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.

2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

Усложнение: ограничение на длину слова (не более 15 символов).
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

def gen_lex_dict(word):
    lexs = []
    for number, cases in endings.items():
        for ending in cases.values():
            lexeme = f"{word} компьютер{ending}"
            lexs.append(lexeme)  
    return lexs

def find_shortest(lexemes, base_word):
    filtered_lexemes = [lex for lex in lexemes if lex != base_word and len(lex) <= 15]
    if not filtered_lexemes:
        return None 
    return min(filtered_lexemes, key=len)

def gen_lex_it(word):
    s_end = ['', 'а', 'у', '', 'ом', 'е']
    p_end = ['ы', 'ов', 'ам', 'ы', 'ами', 'ах']
    all_end = itertools.chain(s_end, p_end)

    lexs = [f"{word} компьютер{ending}" for ending in all_end]
    return lexs

word = input("Введите слово: ")

t_d = timeit.timeit(lambda: gen_lex_dict(word), number=1)
r_d = gen_lex_dict(word)
shortest_d = find_shortest(r_d, f"{word} компьютер")

t_i = timeit.timeit(lambda: gen_lex_it(word), number=1)
r_i = gen_lex_it(word)
shortest_i = find_shortest(r_i, f"{word} компьютер")

print("Сгенерированные лексемы (словарь):")
print(r_d)
print(f"Время выполнения (словарь): {t_d:.5f} сек")
print(f"Самая короткая лексема (словарь): {shortest_d if shortest_d else 'Нет подходящих лексем'}")

print("Сгенерированные лексемы (itertools):")
print(r_i)
print(f"Время выполнения (itertools): {t_i:.5f} сек")
print(f"Самая короткая лексема (itertools): {shortest_i if shortest_i else 'Нет подходящих лексем'}")