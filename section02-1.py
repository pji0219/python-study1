# 기본 출력
print('hello, python!')
print("hello, python!")
print("""hello, python!""")
print('''hello, python!''')

print()

# separator 옵션 사용
print('T', 'E', 's', 'T', sep='')
print('2020','02','19', sep='-')
print('niceman', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end='')
print('the black parade', end='')
print('piano notes')

print()

# format 사용
print('{} and {}'.format('You', 'Me'))
print('{} and {} and {}'.format('You','Me'))
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))

print()

# %s, %d, %f
print("Test1: %5d, price: %4.2f" %(776, 6534.123))
print("Test1: {0:5d}, price:{1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, price{b: 4.2f}".format(a=776, b=6534.123))
