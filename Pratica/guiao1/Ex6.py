class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def __repr__(self) -> str:
        return f"{self.dia}:{self.mes}:{self.ano}"
    def nextDay(self):
        if self.dia < Data.monthDays(self.mes,self.ano):
            self.dia += 1
        else:
            self.dia= 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        return self.__repr__()
    def monthDays(mes,ano):
        if mes in (1, 3, 5, 7, 8, 10, 12):
            month_length = 31
        elif mes == 2:
            if Data.bissexto(ano):
                month_length = 29
            else:
                month_length = 28
        else:
            month_length = 30
        return month_length
    def bissexto(ano):
        if (ano % 400 == 0):
            leap_year = True
        elif (ano % 100 == 0):
            leap_year = False
        elif (ano % 4 == 0):
            leap_year = True
        else:
            leap_year = False
        return leap_year

def main():
    data1 = Data (28,2,2022)
    print(data1)
    data1.nextDay()
    print (data1)
    print(f"Month 2 of 2022 has {Data.monthDays(2, 2022)} days")
main()