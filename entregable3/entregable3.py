usuarios = []
usuario = []
contador_usuarios = 0




while contador_usuarios < 5:
    nombre= input("escribe tu nombre")
    usuario.append(nombre)
    apellido = input("escribe tu apellido")
    usuario.append(apellido)
    telefono = int(input("escribe tu telefono"))
    usuario.append(telefono)
    correo = input("escribe tu correo")
    usuario.append(correo)
    clave = input("clave")
    usuario.append(clave)
   
    usuarios.append(usuario)
    contador_usuarios +=1
    


for i in usuarios:
    print(i,)
