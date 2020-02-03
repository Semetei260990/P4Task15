import random

class Card:
	def __init__(self):
		self.masti = ['-червы', '-крести', '-ромби', '-пики']
		self.card = ['2', '3', '4', '5', '6', '7', '8', '9', 'Д', 'К', 'A', 'В']
		self.all = [i+x for i in self.card for x in self.masti]

	def remove(self):
		try:
			choice = random.choice(self.all)
			print(choice)
			self.all.remove(choice)
		except IndexError:
			print('В колоде нет карт')

card = Card()

def get_card():
	while True:
		print('--- Нажмите "q" что бы выйти ---')
		words = input()
		if words == 'q':
			break
		else:
			card.remove()

get_card()