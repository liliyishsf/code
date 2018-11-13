import string
def main():
	c=raw_input('input a string:')
	if c.isalpha():
		print ('letter')
	elif c.isdigit():
		print 'number'
	else:
		print 'other'
if __name__=='__main__':
	main()
