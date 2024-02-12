n = input('Digite algo:')
print(type(n) , n.isalnum() , n.isalpha() , n.isalnum())

print('{0} , {1} , {2} , {3}'.format(type(n) , n.isalnum() , n.isalpha() , n.isalnum()))
# Simplificando o .format:
print(f'{type(n)} , {n.isalnum()} , {n.isalpha()} , {n.isalnum()}')