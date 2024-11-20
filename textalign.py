
width = 50
# right aligned 
print("This text is aligned right".rjust(width, '-'))

#  center aligned  

print("This text is Center aligned".center(width, '-'))

# left aligned 

print("This text is left aligned".ljust(width, '-'))

# it is optional to add the a fill value after the length of the width of the string
print("On the left".rjust(width)+" joined here "+"On the right".ljust(width,"*"))