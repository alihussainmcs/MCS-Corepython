# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following:
# D 100 (D --> deposit)
# W 200 (W --> withdrawal)

# Input  :
# D 300
# D 300
# W 200
# D 100
# Output : 500

depo = withd = 0
while True:
	data = input()
	if not data:
		break
	v = data.split(' ')
	for i in range(len(v)):
		if v[i] is 'D':
			depo += int(v[i+1])
		if v[i] is 'W':
			withd += int(v[i+1])
print(depo-withd)
	