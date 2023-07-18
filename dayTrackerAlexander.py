
class Lunch:
	def __init__(self):
		self.name = "Hello"
	
	def __repr__(self):
		return self.name

welcome = """Merci de selectionner le type de la nouvelle entree:
1: repas
2: sommeil
3: activite
4: toilette"""
print(welcome)
typeAnswer = input()
print(typeAnswer)


# print("New entree!")
# #newEntrees = input()
# newEntrees = Lunch()

# print(newEntrees)