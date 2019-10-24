# Класс «Цвет фигуры» содержит свойство для описания цвета геометрической фигуры
class ColorFigure:
	def __init__(self):
		self.color = None
		pass

	@property
	def colorproperty(self):
		return self.color
		pass

	@colorproperty.setter
	def colorproperty(self, color):
		self.color = color
		pass
	pass
