import random
from termcolor import colored

count = 0
wrong = []
question = 0
for i in range(10):
	question += 1
	n = ''
	for section in range(4):
		n = n + str(random.randint(1,255))
		n = n + '.'
	ip = n[:-1]
	octet = ip.split('.')
	octet = str(octet[0])
	octet = int(octet)
	if octet == 127:
		octet = 128
		ip = ip.split('.')
		ip = ip[-1:]
		ip.insert(0,128)
		ip = '.'.join(ip)
	ipclass = ''
	print(str(question) + ')','Which class does this IP address belong to?',colored(ip,'blue'))
	answer = input('Enter a-e: ')
	if 1 <= octet <= 126:
		ipclass = 'a'
	elif 128 <= octet <= 191:
		ipclass = 'b'
	elif 192 <= octet <= 223:
		ipclass = 'c'
	elif 224 <= octet <= 239:
		ipclass = 'd'
	elif 240 <= octet <= 255:
		ipclass = 'e'
	if answer == ipclass:
		count += 1
	else:
		incorrect =str(question) + ') ' + ip + ' is in class ' + ipclass
		wrong.append(incorrect)
print('\nYou scored:',colored(count,'green'), 'out of 10.')
if len(wrong) != 0:
	print(colored('\nIncorrect answers:', 'red'))
	for x in wrong:
		print(x)
