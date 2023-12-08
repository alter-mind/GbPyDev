---
aliases:
  - Система контроля версий
  - ГИТ
  - GIT
tags:
  - git
  - it
  - linux
  - мануалы
  - howto
---

# Система контроля версий GIT
##### Документация

[ProGIT на русском](https://git-scm.com/book/ru/v2)
[ProGIT на английском](https://git-scm.com/book/en/v2)

##### Хранение файлов

Система GIT хранит не полные копии, а версии изменившихся файлов, вместо файлов, не потерпевших изменения используются ссылки на ранние версии. 

Снимок системы называется **коммитом**, хронологическая последовательность коммитов называется веткой. Ветки могут разделяться, идти параллельно и сливаться. 

GIT является децентрализованной системой, однако возможно наличие центрального [[Base/Edu/IT_Knowledge/Репозиторий|репозитория]], при этом каждый участник имеет локальную копию всех файлов, веток и историю правок. 

Выход из строя центрального репозитория не означает потерю всей работы, так как репозиторий может быть восстановлен из любой локальной копии и его может заменить любой другой хост, реализующий систему контроля версий GIT

Наличие центрального репозитория не является обязательным условием, git можно использовать на локальной машине в одиночной разработке.

GIT следит за изменениями, если вы проводите какие-либо действия над файлами, он почти всегда добавляет новые данные в свою базу. Удалить что-либо почти невозможно, что-то добавленное один раз навсегда остается в истории системы. Вы в любой момент можете откатиться в любую точку и получить копию даже удалённых файлов. 

##### Локальная работа. Начало
 
 Чтобы убедиться, что git установлен в системе можно выполнить команду:
```bash
git --version
```

###### Настройка

Перед началом работы необходимо сообщить системе git кто вы и как вас представлять другим участникам распределённой системы контроля версий

Задать имя и адрес электронной почты:
```bash
git config --global user.name 'User Name'
git config --global user.email user@email.com
```

Посмотреть установленные настройки можно командой
```bash
git config --list
```
чтобы узнать местоположение конфигурационного файла
```bash
git config --list --show-origin
```

Существует два способа получить в своё распоряжение git проект:
1. В каталоге проекта выполнить команду 
	`git init`
2. скопировать git проект из удалённого репозитория командой 
	`git clone`
Обе команды создают (копируют) в текущем каталоге подкаталог `.git` в котором будет содержаться вся необходимая информация и сохраняться текущее состояние git проекта. 

Этой командой можно установить редактор по умолчанию, в данном случае nano:
```bash
git config --global core.editor nano
``` 



###### Создание первого коммита

Чтобы добавить файл под контроль системы git необходимо проиндексировать его при помощи команды git add:
`git add .` - индексирует всё содержимое текущего каталога
`git add new.file` - указание что нужно проиндексировать new.file

после индексации можем добавить коммит командой
```bash
git commit -m 'comment'
```
если не указывать комментарий, то после нажатия 'Enter' откроется текстовый редактор по умолчанию, в linux это, как правило, vim или nano.
```bash
git commit
```
В таком режиме возможно создание многострочных комментариев, если оставить комментирий пустым - это приведёт к отмене операции. 
###### Клонирование проекта

пример:
```bash
git clone https://github.com/web-standards-ru/dictionary.git
``` 
эта команда клонирует репозиторий словаря по https

Если необходимо переименовать папку - новое название можно указать сразу после названия репозитория:
```bash
git clone https://github.com/web-standarts-ru/dictionary.git dict
``` 

###### Графические клиенты:

Для работы с git существует множество графических клиентов, среди них gitk или git-gui. Кроме того, множество IDE поддерживают интерграцию с git: eclipse, JetBrains и другие. 

##### Базовые операции

Файлы в git проекте могут быть в отслеживаемом и неотслеживаемом состояниях. В первом случае файлы зарегистрированы в git и его содержимое проиндексировано, во втором случае git ничего о них не знает.  В обоих случаях git помечает эти файлы как доступные для добавления. 

###### Добавление файлов в git проект

Перевести файлы в индекс можно командой `git add`, в коммит попадают только файлы, находящиеся в индексе. 
Выяснить статус проекта - команда `git status`. По умолчанию, вывод команды довольно объемный, можно сделать в коротком виде: `git status -s`. 
Git анализирует только отслеживаемые файлы, чтобы посмотреть изменения можно воспользоваться командой `git diff`.
Если в проекте нет неотслеживаемых файлов и нет изменений вне индекса, то команда `git diff` ничего не вернёт. Однако если добавить к ней параметр '--cached', то мы сможем увидеть изменения, которые находятся в индексе, но ещё не вошли в коммит.  `git diff --cached`

можно объединить команды 'git add' и 'git commit' в одну:
```bash
git commit -am 'комментарий к коммиту'
```

Т.е. если в проекте есть неотслеживаемый или модифицированный файл, то сначала нужно перевести их в индексированной состояние и потом можно сделать снимок проекта. 

###### Удаление файлов

Вспомним, что файлы могут быть в нескольких состояниях:
- **неотслеживаемые**, о которых git ничего не знает
	эти файлы удалить проще всего, можно сделать это любым способом, для этого не нужны средства git
- **отслеживаемые** - это старые изменённые файлы, git знает их предыдущие состояния и готов выдать ранее сохранённый вариант
	Есть 2 варианта действий:
	1. Добавить изменения в индекс командой `git add <file>`
	2. Откатить изменения до состояния предыдущего снимка системы командой `git checkout -- <file>`
- **отслеживаемые, попавшие в индекс**
	Тут уже сложнее, сначала рекомендуется посмотреть изменения:
	`git diff`
	Убедившись в правильности выбора, следует вывести файл из индекса:
	`git reset HEAD <file>`
	после чего мы можем откатиться к предыдущему коммиту или внести необходимые правки. 
- **отслеживаемые, попавшие в коммит**
	Самая сложная ситуация, удаление коммитов считается небезопасным и может нарушить целостность репозитория с кодом. Решение этой ситуации будет добавлено позже. 

###### Просмотр истории проекта

`git log` - показывает историю коммитов в хронологическом порядке от более свежих, к более ранним. Если коммитов много и они не умещаются на экране двигаться дальше можно нажимая пробел. Выйти из режима просмотра можно нажав 'q'.

Можно ограничить количество показываемых коммитов, например команда `git log -2` выведет 2 последних коммита

Чтобы вывести детальный изменения для каждого коммита, следует добавить параметр '-p': `git log -2 -p` 

`git log -2 --stat` - если нужна статисктика для каждого коммита. Под каждым из коммитов выводится список изменённых файлов и количество строк, которые были добавлены или удалены. Добавленные строки маркируются зелёным плюсом, удалённые строки - красным минусом. 

Ещё больше сократить вывод комманды git log можно при помощи параметра '--pretty', который изменяет формат вывода, так команда выводит коммиты в одну строку:
```bash
git log --pretty=oneline
```

Можно вместо 'oneline' использовать 'format' и сформировать собственный формат логов, например так:
```bash
git log -pretty=format: "%h - %an, %ar: %s"
``` 
полный список параметров форматирования и их значения можно найти в документации git

###### Хэш-сумма коммита

каждый коммит в системе git снабжается хэшем SHA-1, в полном хэше часто нет необходимости и его сокращают до 7-8 символов. 

###### Поиск по дате

Для поиска в определённом временном интервале можно использовать параметры **--sinse** и **--until**:
- --sinse позволяет задать до какого момента в прошлом мы ищем коммиты
- --until позволяет задать дату, с которой мы начинаем поиск

команда позволяет искать коммиты, начиная с двух недельной давности и до настоящего момента
```bash
git log --sinse=2.week
```

команда ищет коммиты с начала проекта и до недельной давности. 
```bash
git log --until=1.week
```

можно одновременно использовать оба параметра и задать точный интервал времени поиска в прошлом:
```bash
git log --sinse=2022-01-01 --until=2022-01-31
```
- покажет коммиты за январь 2022 года. 


###### Поиск коммита по строке и автору

При помощи параметра '-S' можно найти коммит, в котором была добавлена или удалена заданная строка:
```bash
git log -SString -p
```
найдёт коммиты, в которых упоминается 'String'.

Поиск коммита по автору:
```bash
git log --author="User Name"
```

Иногда нужно выяснить, кто автор конкретной строки и в каком коммите зафиксированы её последние изменения. Для этого применяется команда **git blame**:
```bash
git blame readme.txt
```
В качестве параметра команда принимает имя файла и выводит содержимое файла, в котором каждая строка помечена хэшем коммита, автором и датой последнего изменения. 

###### Игнорирование

Всё, что помещается в git репозиторий, хранится в истории проекта. Поэтому, хорошей практикой является исключение из общего репозитория всех временных файлов, настроке и логов и т.д. 

Для этого существует специальный конфигурационный файл **.gitignore**, помещаемый в корень проекта. 
Внутри файла прописывается шаблон, все файлы и каталоги, которые ему удовлетворяют игнорируются системой git.

###### Пустые папки

Система git ориентируется на файлы, папки попадают под отслеживание только если в них находятся файлы, так, пустые папки игнорируются

##### Ветки

Сразу после создания git проекта автоматически создается основная ветка **master**, в этом легко убедиться выполнив команду 
```bash
git branch
```
Эта команда выводит список всех доступных веток, помечая текущую ветку звёздочкой

Посмотреть, на какой ветке мы находимся в данных момент можно так же командой
```bash
git status
```

###### Создание ветки

Создать ветку можно командой 
```bash
git branch new_branch
```

Переключиться на эту ветку можно командой 
```bash
git checkout new_branch
```

Эти две команды можно объединить в одну:
```bash
git checkout -b new_branch
```

###### Переименование ветки

Чтобы переименовать ветку, нужно выполнить команду **'git branch -m'**, где после параметра идёт старое название ветки, затем новое название ветки, пример:
```bash
git branch -m new_branch renamed_branch
```
так, ветка new_branch была переименована в ветку renamed_branch

###### Удаление ветки

Чтобы удалить ветку, нужно выполнить команду **git branch -D**:
`git branch -D branch_to_delete`

###### Слияние веток

Коммиты одной ветки можно добавить в другую ветку, такая процедура называется слиянием и выполняется при помощи команды **git merge**. В момент слияния мы должны находиться в той ветке, куда будем сливать изменения. 

Например, мы хотим смержить изменения из ветки **new_branch** в ветку **master**, для этого выполним ряд комманд:
```bash
git checkout master
git merge new_branch
```
Если сейчас выполнить команду **git log** c параметром **graph**, то можно увидеть слияние веток, отрисованное псевдографикой:
```bash
git log --pretty=format: "%h -%d %s %cd" --graph
```

Отслеживать параллельные ветки и их слияние удобнее в графическом клиенте. 


##### Псевдонимы (алиасы) команд

Для объемных команды, которые используются часто можно использовать короткие, запоминающиеся псевдонимы. 

В качестве примера создадим алиас **gg** для команды **git log** с параметром **graph**:

```bash
git config --global alias.gg 'log --pretty=format:"%C(yellow)%h%Creset -%C(green)%d%Creset %s %C(bold blue)(%cn) %C(green)%cd%Creset" --graph --date=format:"%d.%m.%Y %H:%M"'
```

###### Разрешение конфликтов

При командной работе неизбежны ситуации, когда изменения одного разработчика противоречат изменениям другого разработчика. 

Чаще всего конфликты возникают при попытке смержить изменения в одной ветке с другой, когда git не может сделать это автоматически. В отчёте команды будут видны конфликтные файлы, конфликты внутри файлов отмечены угловыми скобками, чтобы их было хорошо видно в коде. В верхней части отображается код текущей ветки, в нижней - той, которая сливается. Нужно выбрать правильный вариант или написать новый, учитывающий изменения из обеих частей. 

Разрешив конфликт нужно зафиксировать изменения в новом коммите. 

##### Создание удалённого репозитория

При разработке участники проекта, как правило, пишут код на своих локальных компьютерах. Чтобы изменения стали доступны другим участникам проекта, их необходимо отправить в удалённый репозиторий, а так-же иметь возможность загружать изменения, сделанные другими участниками. Удалённый репозиторий представляет собой сервер с git, расположенный в интернете или локальной сети. 

Для того, чтобы начать пользоваться удалённым репозиторием можно начать с готовых git-хостиногов:
- [GitHub](https://github.com/)
- [BitBucket](https://bitbucket.org/)
Или развернуть собственный git-репозиторий на каком-либо сервере с SSH доступом. 

Если помимо консольного доступа требуется веб-интерфейс, можно воспользоваться сервисом [GitLab](https://gitlab.com/), его тоже можно развернуть на собственном сервере. 

###### Git хостинг GitHub

Этот хостинг обладает наибольшей популярностью в последние годы, принадлежит компании Microsof (2022). Для свободных проектов он бесплатен, впрочем, можно разместить ограниченное количество закрытые проектов. 

Кроме хостинга, GitHub предоставляет мощный веб-интерфейс для управления Git-репозиторием, трекер задач, Wiki-редактор документации, поиск по проектам, статистику по кодовой базе и многое другое. 

Чтобы получить доступ к созданию собственных репозиториев, необходимо зарегистрироваться и добавить в настройках свой публичный [[Base/Edu/IT_Knowledge/Linux#Ключи SSH |ключ SSH]]. 

Создать удалённый репозиторий на GitHub можно через web интерфейс самого сайта, далее подключаем его:
```bash
git remote add origin git@github.com:alter-mind/GbPyDev.git
```

командой `git push origin master` мы отправим все изменения в ветке **master** в удалённый репозиторий. 

Команда `git remote add origin` регистрирует удалённый сервер в файле **.git/config** 

Можно добавить псевдоним github для удалённого репозитория:
```bash
git remote add github git@github.com:alter-mind/GbPyDev.git
```
Теперь можно отправлять изменения в репозиторий при помощи команды:
```bash
git push github master
```
Т.е. после команды **git push** сначала указываем имя удалённого репозитория, затем название отправляемой ветки. 

Список доступный удалённых репозиториев можно узнать при помощи команды `git remote`

Загрузить изменения из удалённого репозитория можно командой **git pull**:
```bash
git pull origin master
```
загрузит из удалённого репозитория последнюю версию ветки master.

###### Клонирование репозитория

После того, как проект развёрнут в удалённом репозитории его можно клонировать на любой машине, где установлен git:
```bash
git clone git@github.com:alter-mind/GbPyDev.git
```

###### Управление удалёнными ветками

Локальные ветки и изменения в них не отражаются на удалённом репозитории, пока мы не отправим их туда при помощи команды **git push**

Список удалённых веток можно посмотреть в консоли при помощи команды **git branch** c параметром **-r**:
`git branch -r`
В отображении вывода удалённые ветки будут иметь префикс в виде имени удалённого репозитория. 

Чтобы удалить ветку на удалённом сервере нужно воспользоваться командой **git push**, имя ветки следует предварить двоеточием:
`git push origin :branch_to_delete`

Если требуется переименовать удалённую ветку, то сделать это одной командой довольно сложно. Проще всего создать на удалённом сервере копию ветки, а старую - удалить. В качестве примера рассмотрим переименование ветки fix_error в to_delete. 
```bash
git branch to_delete origin/fix_error
git push origin to_delete
git push origin :fix_error
```

###### Статус и навигация по git-проекту

Выяснить, на какой ветке мы сейчас находимся можно при помощи команд **git branch** или **git status**.

Если в качестве командной оболочки используется bash, то можно воспользоваться решением [git-aware-promt](https://github.com/jimeh/git-aware-prompt), которое встраивает название текущей ветки в подсказку командной строки. 

###### Как скрывать изменения

Если в ходе работы над веткой мы внесли изменения в какой-то файл и вынуждены срочной прерваться и перейти к работе с другой веткой, то могут быть плохо предсказуемые последствия, в лучшем случае незафиксированные изменения перейдут в другую ветку.  Чтобы этого не происходило нужно либо зафиксировать изменения в новом коммите, либо отложить их. 

Чтобы отложить изменения, нужно сперва добавить их в индекс командой **git add**, после чего можно выполнить команду **git stash**
```bash
git add .
git stash
```

Наши изменения не потеряны, они спрятаны в stash списке, их можно посмотреть при помощи команды
```bash
git stash list
```

После работы над другой веткой можно вернуться на исходную и вернуть данные из stash командой 
```bash
git stash apply
```
После чего, изменения, спрятанные в stash списке снова доступны для работы. 

Команду **git stash** можно выполнять несколько раз подряд в разных ветках, каждый раз в stash список будет добавляться новая запись, они пронумерованы цифрами начиная с 0. 

По умолчанию git использует последнюю запись, если вы хотите воспользоваться более ранним вариантом, можно явно указать метку stash записи: 
```bash
git stash apply stash@{1}
```

Держать много записей в стеше не является хорошей практикой, можно очистить список при помощи команды 
```bash
git stash drop
```

##### Версионирование
###### Классическая модель

Версии программного обеспечения, классически состоят из трёх чисел, разделённых точкой, первая называется мажорной, вторая минорной и третья - патч-версией. 

**Мажорная версия**, изменяется редка, как правило в результате крупных обновлений или кардинальной переработки продукта. 

**Минорная версия** отвечает за регулярные релизы, в рамках которых добавляется новый функционал, исправляются ошибки и происходит развитие программного продукта. 

**Патч-версия** не вносит изменения в возможности программного продукта, в её рамках, как правило, исправляются критические ошибки и уязвимости. 

###### Другие модели

Существуют и другие модели версионирования, некоторые дистрибутивы [[Base/Edu/IT_Knowledge/Linux|linux]] ориентируются на даты, некоторые программные продукты отмечают номера сборок

###### Весионирование в git 

Какая бы модель версионирования ни была выбрана, в системе контроля версий нужно отмечать коммит, отвечающий за версию, чтобы в любой момент времени была возможность собрать нужную версию программного продукта

###### Тэги

Для специальной пометки коммитов существуют механизм тэгов (меток). 

В больших проектах может быть огромное колличество коммитов, осуществлять навигацию по ним и найти нужный может быть затруднительно. 

Эту проблему решают метки - короткое запоминающееся название, по которому коммит легко найти среди других 

Метки - это тоже тэги, которые назначаются коммитам автоматически. Одному коммиту мы можем назначить любое количество тэгов. 

###### Создание тэга

Для создания тэга есть команда **git tag**:
```bash
git tag v1.1.0
```

При попытке создания уже существующего тэга git сообщает, что такой тэг уже существует.

Тэги можно снабжать комментариями, для этого метку тэга добавляем при помощи параметра **-a**, а комментарий при помощи параметра **-m**:
```bash
git tag -a v1.1.0 -m 'Комментарий к тэгу'
```

###### Просмотр тэгов

Для просмотра существующих тэгов вызываем команду **git tag** без параметров:
```bash
git tag
```

Для фильтрации вывода можно воспользоваться поиском по шаблону:
```bash
git tag -l v1.2.*
```

###### Удаление тэга

Чтобы удалить тэг, команде **git tag** следует указать параметр **-d**:
```bash
git tag -d v1.1.1
```

###### Связь коммита и тэга

Тэг - это всегда ссылка на коммит. На один и тот же коммит можно навесить множество тэгов. Хэш тоже можно рассматривать как тэг, но запомнить его гораздо сложнее, кроме того его название не информативно. 

Можно посмотреть описание коммита при помощи команды **git show**, обращаясь к нему по тэгу:
```bash
git show v1.1.0
```

Вместо тэга можно использовать хэш:
```bash
git show 037b3a
```

По умолчанию команда **git tag** устанавливает метку на текущий коммит. Однако мы может установить тэг и на совершенно произвольный коммит, для этого в конце команды указывается хэш нужного коммита:
```bash
git tag -a v0.3.5 -m 'Старая версия' abee3c4
```

Если необходимо поработать с проектом старой версии, мы можем отпочковать ветку от коммита, на которую указывает определённый тэг (вместа тэга можно использовать хэш коммита):
```bash
git checkout -b old_version_0_3_5 v0.3.5
```

###### Тэг HEAD
Помимо хэшей и наших собственных тэгов, git предоставляет несколько допольнительных тэгов, тэг **HEAD** указывает на последний коммит. 

###### Работа с тэгами в удалённом репозитории

По умолчанию **git push** не отправляет тэги на удалённый репозиторий, поэтому для отправки тэга необходимо явно указать его имя после команды **git push**:
```bash
git push origin v1.1.0
```

Используется та же комманда, что и для отправки веток, только вместо названия ветки мы указываем название тэга. 

Если перейти на страницу релизов на **GitHub**, то мы увидим, что тэг *v1.1.0* появился в удалённом репозитории. 

Выше мы отправили в удалённый репозиторий всего один тэг. Если тэгов много, можно отправить их все одной командой:
```bash
git push origin --tags
```

Для того, чтобы запросить тэги на удалённом сервере воспользуемся командой 
`git ls-remote`

Для удаления тэга на удалённом сервере используется тот же механизм, что и для удаления веток.
Так, команда 
`git push origin :v0.3.5` 
Удаляет тэг v0.3.5 c удалённого сервера
##### Слияния и переносы
###### Merge-request
Представим ситуацию, когда мы отпочковали от ветки *master* новую ветку *feature*, в каждой ветке было добавлено несколько коммитов, и теперь перед нами стоит задача добавить изменения из ветки *master* в ветку *feature*. 

Самое простое, что можно сделать в этой ситуации - смержить изменения из ветки *master* в ветку *feature*
```bash
git checkout feature
git merge master
```

###### git rebase

Cуществует альтернативный вариант решить задачу синхронизации изменений (см. [[Base/Edu/IT_Knowledge/GIT#Merge-request|предыдущий параграф]]). Вместо того, чтобы вливать в ветку *feature* изменения из ветки *master*, коммиты ветки *feature* перемещаются таким образом, чтобы ветка *feature* начиналась там, где заканчивается ветка *master*. В результате ветка feature будет содержать все коммиты ветки *master* + свои новые коммиты. 

**операция git rebase считается сложной и рискованной, затрагивает историю git, поэтому во многих компаниях она запрещена к использованию**. Или, во всяком случае, такая практика является нежелательной и прибегать к ней следует только в крайнем случае. 

Рассмотрим алгоритм действий. Переключаемся в ветку *feature*
`git checkout feature`
Смотрим разницу с веткой *master*
`git diff master`
Выполняем команду **git rebase**
`git rebase master`
Теперь наша ветка feature перемещена вперёд.

Но если мы попробуем закинуть её на удалённый сервер у нас ничего не получится, потому, что там всё ещё хранится прежний вариант ветки *feature*. Чтобы закинуть новый вариант ветки нужно принудительно перезаписать ветку. Для этого выполним команду **git push** с параметром **-f**:
`git push origin feature -f`

**-f** является сокращением от английского слова 'force'. Считается, что принудительное переписывание веток потенциально опасно и может повредить весь проект. Поэтому каждая команда разработки заранее договаривается, использовать **git rebase** или же нет. 

###### Перенос коммита

Иногда нужно перенести изменения из одной ветки в другую, а сливать изменения нельзя.  В этом случае можно перенести один или несколько коммитов при помощи команды **git cherry-pick**. Для этого перемещаемся в нужную ветку и выполняем команду **git cherry-pick**, в качестве параметра указываем хэш переносимого коммита:
`git cherry-pick 037b3a1`
При попытки слияние может возникнуть конфликт, устраняем его добавляем файлы в индекс и завершаем перенос:
`git cherry-pick --continue`

В результате в нужную ветку будет перенесён выбранный коммит. Его хэш поменяется, т.к. git считает его новым коммитом в другой ветке, однако вносимые изменения будут польностью совпадать с изменениями в исходном коммите. 

Иногда, коммитов, которые нужно перенести из одной ветки в другую может быть довольно много и переносить их поодиночке может быть утомительно, возрастает вероятность ошибок. 

###### Объединение коммитов

Несколько коммитов одной ветки можно объединить в один, например для того, что после перенести их в другую ветку коммандой **git cherry-pick**.
Для операции объединения используюется команда **git rebase -i**

Представим ситуацию, что в ветках *feature* и *master* есть несколько коммитов после их разделения и сейчас мы хотим перенести эти коммиты из ветки *feature* в ветку *master*
Выполняем команду **git cherry** с параметром **-v**, чтобы узнать насколько текущая ветка *feature* отличается от ветки *master*:
`git cherry -v master`
Знаем, что сослаться на последний коммит ветки можно при помощи тега *HEAD*.
`git show HEAD`
Если нам нужен коммит, предшествующий последнему, через тильду указываем значение 1:
`git show HEAD~1`
Так, меняя цифру, можно перебрать все коммиты ветки. 
Допустим, разница между ветками составляет 3 коммита, тогда посмотреть начальный коммит:
`git show HEAD~3`
Чтобы объединить коммиты, начиная с этого и до последнего выполняем комманду **git rebase -i**:
`git rebase -i HEAD~3`
В результате работы откроется файл, с описанием всех коммитов и перечислением того, что с ними можно сделать. Если перед каждым коммитом мы оставляем слово **pick** - *они остаются*, если же **squash** - *объединяются*. Должен остаться хотя-бы один коммит, помеченный как **pick**. Cохраняем файл. В результате git склеивает коммиты в один. 
Теперь ветка *feature* отличиется от *master* только одним коммитом. Так как мы воспользовались перезаписыванием истории проекта при помощи git rebase, то при отправке ветки на удалённый сервер потребуется перезаписать ветку *feature* при помощи парамера **-f** или **--force**. 



# Gitflow
По мере разрастания проекта, увеличивается и количество обслуживающих его людей. Рано или поздно поднимается вопрос, как координировать действия большой массы людей. Важно добиться чтобы на пользователях конечного продукта не отображались организационные изменения и чем крупнее проект, тем это более критично.

Новый функционал в продукт обычно добавляется небольшими порциями, которые выпускают в качестве релиза. В релизе важно добавить новые возможности, проверив что они работают именно так, как задумано, при этом не ломается старый функционал.  

Эта задача решается ручным и автоматическим тестированием. Полностю автоматизировать тестирование в сколь угодно сложном проекте. Прогнать каждую строку кода со всеми возможными вариантами данных потребует на порядок больше ресурсов, чем на разработку продукта. Поэтому совместно с автоматическим тестированием применяется ручное, при помощи которого тестировщики определяют наиболее часто встречающиеся сценарии ошибок. Они и становятся кандидатами для создания автоматического тестирования. 

Так, тестирование - главный барьер на пути обновлённой программы к пользователю. Следует организовать разработку так, чтобы код обязательно прошёл проверку тестировщиками. 

## Gitflow
В решении этой задачи помогает *gitflow* - набор позволяет управлять релизами проекта. Эти правила определяют, какие ветки нужно создавать и как проводить их слияние

Для работы по gitflow создаются две постоянные ветки: *master* и *develop* 

Ветка *master* создаётся по умолчанию при создании репозитория, она считается главное и в каждый момент код в ней должен быть готов к релизу. Это может быть новый или старый релиз, однако выкатка из него в продакш никогда не должна приводить к поломке. 

Ветка *develop* используется для разработки, в ней должны содержаться самые последние изменения, необходимые для следующего релиза. Когда код в этой ветке достигает стабильного состояния и готов к релизу, все изменения должны быть влиты в ветку *master* и помечены тэгом с номером релиза. 
Так, каждый раз когда изменения вливаются в ветку master, получается новый релиз. 

Помимо веток *master* и *develop* используются вспомогательные ветки для разработки и тестирования, в отличие от главных веток, они всегда имеют ограниченный срок жизни. В качестве вспомогательных веток используются:
- ветки задач, которые решают конкретные поставленные задачи.
- релизные ветки для сбора релиза
- hofix ветки для срочных исправлений 

###### Ветки задач
Ветки задач используются для разработки новых функций, чаще всего они отпочковываются от ветки develop. Такая ветка живёт столько, сколько разрабатывается новый функционал, после чего, как правило, ветка сливается в develop.

Как правило, в трекере задач, заводится тикет на функционал, номер задачи добавляется в название ветки, чтобы в любой момент времени можно было обратиться к трекеру за подробным описанием. 

###### Релизная ветка
Релизная ветка используюется для подготовки к выпуску новых версий продукта. Она нужна, чтобы в релиз попало не всё содержимое *develop* ветки, а лишь избранные задачи, например, новый, ещё не стабильный функционал. Благодаря такому подходу в релизной ветке проект может быть доведён до стабильного состояния, в то время, как в ветке develop может продолжаться разработка будущего функционала. 

Существует два подхода для формирования релизной ветки.
1. Согласно первому, она создаётся заранее, перед стартом релиза, её можно отпочковать от *develop*, если код в ней стабилен, либо же от *master*. В любом случае ветки задач сливаются в релизную ветку, по мере тестирования и нахождения ошибок ветка исправляется и в конце, стабильная релизная ветка сливается и в *develop* и в *master*.
2. Согласно второму подходу, релизная ветка формируется из веток задач по мере их готовности. При этом ветки задач не удаляются и в любой момент можно пересобрать релизную ветку, исключив из неё ту или иную задачу, либо же добавить новый функционал. При таком подходе важно отпочковывать ветки задач от master, и вносить изменения именно в ветки задач, так как релизная ветка в любой момент может быть удалена или пересобрана. После того, как релизная ветка сливается в *master* она, релизная ветка, может быть удалена, считается, что *master* ветка готова к релизу. При этом на ветку *master* ставится тэг с [[Base/Edu/IT_Knowledge/GIT#Версионирование|версией продукта]], как правило, при каждом релизе увеличивается минорная версия.

###### Hotfix ветки

Hotfix-ветки предназначены для срочных исправлений. В больших проектах бывает сложно протестировать всё до конца перед выпуском продукта. Продакшн среда может быть больше и сложнее устроена, чем тестовый стенд и включать интерграции которые сложно обеспечить на тестовом стенде. 

Как правило, изменения, которые нужно внести в код небольшие и очевидные. Всегда, когда это возможно, в случае возникновения ошибок или некорректного поведения проекта, релиз стараются откатить на предыдущую стабильную версию. 

Hotfix ветки всегда отпочковываются от *master*, и готовые изменения сливаются в *master* и в *develop*. Поскольку hotfix-ветка сливается в *master* на неё тоже ставится версия, при этом увеличивается номер патч-версии. 

###### Общая концепция

Так, мы имеем 4 параллельных потока:
- ветки задач (feature)
- *develop* c последней версией продукта
- релизная ветка с хотфиксами
- *master* стабильная ветка

Идеально, если каждый из этих потоков имеет собственный стенд. 
 - *master* - это продакшн окружение
 - *release* - релизная ветка и хотфиксы - это предпрод, среда максимально близкая по своим параметрам к продашн окружению
 - *develop* - это стейджинг окружение
 - *feature* - ветки задач - либо на втором стейджинге, либо на dev-машинах.

В разных компаниях может быть разная инфраструктура, в зависимости от возможностей и задач. У кого-то может быть только продашкн окружение, у кого-то в дополнение может быть только предпрод. У кого-то может быть полный набор окружений, десяткий стейджей или облачная инфраструктура, позволяющая разворачивать для тестирования каждую ветку задач. В зависимости от окружения работа выстраивается работа отдела тестирования. 