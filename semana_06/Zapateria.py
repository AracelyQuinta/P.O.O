
class Zapato:
    def __init__(self, tipo_de_calzado, uso_principal, color, talla):
        self.tipo_de_calzado = tipo_de_calzado
        self.uso_principal = uso_principal
        self.color = color
        self.talla = talla

    def mostrar_atributos_de_zapato(self):
        return f"Tipo de calzado: {self.tipo_de_calzado}, se lo usará en {self.uso_principal}, color: {self.color}, talla: {self.talla}"

# Subclase que hereda de Zapato

"""
    super().__init__(nombre, apellido, edad)
        self.tipo_de_paciente = tipo_de_paciente

    def clasificacion_por_edad(self):
        if self.edad < 1:
            print("Es un recien nacido")
        elif self.edad < 3:
            print("Es un bebe")
        elif self.edad < 11:
            print("Es un niño")
        elif self.edad < 18:
            print("Es un adolescente")
        elif self.edad < 59:
            print("Es un adulto")
        else:
            print("Es un adulto mayor")

    def mostrar_tipo_de_paciente(self):
        return f"Tipo de paciente: {self.tipo_de_paciente}"
"""





class Fabricar(Zapato):
    def __init__(self, tipo_de_calzado, uso_principal, color, talla, estilo_o_caracteristica, material_de_la_suela, pegamento_de_zapato):
        super().__init__(tipo_de_calzado, uso_principal, color, talla)
        self.estilo_o_caracteristica = estilo_o_caracteristica
        self.material_de_la_suela = material_de_la_suela
        self.pegamento_de_zapato = pegamento_de_zapato

    def mostrar_detalles_fabricacion(self):
        atributos_basicos = self.mostrar_atributos_de_zapato()
        return f"{atributos_basicos}. Estilo: {self.estilo_o_caracteristica}, Suela: {self.material_de_la_suela}, ¿Necesitas más pegamento?: {'Sí' if self.pegamento_de_zapato else 'No'}"

class venta(Zapato):
    def __init__(self, tipo_de_calzado, uso_principal, color, talla):
        super().__init__(self, tipo_de_calzado)
# Crear instancia
fabricar1 = Fabricar("zapatos deportivos", "deportes", "blanco", 40, "suaves y cómodos", "suela sintética", True)

# Mostrar resultado
print(fabricar1.mostrar_detalles_fabricacion())


