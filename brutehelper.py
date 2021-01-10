
pw = input(" \u001b[31mwhat is your password: ")
print("")


 #simple

print(pw.upper())
print(pw.lower())


 #numbers

print(pw + "123")
print(pw + "1")
print(pw + "2")
print(pw + "3")
print(pw + "0000")
print(pw + "000")
print(pw + "1111")
print(pw + "111")

 #capitals

print(pw.capitalize())
print(pw.capitalize() + "1")
print(pw.capitalize() + "2")
print(pw.capitalize() + "123")
print(pw.capitalize() + "12345")
print(pw.capitalize() + "321")
print(pw + "2")

# full upper/lower and symbols
print(pw.capitalize().replace("s", "$") + "123")
print(pw.capitalize().replace("s", "$") + "1")
print(pw.capitalize().replace("s", "$") + "321")

print(pw.capitalize().replace("s", "$",).replace("o", "0") + "1")
print(pw.capitalize().replace("s", "$",).replace("o", "0"))
print(pw.capitalize().replace("s", "5",).replace("o", "0").replace("l", "1"))
print(pw.upper())
print(pw.lower())

print("""
list finished. \u001b[0m""")