from func import *

books = None  # нужно, чтобы не перечитывать файлы на диске, если их много и они большие
while True:
    entry_menu.show()
    answer = get_answer(entry_menu)
    books = manage_files(answer, books)
    if not books:
        break
