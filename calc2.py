query = raw_input("\nType a query: ")

def main(val):
	try:
		if "+" in val or "-" in val or "*" in val or "/" in val or "**" in val:
			result = eval(val)
			return "Result: " + str(result)
		else:
			return "\nPlease, just use numbers."
	except SyntaxError:
		return "\nSyntax Error, please try again."
		
print main(query)
