from obj import Contact, Book, Menu
import os

entry_menu = Menu('1 - открыть/создать справочник\n'
                  '2 - показать файлы в текущей директории\n'
                  '3 - удалить файл справочника\n'
                  '4 - выбрать справочник для работы\n'
                  '0 - для выхода')
book_menu = Menu('1 - показать контакты\n'
                 '2 - добавить контакт\n'
                 '3 - редактировать контакт\n'
                 '4 - удалить контакт\n'
                 '5 - сохранить справочник на диск\n'
                 '0 - для выхода')


def get_answer(menu):
    answer = input('Ваш выбор: ')
    if menu.is_esists(answer):
        return int(answer)
    else:
        menu.show()
        get_answer(menu)


def bin_answer():
    return True if input('Ответ [yes/no]: ') in 'ДадаYesyes1' else None


def open_book(book_name=None):
    try:
        if not book_name:
            book_name = input('Укажите имя справочника: ')
        if os.path.exists(book_name):
            print('Данный файл уже существует, открыть его?')
            if bin_answer():
                return Book(book_name)
            else:
                print('Создать новый?')
                if bin_answer():
                    open_book()
                else:
                    return None
        else:
            return Book(book_name)
    except Exception as err:
        print(err)
        print('Error in func create_book()')


def list_books():
    books = []
    for file in [path for path in os.listdir() if os.path.isfile(path)]:
        try:
            book = Book(file)
            books.append(book)
        except:
            pass
    return books


def del_book(path, books=None):
    if books is None:
        books = list_books()
    if path in [book.name for book in books]:
        books = list(filter(lambda book: book.name == path, books))
        os.remove(path)
        return True, books
    return False, books


def manage_files(answer, books=None):
    if answer == 0:
        return False
    elif answer == 1:
        book = open_book()
        return [book]
    elif answer == 2:
        books = list_books()
        if books:
            print(' '.join([bk.name for bk in books]))
            return books
        else:
            print('Файлов со справочником в каталоге не обнаружено, желаете создать?')
            if bin_answer():
                book = open_book()
                return [book]
            else:
                return False
    elif answer == 3:  # вот тут возможно будут ошибки при попытке повторного удаления
        path = input('Файл для удаления: ')
        result, books = del_book(path, books)
        print('Успешно удалено' if result else 'Нет такого справочника или при удалении возникла ошибка')
    elif answer == 4:
        if books:
            manage_book(selector(books))
        else:
            print('Не выбран справочник, желаете выбрать?')
            if bin_answer():
                manage_book(selector(books))
                return books
            else:
                return False


def selector(books):
    if not books:
        books = list_books()
    print(' '.join([bk.name for bk in books]))
    path = input('Выберите имя справочника: ')
    for book in books:
        if book.name == path:
            return book
    return selector(books)


def manage_book(book):
    while True:
        book_menu.show()
        answer = get_answer(book_menu)
        if answer == 0:
            break
        elif answer == 1:
            print(book)
        elif answer == 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            email = input('Введите почту: ')
            note = input('Введите примечание: ')
            print(f'* {len(book)}')
            new_id = book[len(book) - 1].id + 1 if len(book) else 0
            book.add(Contact(name, phone, email, note, new_id))
        elif answer == 3:
            edit_contact(book, delete=False)
        elif answer == 4:
            edit_contact(book, delete=True)
        elif answer == 5:
            book.save()
        if book.have_changes:
            print('* - есть несохранённые изменения, желаете сохранить?')
            if bin_answer():
                book.save()


def edit_contact(book, delete=False):
    if len(book):
        print(f'Нужно выбрать контакт для {"удаления" if delete else "редактирования"}, желаете осуществить поиск?')
        if bin_answer():
            search_menu = book[0].key_menu
            search_menu.show()
            answer = get_answer(search_menu)
            key = book[0].keys[answer]
            mask = input('Введите поисковый ключ: ')
            found = book.search(mask, key)
        else:
            found = book.contacts
        if len(found):
            print('Подходящие контакты')
            to_strip = '\n'
            contact_menu = Menu('\n'.join([f'{el.id} - {str(el).rstrip(to_strip)}' for el in found]))
            contact_menu.show()
            edit_id = get_answer(contact_menu)
            if delete:
                book.delete(edit_id)
            else:
                print('Какое поле хотите изменить?')
                key_menu = book[0].key_menu
                key_menu.show()
                answer = get_answer(key_menu)
                key = book[0].keys[answer]
                edition = input('Введите новое содержание поля: ')
                book.change(edit_id, edition, key)
    else:
        print('Этот справочник пуст')
