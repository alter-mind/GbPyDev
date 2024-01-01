---
aliases:
  - Знакомство с web технологиями. Домашняя работа к 3-му семинару
tags:
  - homeworks
  - web
  - JS
cssclasses:
---
###### Area links
- [[README|main doc]]
- [[web_tech_intro/readme|Знакомство с web технологиями]]
- [[web_tech_intro/sem3/classwork|Семинар 3]]
##### work notes

_______________________________
# homework

Создать страницу, которая спрашивает имя у пользователя и выводит его с помощью функции.

Копирует [[web_tech_intro/sem3/classwork#Задание 4|Задание 4 с семинара]]
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <p>Это обычный HTML документ</p>
    <script type="text/javascript">
      let uname = prompt('Introduce youreself, please:', 'Username');
      alert(`Hello, ${uname}`);
    </script>
  </body>
</html>
```