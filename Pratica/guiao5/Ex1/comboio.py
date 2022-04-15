from vagoes import Vagao

class Comboio():
	def __init__(self,maximums):
		self.vagoes = []
		for i in maximums:
			self.vagoes.append(Vagao(i)) 

	def get_vagoes(self):
		return self.vagoes

	def set_vagoes(self,novo_vagao):  # adiciona novos vagoes ao comboio 
		for i in novo_vagao:
			self.vagoes.append(Vagao(i))	
	
	def carregar(self,armazem):
			index  = 0
			weight = self.vagoes[index].get_peso()
			for i in armazem.get_fila():
				if weight - i.get_peso() < 0:
					index += 1
					if index == len(self.vagoes):
						print(f"Necessário novo vagão. Disponíveis {weight} toneladas e mercadoria pesa {i.get_peso()} toneladas.")
						print("AVISO! Não existem mais vagões vazios")
						break
					print(f"Necessário novo vagão. Disponíveis {weight} toneladas e mercadoria pesa {i.get_peso()} toneladas.")
					weight = self.vagoes[index].get_peso()
					self.vagoes[index].add_cargo(i)
					weight -= i.get_peso()
					print(f"Carregando {i.get_designacao()},{i.get_dono()},{i.get_peso()} " + 
						f"no vagao Vagão de Mercadorias n.{index+1},Carga máx={self.vagoes[index].get_peso()}")
					continue
				weight -= i.get_peso()
				self.vagoes[index].add_cargo(i)
				print(f"Carregando {i.get_designacao()},{i.get_dono()},{i.get_peso()}" +
					f" no vagao Vagão de Mercadorias n.{index+1},Carga máx={self.vagoes[index].get_peso()}")
	
	def fazer_viagem(self):
		print("LOCOMOTIVA\n\rPartida........ viagem .....Chegada.")

	def descarregar(self):
		for i in self.vagoes[::-1]:
			print(f"Início da descarga de Vagão{self.vagoes.index(i)+1}[carga={i.total_weight()}, carga max = {i.get_peso()}\n")
			for j in i.get_conteudo():
				print(f"{j.designacao},{j.dono},{j.peso}")


	def __repr__(self):
		print("COMBOIO:")
		for vagoes in self.vagoes[::-1]:
			print(f"\rVagão de Mercadorias n.{self.vagoes.index(vagoes)+1}, Carga máx = {vagoes.get_peso()} toneladas")
		return ""   # return a empty string just so i can run the main code as wanted

