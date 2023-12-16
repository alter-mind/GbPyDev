#!/bin/bash

# Создаем и переходим во временную директорию
mkdir temp
cd temp/

# Копируем заранее форкнутый репозиторий
git@github.com:alter-mind/DSde.git
cd DSde/

# Копируем инструкцию для гита из своего основного репозитория
cp ../../python/git_intro/sem1_homework/git.md README.md

# Добавляем в индекс, коммитим и пушим
git add .
git commit -m 'update README.md'
git push origin master

# Делаем pull request в репозиторий преподавателя

# Удаляем временную папку
cd ../../
rm -rf temp/
