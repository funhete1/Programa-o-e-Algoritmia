class Vagao():
	def __init__(self,peso):
		self.peso = peso
		self.conteudo = []
	def get_peso(self):
		return self.peso

	def add_cargo(self,cargo):
		self.conteudo.append(cargo)

	def get_conteudo(self):
		return self.conteudo

	def total_weight(self):
		return sum(map(lambda x: x.get_peso(), self.conteudo))
	
	def __repr__(self):
		return f"Conteudo: {self.conteudo}\n\rPeso: {self.peso}"



