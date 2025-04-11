
class Vehiculo:
    '''
    clase usada para crear objetos de tipo vehiculo
    '''
    def __init__(self,marca, modelo, color, placa, anio, cilindraje, kilometraje, combustible, seguro, caja_de_cambio, gama, chasis, pais_de_origen, tipo_de_puertas,
                 valor, llanta_de_emergencia, numero_de_puertas):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._placa = placa
        self._anio = anio
        self._cilindraje = cilindraje
        self._kilometraje = kilometraje
        self._combustible = combustible
        self._seguro = seguro
        self._caja_de_cambio = caja_de_cambio
        self._gama = gama
        self._chasis = chasis
        self._pais_de_origen = pais_de_origen
        self._tipo_de_puertas = tipo_de_puertas
        self._valor = valor
        self._llanta_de_emergencia = llanta_de_emergencia
        self._numero_de_puertas = numero_de_puertas


    def __str__(self):
       return f"Vehiculo: {self.__dict__.__str__()}"
         #return (f"Vehiculo [marca: {self._marca}, modelo: {self._modelo}, color: {self._color}, placa: {self._placa},"
               # f"anio: {self._anio}]")



if __name__ == "__main__":
    objVehiculo1 = Vehiculo("Ford", "F150", "Negro", "GTE6663", 2016, "2", "0","Gasolina", "Si","Automatica", "Alta", "78942123", "USA", "Blindadas", "300000", "Si", "2")
    print(f"Marca: {objVehiculo1._marca}")
    print(f"Modelo: {objVehiculo1._modelo}")
    print(f"Color: {objVehiculo1._color}")
    print(f"Placa: {objVehiculo1._placa}")
    print(f"Anio: {objVehiculo1._anio}")
    print(f"Cilindraje: {objVehiculo1._cilindraje}")
    print(f"Kilometraje: {objVehiculo1._kilometraje}")
    print(f"Combustible: {objVehiculo1._combustible}")
    print(f"Seguro: {objVehiculo1._seguro}")
    print(f"Caja de cambio: {objVehiculo1._caja_de_cambio}")
    print(f"Gama: {objVehiculo1._gama}")
    print(f"Chasis: {objVehiculo1._chasis}")
    print(f"Pais de origen: {objVehiculo1._pais_de_origen}")
    print(f"Tipo de puertas: {objVehiculo1._tipo_de_puertas}")
    print(f"Valor: {objVehiculo1._valor}")
    print(f"Llanta de emergencia: {objVehiculo1._llanta_de_emergencia}")
    print(f"Numero de puertas: {objVehiculo1._numero_de_puertas}")

    #print(objVehiculo1)
    #print(id(objVehiculo1))
