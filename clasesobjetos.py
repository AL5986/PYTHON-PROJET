# Creamos una clase Coche()
class Coche():
  
  # Creamos propiedades de la clase Coche()
  largochasi=4
  anchochasi=1.8
  ruedas=4
  enmarcha=False
  
  #Creamos metodos o comportamientos de la clase Coche()
  def arrancar(self):
    self.enmarcha=True
  
  def estado(self):
    if(self.enmarcha):
      return "El coche esta en marcha"
    else:
      return "El coche esta parado"

# Creamos un objeto micoche, una instancia de la clase Coche()
micoche=Coche()

# Cambiamos el comportamiento de arrancar con lo cual cambiamos la propiedad enmarcha=True
micoche.arrancar()


print("El largo del chasi es: ",micoche.largochasi,"m")
print(micoche.estado())


micoche2=Coche()

print("El largo del chasi es: ",micoche2.largochasi,"m")
print(micoche2.estado())