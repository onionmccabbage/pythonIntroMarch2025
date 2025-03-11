def writeOutput(t):
    '''write the text 't' to a text file'''
    # we need a file access object
    fout = open('my_text.txt', 'at')
    fout.write(f'{t}\n') # here we add a new line character
    fout.close()# always a good idea to tidy up

# exercise the code
t = 'more content written to file'
writeOutput(t)