class Produto:
    cid = 0
    def __init__(self,nome,qntdisp,pbase) -> None:
        self.nome = nome
        self.qntdisp = qntdisp
        self.pbase = pbase
        Produto.cid +=1
        self.cid = Produto.cid
    def __repr__(self) -> str:
        return f"{self.cid} {self.nome}\t {self.qntdisp} {self.pbase} {((self.pbase * 23) / 100) + self.pbase}"
    def add_stock(self,value):
        self.qntdisp +=value


class Livro(Produto):
    def __init__(self, nome, qntdisp, pbase,autores = []) -> None:
        super().__init__(nome, qntdisp, pbase)
        self.autores = autores
    def get_nome(self):
        return self.nome
    def get_num_autores(self):
        return(len(self.autores))
    def add_autor(self,autor):
        self.autores.append(autor)
    def get_autores(self):
        return self.autores
        
    def __repr__(self) -> str:
        return f"{self.cid} {self.nome}\t {self.qntdisp} {self.pbase} {((self.pbase * 6)/100)+self.pbase}"

class Telemovel(Produto):
    def __init__(self, marca,modelo, qntdisp, pbase) -> None:
        nome = marca+modelo
        super().__init__(nome, qntdisp, pbase)
    
class Televisor(Produto):
    def __init__(self, marca,modelo, qntdisp, pbase,polegadas) -> None:
        nome = marca+modelo
        super().__init__(nome, qntdisp, pbase)
        self.polegadas = polegadas

class Electrodomestico(Produto):
    def __init__(self,nome, qntdisp, pbase) -> None:
        super().__init__(nome, qntdisp, pbase)
    def set_classe(self,classe):
        self.classe = classe
    
    

