print("Debes de ingresar el valor sin el punto\n\nEjemplo de error => 13.000\n\nEjemplo valido => 13000")


try:

 pesetas=int(input("\n\nCantidad en pesetas : "))
except ValueError:
    print("Error!")


try:


 print(round(pesetas/166), "Euros")
except NameError:
    pesetas=""







