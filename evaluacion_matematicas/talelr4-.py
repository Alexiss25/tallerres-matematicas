# Sistema de registro de usuarios

usuarios = {} 

while True:
    print("Bienvenido al sistema de registro")
    print("1. Registrar usuario")
    print("2. Consultar usuario")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == "1" :
        documento = input("Ingrese su documento: ")
        if documento in usuarios:
            print("El documento ya está registrado.")
        else:
            nombres = input("Ingrese su nombre: ")
            apellidos = input("Ingrese su apellido: ")
            try:
                edad = int(input("Ingrese su edad: "))
                peso = float(input("Ingrese su peso: "))
                estatura = float(input("Ingrese su estatura: "))
            except ValueError:
                print("Error: Por favor, ingrese valores numéricos válidos para edad, peso y estatura.")
                continue
        
           
            usuarios[documento] = {
                "nombres": nombres,
                "apellidos": apellidos,
                "edad": edad,
                "peso": peso,
                "estatura": estatura
            }
            print("Registro exitoso.")
    
    elif opcion == "2" :
        documento = input("Ingrese el documento del usuario a consultar: ")
        if documento in usuarios:
            print("Datos del usuario:")
            print(f"Nombres: {usuarios[documento]['nombres']}\n"
                  f"Apellidos: {usuarios[documento]['apellidos']}\n"
                  f"Edad: {usuarios[documento]['edad']}\n"
                  f"Peso: {usuarios[documento]['peso']}\n"
                  f"Estatura: {usuarios[documento]['estatura']}")
        else:
            print("El documento no está registrado.")
    
    elif opcion == "3" :
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Datos incorrectos. Intente nuevamente, por favor.")