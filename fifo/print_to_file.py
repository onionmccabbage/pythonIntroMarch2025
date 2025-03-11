def printOutput(t):
    '''Use print to commit the text 't' into a persistent text file'''
    # we need a file access object
    fout = open('my_text.txt', 'at') # 'a' will append 't' means text 
    # remember - print defaults to adding a new line at the end
    print(t, file=fout)
    # tidy up when done
    fout.close() # release the memory assets

# exercise the code
t = 'here is some information'
printOutput(t)