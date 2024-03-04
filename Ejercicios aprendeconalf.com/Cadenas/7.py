correo = input("Escribe tu correo para cambiar su dominio: ")
print(correo[:correo.find('@')] + '@ceu.es')