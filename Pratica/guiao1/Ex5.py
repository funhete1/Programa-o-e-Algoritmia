class Aluno:
    def __init__(self,__nome,__mec,__curso):
        self.mec = __mec
        self.nome = __nome
        self.curso = __curso
    def set_num_mec(self, __mec):
        self.mec = __mec
    def __repr__(self):
        return f"Aluno: {self.mec}; {self.nome}; {self.curso}"
class Livro:
    Id = 100
    def __init__(self,__name,__type ="Normal"):
        self.id = Livro.Id
        self.name = __name
        self.type = __type
        Livro.Id +=1
    def getId(self):
        return f"{self.id}"
    def getTitulo(self):
        return f"{self.name}"
    def setTipoEmprestimo(self,__type):
        self.type = __type
    def __repr__(self):
        return f"Livro {self.id}: {self.name}, {self.type}"
        

def main():
    livro1= Livro("Java 8", "CONDICIONAL");
    print(livro1)
    catalogo=[]
    catalogo.append(livro1)
    catalogo.append(Livro("POO em Java 8"))
    catalogo.append(Livro("Java para totós", "NORMAL"))
    print(f"ID = {catalogo[1].getId()} Título = { catalogo[1].getTitulo()}")
    catalogo[2].setTipoEmprestimo("CONDICIONAL")
    for livro in catalogo:
        print(livro)
    # Alunos        
    utilizadores=[] 
    utilizadores.append(Aluno("Catarina Marques", 80232, "MIEGI"))
    utilizadores.append(Aluno("Joao Silva", 90123, "Lic Física"))
    utilizadores[1].set_num_mec(80123)
    utilizadores.append(Aluno("António Costa", 100123, "Lic Matemática"))
    for aluno in utilizadores:
        print(aluno)
main()