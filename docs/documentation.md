# Документация проекта

## Общее описание решения

Данный проект представляет собой программу для вычисления площади и периметра фигур: круга и квадрата. Пользователь может выбрать фигуру, функцию (площадь или периметр) и ввести необходимые размеры. Программа использует динамическое выполнение кода для вызова соответствующих функций, определенных в модулях `circle` и `square`.

## How to use calculator

1. Запустите команду `python calculate.py`.
2. Введите название фигуры. Доступные варианты: Circle, Square.
3. Введите функцию: Area или Perimeter.
4. Введите размеры фигуры. Радиус для круга, одна сторона для квадрата.
5. Получите ответ!

## Math formulas

### Area
- **Circle:** \( S = \pi R^2 \)
- **Square:** \( S = a^2 \)
- **Rectangle:** \( S = ab \)
- **Triangle:** \( S = \sqrt{p \cdot (p-a) \cdot (p-b) \cdot (p-c)} \) где \( p \) — полупериметр.

### Perimeter
- **Circle:** \( P = 2\pi R \)
- **Square:** \( P = 4a \)
- **Rectangle:** \( P = 2a + 2b \)
- **Triangle:** \( P = a + b + c \)

## Описание функций

### Модуль `circle`

#### Функция `area(r)`

Вычисляет площадь круга.

**Параметры:**
- `r` (float): радиус круга.

**Возвращаемое значение:**
- float: площадь круга.

**Пример вызова:**
```python
area(5)  # Вернет 78.53981633974483

**История изменения проекта и их хеши**
8bb950d (HEAD -> documentation, origin/documentation) files was modified
b5b0fae (origin/develop, develop) L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d (origin/main, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
