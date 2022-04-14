from armazem import Armazem
from mercadorias import Mercadoria
from comboio import Comboio

def main():
    armazem_origem = Armazem("Aveiro")
    
    # receber mercadorias - Mercadoria tem designação, peso (Kg) e dono
    armazem_origem.receber(Mercadoria("Mercedes 200",3000,"Automotor"))   
    armazem_origem.receber(Mercadoria("Renault Twingo",2000,"XPTZ"))
    armazem_origem.receber(Mercadoria("BMW",4000,"XPTZ"))
    armazem_origem.receber(Mercadoria("Peças auto",7000,"XPTZ"))
    armazem_origem.receber(Mercadoria("Parafusos",4000,"CP CARGO"))
    armazem_origem.receber(Mercadoria("Cereais",4000,"CP CARGO"))
    armazem_origem.receber(Mercadoria("Motos",5000,"APRILIA"))

    # criar comboio com 3 vagões, todos com carga máxima de 10 toneladas
    comboio = Comboio([10, 10, 10])

    # carregar comboio com o que está em armazém
    comboio.carregar(armazem_origem)
    print(comboio)

    # fazer viagem e descarregar no destino
    comboio.fazer_viagem()
    comboio.descarregar()  # descarrega e mostra

    # mostrar o que ficou por enviar
    print(armazem_origem)


if __name__ == "__main__":

    main()
