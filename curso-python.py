#Comentario

# Variables
variable_string = "holaMundo";
print (type(variable_string)) #print: imprimir en consola

x = 5
print(type(x)) #type: Getting the Data Type


numero1 = input("Ingresa un número: ")
numero2 = 6;
numero1 = int(numero1) #int(): especifica el tipo de dato, lo convierte a int
numero2 = int(numero2)
suma = numero1 + numero2;
print(str(suma))

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Data Types
    # Text Type:	str
    # Numeric Types:	int, float, complex
    # Sequence Types:	list, tuple, range
    # Mapping Type:	dict
    # Set Types:	set, frozenset
    # Boolean Type:	bool
    # Binary Types:	bytes, bytearray, memoryview
    # None Type:	NoneType

x = "Hello World" #Setting the Data Type
x = str("Hello World") #Setting the Specific Data Type

# Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Random Number
    # Python tiene un módulo incorporado llamado aleatorio que se puede usar para hacer números aleatorios:
import random

print("Random Number: ", random.randrange(1, 10))

# Specify a Variable Type
x = int(2.8) # y will be 2
y = float("3")   # z will be 3.0
z = str(3.0)  # z will be '3.0'

# Looping Through a String
    # Podemos recorrer los caracteres en una cadena, con un bucle for.
for x in "banana":
  print(x) #outside: b a n a n a

# String Length
    # La función len() devuelve la longitud de una cadena:
a = "Hello, World!"
print(len(a))

# Check String
    # Para verificar si una determinada frase o carácter está presente en una cadena, podemos usar la palabra clave in.
txt = "The best things in life are free!"
print("free" in txt) #outside: true/false

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")