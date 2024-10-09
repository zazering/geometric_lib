import circle  # Импортируем модуль circle для расчетов, связанных с кругом
import square  # Импортируем модуль square для расчетов, связанных с квадратом

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}  """ Словарь для хранения размеров, необходимых для каждой комбинации фигуры и функции """

def calc(fig, func, size):
    """Вычисляет и выводит результат заданной функции для указанной фигуры."""
    assert fig in figs
    assert func in funcs

    """ Используем eval для динамического вызова соответствующей функции из модуля фигуры """
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} фигуры {fig} равен {result}')  # Выводим результат

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    
    while fig not in figs:
        fig = input(f"Введите название фигуры, доступные: {figs}:\n")
    
    while func not in funcs:
        func = input(f"Введите название функции, доступные: {funcs}:\n")
    
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Введите размеры фигуры через пробел (1 для круга и квадрата)\n").split(' ')))
    
    calc(fig, func, size)
