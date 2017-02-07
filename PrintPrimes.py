def PrintPrimeNumberInARange(n):

	for num in range (0,n+1):

		if num>0:

			for a in range(1,num):

				if num%2==0 and num!=2:

					break

				elif num%3==0 and num!=3:

					break

				elif num>n:

					break

				else:

					print num