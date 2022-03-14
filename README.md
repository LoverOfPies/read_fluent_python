# Конспект по книге Рамальо Лучано - Python. К вершинам мастерства - 2016 

## Часть 1. Пролог

### Глава 1. Модель данных в языке Python

#### Были рассмотрены:

#### 1) Колода карт на Python
* Пример в модуле __french_deck.py__

#### 2) Как используются специальные методы.
* Специальные методы предназначены для вызова интерпретатором.
* Как правило, специальный метод вызывается неявно.
* Если необходимо обратиться к специальному методу, то обычно лучше вызвать 
соответствующую встроенную функцию.

#### 3) Эмуляция числовых типов
* Пример в модуле __vector.py__

#### 4) Строковое представление
* Специальный метод \_\_repr__ вызывается встроенной функцией repr для получения строкового представления объекта.
* Интерактивная оболочка и отладчик вызывают функцию repr, передавая ей результат вычисления выражения.
* Строка, возвращаемая методом \_\_repr__, должна быть однозначно определена и по возможности соответствовать коду, необходимому для восстановления 
объекта.
* В отличие от \_\_repr__, метод \_\_str__ вызывается конструктором str() и неявно используется в функции print.
* Если вы реализуете только один из этих двух методов, то пусть это будет 
\_\_repr__, потому что в отсутствие пользовательского метода \_\_str__ интерпретатор Python вызывает \_\_repr__.

#### 5) Булево значение пользовательского типа
* Хотя в Python есть тип bool, интерпретатор принимает любой объект в булевом 
контексте, например в условии if, в управляющем выражении цикла while или в 
качестве операнда операторов and, or и not. Чтобы определить, является ли выражение истинным или ложным, применяется функция bool(x), которая возвращает 
True или False.
* По умолчанию любой объект пользовательского класса считается истинным, 
но положение меняется, если реализован хотя бы один из методов \_\_bool__ или \_\_len__.
* Функция bool(x), по существу, вызывает x.\_\_bool__() и использует полученный результат. Если метод \_\_bool__ не реализован, то Python пытается вызвать 
x.\_\_len__() и при получении нуля функция bool возвращает False. В противном случае bool возвращает True.

#### 6) Сводка специальных методов
|Категория| Имена методов                                                           |
|----------|-------------------------------------------------------------------------|
|Представление в виде строк и байтов| __repr__, __str__, __format__, __bytes__                                |
|Преобразование в число| __abs__, __bool__, __complex__, __int__, __float__, __hash__, __index__ |

TODO: Разобраться с таблицами, как проще оформить

#### 7) Почему len – не метод
* Функция len(x) работает очень быстро, если x – объект встроенного типа. Для 
встроенных объектов интерпретатор CPython вообще не вызывает методы, а просто читает значение, 
хранящееся в поле C-структуры.
* Иначе говоря, len не вызывается как метод, потому что играет особую роль 
в модели данных Python, равно как и abs. Но благодаря специальному методу 
\_\_len__ можно вызывать функцию len и для пользовательских объектов.

#### 8) Резюме

* Благодаря реализации специальных методов пользовательские объекты могут 
вести себя, как встроенные типы. Это позволяет добиться выразительного стиля 
кодирования, который сообщество считает «питоническим».
* Важное требование к объекту Python – обеспечить полезные строковые 
представления себя: одно – для отладки и протоколирования, другое – для показа пользователям. 
Именно для этой цели предназначены специальные методы \_\_repr__ и \_\_str__.

