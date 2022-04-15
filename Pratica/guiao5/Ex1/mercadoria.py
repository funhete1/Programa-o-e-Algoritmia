class Mercadoria():
	
	def __init__(self, designacao, peso, dono):
		self.designacao = designacao
		self.peso = peso/1000
		self.dono = dono

	def get_designacao(self):
		return self.designacao

	def set_designacao(self,designacao):
		self.designacao = designacao

	def get_peso(self):
		return self.peso

	def set_designacao(self,peso):
		self.peso = peso

	def get_dono(self):
		return self.dono
	
	def set_dono(self,designacao):
		self.dono = dono

	def __repr__(self):
		return f"{self.designacao}({self.dono},{self.peso} ton)"



