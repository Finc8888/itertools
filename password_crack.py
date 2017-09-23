import random as r
import itertools as it
tup = [r.randint(0,9) for i in range(4)]
# print(tup)
a,b,c,d = tup
pswd = '{}{}{}{}'.format(a,b,c,d)
# pswd = '9547'
# print(pswd)

while True:
	ans = input("Для входа в систему введите пароль из 4 неповторяющихся цифр\n")
	crack = it.permutations(range(10),4)
	if ans == 'c':
		while True:
			i = next(crack)
			e,f,g,h = i
			pswd_crack = '{}{}{}{}'.format(e,f,g,h)
			# print(pswd_crack)
		    # ans = pswd_crack
			if pswd == pswd_crack:
				print("Искомый пароль",pswd_crack)
				break
	elif pswd == ans:
		print("Добро пожаловать в систему",pswd)
		break
	elif ans == '' or ans == 'q':
		break
	else:
		print("Пароль не верен, попробуйте снова")
