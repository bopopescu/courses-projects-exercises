class Sample():
	pass


y = Sample()
print(type(y))


class Dog():
	
	species = "mammal"
	
	def __init__(self,breed,name):
		self.breed = breed
		self.name = name


my_dog = Dog("Lab","Sammy")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)


class Circle():
	
	pi = 3.14
	
	def __init__(self,radius=1):
		self.radius = radius
		
	def area(self):
		return self.radius*self.radius * Circle.pi
	
	def set_radius(self,new_r):
		self.radius = new_r


mycircle = Circle(3)
mycircle.set_radius(999)
print(mycircle.area())

#INHERITANCE

class Animal():
	def __init__(self):
		print("Animal Created")
	
	def whoAmI(self):
		print("Animal")
	
	def eat(self):
		print("Eating")


class Dog2(Animal):
	
	def __init__(self):
		#Animal.__init__(self)
		print("Dog Created")
	
	def bark(self):
		print("Woof!")
	
	def eat(self):
		print("Dog eating!")
	


mydog = Dog2()
mydog.whoAmI()
mydog.eat()
mydog.bark()
mydog.eat()


#SPECIAL METHODS

class Book():
	def __init__(self,title,author,pages):
		self.title = title
		self.author = author
		self.pages = pages
	
	def __str__(self):
		return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
	
	def __len__(self):
		return self.pages
	
	def __del__(self):
		print("a book is destroyed!")

b = Book("Python","Kuba",250)
print(b)
print(len(b))
del b

