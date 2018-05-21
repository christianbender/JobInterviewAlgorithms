def anagramCheck(a, b):
    assert isinstance(a, str) and isinstance(b, str)
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)
	
	
if __name__ == "__main__":
	print(anagramCheck("Tom Marvolo Riddle", "I am Lord Voldemort")) # => True
	print(anagramCheck("Hello", "olleH")) # => True
	print(anagramCheck("Hi", "hello")) # => False
