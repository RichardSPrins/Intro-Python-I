"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as f:
  read_text = f.read()

print(read_text)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file_object = open('bar.txt', 'w')
file_object.write('first line\n')
file_object.write('second line\n')
file_object.write('third line\n')
file_object.close()

with open('bar.txt', 'r') as x:
    read_data = x.read()


print(read_data)