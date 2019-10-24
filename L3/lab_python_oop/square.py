from lab_3.lab_python_oop.rectangle import Rectangle
from lab_3.lab_python_oop.color_figure import ColorFigure

# Класс Квадрат
class Square(Rectangle):
	FIGURE = "Square"

	@classmethod
	def get_figure_type(cls):
		return cls.FIGURE

	def __init__(self, x, color):
		self.x = x
		self.col = ColorFigure()
		self.col.colorproperty = color
		pass

	def area(self):
		return self.x * self.x
		pass

	def __repr__(self):
		return "\nLength: {}.\nArea of {} {} : {}\n"\
			.format(self.x , self.col.colorproperty, self.get_figure_type(), self.area())
		pass

	pass
