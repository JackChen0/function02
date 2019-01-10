x = []
def sum_list(number):
	x.append(number)
	return x

while True:
	y = int(input('Enter the number.'))
	sum_list(int(y))
	if y == 0:
		break 
print(sum(x))