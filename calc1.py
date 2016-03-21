query = raw_input("\nType a query: ")

def main(val):
	result = eval(val)
	return "Result: " + str(result)

print main(query)
