from lab_3.lab_python_oop.geometric_figure import Geometric_figure
from lab_3.lab_python_oop.color_figure import ColorFigure

# Класс «Прямоугольник» наследуется от класса «Геометрическая фигура»
class Rectangle(Geometric_figure):
	def __init__(self, width, high, color):
		super().__init__("Rectangle")
		self.width = width
		self.high = high
		self.col = ColorFigure()
		self.col.colorproperty = color
		# self._color = ColorFigure(color)
		pass

	def area(self):
		return self.width * self.high
		pass

	def __repr__(self):
		return "(Width = {}, High = {}).\nArea of {} {} : {}\n"\
			.format(self.width, self.high, self.col.colorproperty, self.name, self.area())
		pass

	pass
