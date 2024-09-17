class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

#Exemplo de uso 
temp = Temperatura(13)

temp_celsius = 13
temp_fahrenheit = Temperatura.celsius_para_fahrenheit(temp_celsius)
print(f"{temp_celsius}ºC é igual a {temp_fahrenheit}ºF")

temp_fahrenheit = 55.4
temp_celsius = Temperatura.fahrenheit_para_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}ºF é igual a {temp_celsius}ºC")