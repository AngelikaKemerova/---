from lab_3.lab_python_oop.geometric_figure import Geometric_figure
from lab_3.lab_python_oop.color_figure import ColorFigure
import math

# Класс Круг
class Circle(Geometric_figure):
	def __init__(self, radius, color):
		super().__init__("Circle")
		self.radius = radius
		self.fc = ColorFigure()
		self.fc.colorproperty = color
		pass

	def area(self):
		return math.pi * (self.radius ** 2)
		pass

	def __repr__(self):
		return "\nRadius: {}.\nArea of {} {} : {}\n"\
			.format(self.radius, self.fc.colorproperty, self.name, self.area())
		pass

	pass
