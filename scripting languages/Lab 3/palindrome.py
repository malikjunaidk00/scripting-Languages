#!/usr/bin/env python3
def testPalindrome(s):
	if (s.lower() == s.lower()[::-1]):
		print("{} is a palindrome string!".format(s))
	else:
		print("{} is not a palindrome string!".format(s))
		
		
def main():
	s = input("write a string to test palindrome: ")
	testPalindrome(s)

##############################################################################

if __name__ == "__main__":
	main()

