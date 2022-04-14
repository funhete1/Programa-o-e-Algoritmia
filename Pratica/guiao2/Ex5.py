class Alojamento():
    def __init__(self,codigo,nome,local,ppnoite,disponibilidade,avaliacao) -> None:
        self.__codigo =  codigo
        self.__nome = nome
        self.__local =  local
        self.__ppnoite = ppnoite
        self.__disponibilidade = disponibilidade
        self.__avaliacao = avaliacao
    
    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome
    
    def get_local(self):
        return self.__local

    def get_ppnoite(self):
        return self.__ppnoite
    
    def get_disponibilidade(self):
        return self.__disponibilidade
    
    def get_avaliacao(self):
        return self.__avaliacao

    def set_nome(self, nome):
        self.__nome = nome

    def set_ppnoite(self,ppnoite):
        self.__ppnoite = ppnoite

    def set_disponibilidade(self,tf):
        self.__disponibilidade = tf
    
    def set_avaliacao(self,value):
        self.__avaliacao = value
    
    def __repr__(self) -> str:
        return f"Codigo:{self.get_codigo()}\nNome:{self.get_nome}\nLocal:{self.get_local()}\nPreco por noite:{self.get_ppnoite()}\nDisponibilidade:{self.get_disponibilidade()}\nAvaliacao:{self.get_avaliacao}"
class Apartamento(Alojamento):
    def __init__(self, codigo, nome, local, ppnoite, disponibilidade, avaliacao, numdequartos) -> None:
        self.__numdequartos = numdequartos
        super().__init__(codigo, nome, local, ppnoite, disponibilidade, avaliacao)

    def get_numdequartos(self):
        return self.__numdequartos
    
class Quartodehotel(Alojamento):
        def __init__(self, codigo, nome, local, ppnoite, disponibilidade, avaliacao, tipo) -> None:
            self.t__ipo = tipo 
            super().__init__(codigo, nome, local, ppnoite, disponibilidade, avaliacao)
        
        def get_tipo(self):
            return self.tipo
        
        def __repr__(self) -> str:
            return super().__repr__()

def main():
    alojamento1 = Alojamento(123456,"Sonho belo", "Aveiro", 50.4,"Disponivel", 5)
    print(alojamento1)
    