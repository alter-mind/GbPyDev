"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам,
если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.
"""

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'


def check_rhythm(string):
    def vowels_count(string):
        count = 0
        vowels = 'ёуеыаоэяию euioa'
        for letter in string:
            if letter in vowels:
                count += 1
        return count

    phrases = string.split()
    if len(phrases) < 2:
        return None
    else:
        check = True
        const_vowels = vowels_count(phrases[0].lower())
        for phrase in phrases[1:]:
            if const_vowels != vowels_count(phrase.lower()):
                check = False
        return check


rhythm = check_rhythm(stroka)
if rhythm is None:
    print('Количество фраз должно быть больше одной!')
elif rhythm:
    print('Парам пам-пам')
else:
    print('Пам парам')