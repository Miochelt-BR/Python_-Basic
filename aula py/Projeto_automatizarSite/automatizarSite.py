import webbrowser as wb
import random as rd

print(" seja bem vindo ")

print('-------------------------')
print('  Sites Favoritos  |')
print('-------------------------')

def randomica():
	ran = rd.randint(1, 5) 
	if ran == 1:
		wb.open('https://www.google.com/')
	elif ran == 2:
		wb.open('https://github.com/github')
	elif ran == 3:
		wb.open('https://www.youtube.com/')
	elif ran == 4:
		wb.open('https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo')
	elif ran == 5:
		wb.open('https://web.whatsapp.com/')
		
def main():
	while True:	
		print('GOOGLE[1], GIT[2], YOUTUBE[3], Linkdin[4], web.whatsapp[5], RANDOMIZAR[6], EXIT[7].')
		x = int(input('>>>'))
		#Condições:
		if x == 1:
			wb.open('https://www.google.com/')
		elif x == 2:
			wb.open('https://github.com/github')
		elif x == 3:
			wb.open('https://www.youtube.com/')
		elif x == 4:
			wb.open('https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo')
		elif x == 5:
			wb.open('https://web.whatsapp.com/')
		elif x == 6:
			randomica()
		elif x == 7:
			input('Aperte enter para sair.')
			break
		else:
			print('Opção não aceita, por favor digite uma opção válida.')
		print()		
main()