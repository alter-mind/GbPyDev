---
aliases:
  - Семинар 3
tags: 
cssclasses:
---
###### Area links
- [[README|main doc]]
- [[web_tech_intro/readme|Знакомство с web технологиями]]
- [[web_tech_intro/sem3/homework|Домашняя работа]]
##### work notes

_______________________________
# classwork

### Задание 1

**Задача**: создать всплывающее диалоговое окно с произвольным текстом, например, "Привет, Мир!" c помощью JavaScript

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
      alert('Привет, мир!');
    </script>
  </body>
</html>
```

### Задание 2

**Задача**: вычислить результат 158 + 2 и вывести значение выражения в диалоговое окно. 

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
      alert(158 + 2);
    </script>
  </body>
</html>
```

### Задание 3

**Задача**: передать строковый параметр в диалоговое окно. Например, вывести "Привет, Алевтина!", где имя - это передаваемый параметр.

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
      let uname = 'UserName';
      alert(`Привет, ${uname}`);
    </script>
  </body>
</html>
```

### Задание 4

**Задача**: вызвать диалоговое окно с заголовком "Как вас зовут?" и подсказкой в поле ввода "Имя".
А затем вывести имя, которое ввели в поле ввода. 

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
      alert(`Привет, ${uname}`);
    </script>
  </body>
</html>
```

### Задание 5
**Задача**: написать функцию, выводящую в диалоговом окне текст и переменную.
Например, "Привет, Алевтина".
Где имя "Алевтина" это внешняя переменная. 
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
      function sayHello(uname) {
        alert(`Hello, ${uname}`);
      }
      sayHello(uname)
    </script>
  </body>
</html>
```

### Задание 6\*
**Задача**: вывести на экран в диалоговом окне текст с сообщением: "Вы уверены?" и кнопками "Ок", "Отмена". 
- При нажатии на кнопку "Ок" вывести в диалоговом окне текст с сообщением "Мы рады, что вы уверены!"
- При нажатии на кнопку "Отмена" вывести текст с сообщением "Жаль, что вы не уверены..."
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
      let answer = confirm('Вы уверены?');
      if (answer) {
        alert('Мы рады, что вы уверены!');
      } else {
        alert('Жаль, что вы не уверены...')
      }
    </script>
  </body>
</html>
```

### Задание 7\*
**Задача**: перепишите код, используя конструкцию `switch-case`, запрашивая возраст пользователя через диалоговое окно. 
```html
<script>
	let age = 101;
	if (age == 18) {
		alert('Вы совершеннолетний, вам всё можно');
	} else if (age == 10) {
		alert('Вам надо учить уроки!');
	} else if (age == 30) {
		alert('Ложитесь спать, завтра на работу');
	} else {
		alert('Мы не знаем, что вам делать');
	}
</script>
```

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
      let answer = parseInt(prompt('Укажите свой возраст', '30'))
      switch(answer) {
        case 18:
          alert('Вы совершеннолетний, вам всё можно');
          break;
        case 10:
          alert('Вам надо учить уроки');
          break;
        case 30:
          alert('Ложитесь спать, завтра на работу');
          break;
        default:
          alert('Мы не знаем, что вам делать')
      }
    </script>
  </body>
</html>
```