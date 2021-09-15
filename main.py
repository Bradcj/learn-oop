from agg import add, sub, mul, div

@add
def Opt1(opt, result):
    return opt + ' gives result as ' + str(result)

@sub
def Opt2(opt, result):
    return opt + ' gives result as ' + str(result)

@mul
def Opt3(opt, result):
    return opt + ' gives result as ' + str(result)

@div
def Opt4(opt, result):
    return opt + ' gives result as ' + str(result)

Opts = input('Enter the Mathematical Symbols (+, -, * ,/) => ')
n1 = int(input('Enter the 1st number => '))
n2 = int(input('Enter the 2nd number => '))

if Opts == '+':
    Opts = Opt1(n2,n1)
elif Opts == '-':
    Opts = Opt2(n2,n1)
elif Opts == '*':
    Opts = Opt3(n2,n1)
elif Opts == '/':
    Opts = Opt4(n2,n1)

print(Opts)
