class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        lst =[]
        Kelvin = celsius + 273.15
        Farenheit = celsius * 1.80 + 32.00
        lst.append(Kelvin)
        lst.append(Farenheit)
        return lst
        


        