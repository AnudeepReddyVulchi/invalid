str = raw_input()
ab = ['a','e','i','o','u','A','E','I','O','U']
list = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
if (str in ab):
	print("vowel")
elif (str in list):
	print("consonant")
else:
	print("invalid")
