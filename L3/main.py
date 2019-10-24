from L3.lab_python_oop.rectangle import Rectangle
from L3.lab_python_oop.circle import Circle
from L3.lab_python_oop.square import Square

def main():
	rect = Rectangle(3, 2, "'dark blue'")
	print(rect)
	circle = Circle(5, "'green'")
	print(circle)
	square = Square(5, "'red'")
	print(square)

if __name__ == "__main__":
	main()
