#!/bin/bash

# Создаем и переходим во временную директорию
mkdir temp_dir
cd temp_dir/

# Создаем и заполняем файлы первых четырёх веток, каждую слелующую начинаем с
# коммита предыдущей
git checkout -b branch1
echo 'sample text for branch1' > branch1.file
git add .
git commit -m 'Add files for branch1'
git checkout -b branch2
echo 'sample text for branch2' > branch2.file
git add .
git commit -m 'Add files for branch2'
git checkout -b branch3
echo 'sample text for branch3' > branch3.file
git add .
git commit -m 'Add files for branch3'
git checkout -b branch4
echo 'Sample text for branch4' > branch4.file
git add .
git commit -m 'Add files for branch4'


# Переключаемся на ветку branch3 и создаем конфликт
git checkout branch3
echo 'Updated text for branch3' > branch1.file
git add .
git commit -m 'Add conflict in branch3 for merge with branch4'

# Переключаемся на ветку branch4 и сливаем branch3
git checkout branch4
git merge branch3

# Создании конфликта опечатался, была задумка поместить конфлик в файл
# 'branch3.file'
# Данный конфликт был разрешён автоматически
# Выводим результаты для проверки
cat branch1.file

# Создадим ситуацию, чтобы изменения в одной ветке противоречили изменениям
# в другой ветке так, чтобы git не смог разрешить их автоматически
git checkout branch1
echo 'Some another text for branch1' >> branch1.file
git add .
git commit -m 'Add new conflict for branch1'
git checkout branch2
echo 'More text for branch2' >> branch2.files
git add .
git commit -m 'Add conflict for branch2 too'
git checkout branch3
echo 'and a little bit text for branch3' >> branch2.files
git add .
git commit -m 'Add some conflict for branch3 too'

# Теперь попробуем каскадно смержить branch4 в branch3, затем branch3 в
# branch2 и, наконец, branch2 в branch1
git merge branch4
# Первое слияние прошло без конфликтов, едем далее
git checkout branch2
git merge branch3
# наконец, git не смог самостоятельно разрешить конфликт в файле branch2.files
# создаем это вручную, выберем одну из версий обозначенную угловыми скобками
nano branch2.files
# сохраняем файл и фиксируем изменения
git add .
git commit -m 'conflict solved'
# переходим в branch1 и мержим branch2
git merge branch2
# снова разрешаем конфликт вручную
nano branch1.file
git commit -m 'final solve'

# сохраняем красивый вид (у меня свой алиас для команды, он описан в git.md
# в домашней работе к первому уроку)
git gg > ../git_log_graph.log

# Возвращаемся в исходную директорию и удаляем временную
cd ..
rm -rf temp_dir

# В основном репозитории нам не хотелось бы видеть всего этого безобразия, но
# последний файл git_log_graph.log хотелось бы сохранить
# Для этого воспользуемся cherry-pick
git checkout git_intro
git cherry-pick 68cce0c

# Сохраняем эту инструкцию и делаем финальный коммит
