from abc import ABC, abstractmethod

# Абстрактный класс "Геометрическая фигура"
class Geometric_figure(ABC):
    def __init__(self, name):
        self.name = name
        pass

    @abstractmethod
    def area(self):
        pass
    pass
