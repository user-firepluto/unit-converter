#mass

def mass():
    unit1 = str(input('Starter unit: '))
    unit2 = str(input('Result unit: '))
    x = float(input('Value to be converted: '))

    if unit1 == 'mg' and unit2 == 'cg' or unit1 == 'cg' and unit2 == 'dg' or unit1 == 'dg' and unit2 == 'g' or unit1 == 'g' and unit2 == 'dag' or unit1 == 'dag' and unit2 == 'hg' or unit1 == 'hg' and unit2 == 'kg':
        x = x / 10
        print(x, unit2)
    elif unit1 == 'cg' and unit2 == 'mg' or unit1 == 'dg' and unit2 == 'cg' or unit1 == 'g' and unit2 == 'dg' or unit1 == 'dag' and unit2 == 'g' or unit1 == 'hg' and unit2 == 'dag' or unit1 == 'kg' and unit2 == 'hg':
        x = x * 10
        print(x, unit2)
    elif unit1 == 'mg' and unit2 == 'dg' or unit1 == 'cg' and unit2 == 'g' or unit1 == 'dg' and unit2 == 'dag' or unit1 == 'g' and unit2 == 'hg' or unit1 == 'dag' and unit2 == 'kg':
        x = x / 100
        print(x, unit2)
    elif unit1 == 'dg' and unit2 == 'mg' or unit1 == 'g' and unit2 == 'cg' or unit1 == 'dag' and unit2 == 'dg' or unit1 == 'hg' and unit2 == 'g' or unit1 == 'kg' and unit2 == 'dag':
        x = x * 100
        print(x, unit2)
    elif unit1 == 'mg' and unit2 == 'g' or unit1 == 'cg' and unit2 == 'dag' or unit1 == 'dg' and unit2 == 'hg' or unit1 == 'g' and unit2 == 'hg' or unit1 == 'g' and unit2 == 'kg':
        x = x / 1000
        print(x, unit2)
    elif unit1 == 'g' and unit2 == 'mg' or unit1 == 'dag' and unit2 == 'cg' or unit1 == 'hg' and unit2 == 'dg' or unit1 == 'hg' and unit2 == 'g' or unit1 == 'kg' and unit2 == 'g':
        x = x * 1000
        print(x, unit2)
    elif unit1 == 'mg' and unit2 == 'dag' or unit1 == 'cg' and unit2 == 'hg' or unit1 == 'dg' and unit2 == 'kg':
        x = x / 10000
        print(x, unit2)
    elif unit1 == 'dag' and unit2 == 'mg' or unit1 == 'hg' and unit2 == 'cg' or unit1 == 'kg' and unit2 == 'dg':
        x = x * 10000
        print(x, unit2)
    elif unit1 == 'mg' and unit2 == 'hg' or unit1 == 'cg' and unit2 == 'kg':
        x = x / 10000
        print(x, unit2)
    elif unit1 == 'hg' and unit2 == 'mg' or unit1 == 'kg' and unit2 == 'cg':
        x = x * 10000
        print(x, unit2)
    elif unit1 == 'mg' and unit2 == 'kg':
        x = x / 100000
        print(x, unit2)
    elif unit1 == 'kg' and unit2 == 'mg':
        x = x * 100000
        print(x, unit2)
    elif unit1 or unit2 == 'mg' or 'cg' or 'dg' or 'g' or 'dag' or 'hg' or 'kg':
        print('Invalid prompt')