import circle
import square
import triangle

# Словарь для хранения функций по фигурам и операциям
figs = {
    'circle': {
        'perimeter': circle.perimeter,
        'area': circle.area
    },
    'square': {
        'perimeter': square.perimeter,
        'area': square.area
    },
    'triangle': {
        'perimeter': triangle.perimeter,
        'area': triangle.area
    }
}


def calc(fig, func, size):
    """Вычисляет значение для заданной фигуры и функции."""
    assert fig in figs, f"Figure '{fig}' is not available."
    assert func in figs[fig], (f"Function '{func}' is not available for "
                               f"figure '{fig}'.")

    result = figs[fig][func](*size)

    return result  # Возвращаем само значение


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, "
                    f"available are {list(figs.keys())}:\n")

    while func not in figs[fig]:
        func = input(f"Enter function name, "
                     f"available are {list(figs[fig].keys())}:\n")

    while len(size) != 1:
        if fig == 'triangle':
            size = list(map(int, input("Input three sides of the triangle "
                                       "separated by space:\n").split()))
            if len(size) != 3:
                print("Please enter exactly three sides for a triangle.")
                size = []
        else:
            size = list(map(int, input("Input figure size (1 for circle and "
                                       "square):\n").split()))

    result = calc(fig, func, size)
    print(f'The {func} of the {fig} is {result}.')
