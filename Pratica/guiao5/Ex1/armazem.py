class Armazem:
	def __init__(self,localidade):  # sempre que inicializar um armazem uma fila de mercadorias e criada
									# e ao inicializar e necessario informar a localidade do armazem
		self.localidade = localidade
		self.fila = []
	
	def receber(self,mercadoria): 	# sempre que invocada introduz a mercadoria ao final da fila 
									# mantendo assim a ordem de chegada
		self.fila.append(mercadoria)

	def get_fila(self):
		return self.fila

	def entregar(self, element):
		self.fila.remove(element)

	def __repr__(self):
		return f"Armazem em {self.localidade}\n\rPara embarcar: {self.fila}"