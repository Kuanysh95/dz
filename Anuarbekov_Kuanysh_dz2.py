class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calculation(self, weight=25, thickness=5):
        return f'Масса асфальта: {(self._lenght * self._width * weight * thickness) / 1000} т'


road = Road(5000, 20)
print(road.mass_calculation())