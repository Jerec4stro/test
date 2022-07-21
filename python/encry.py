
def encriptar(texto):
    
    textofinal = ''

    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textofinal += chr(ascii)
    
    return textofinal

def desencriptar(texto):
    print("El texto a desencriptar es: " + texto) 
    textofinal = ''
    for letra in texto:
        
        ascii = ord(letra)
        ascii -= 1
        textofinal += chr(ascii)
    
    return textofinal





def EncriptarArchivo(rutaArchivo):
    archivo = open("texto.txt", 'r')
    texto = archivo.read()
    archivo.close()    
    
    TextoEncriptado = encriptar(texto)


    archivo = open('texto.txt', 'w')
    archivo.write(TextoEncriptado)
    archivo.close()
    print("[+] Archivo Encriptado Exitosamente ;)")




def DesencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()    
    
    textoDesencriptado = desencriptar(texto)


    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print("[+] Archivo Desencriptado Exitosamente. ")    


respuestaEoD = input('Presione la letra "E" para encriptar, o "D" para desencriptar:\n\n ')
rutaArchivo = input('Ingrese la ruta de el archivo: \n\n')

if respuestaEoD == "E":
    EncriptarArchivo(rutaArchivo)
else:
    DesencriptarArchivo(rutaArchivo)
