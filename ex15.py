from sys import argv

# argv requires that the user enter a filename
script, filename = argv

# Opens up the file and saves it to a text variable
txt = open(filename)

#Reads back the name of the file and opens its contents
print "Here's your file %r" % filename
print txt.read()

# Asks for the users file again and reads it out
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
txt.close()
