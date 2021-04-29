import pandas as pd
import random

file = input('Enter csv file: ')
c1 = ord(input('Enter x variable column letter (ie A, B, C, etc.): ')) - 65
c2 = ord(input('Enter y variable column letter (ie A, B, C, etc.): ')) - 65


df = pd.read_csv(file, header=None)
df = df.iloc[:, [c1, c2]]

try:
    maxim = float(df.iloc[:, 1].max())
    minum = float(df.iloc[:, 1].min())
except:
    print('Nonnumber types in csv columns, please clean up data')
    exit()

Area = (float(df[0].iloc[-1]) - float(df[0].iloc[0])) * (maxim - minum)

n = input('How many times? ')
count = {'for': 0, 'total': 0}
for i in range(int(n)):
    count['total'] += 1
    index = random.randrange(0, len(df[0]))
    num = random.uniform(float(minum), float(maxim))
    val = float(df[1].iloc[index])
    if val > 0:
        if 0 < num < val:
            count['for'] += 1
    elif val < 0:
        if val < num < 0:
            count['for'] -= 1
Fraction = count['for'] / (count['total'])
Integral = Area * Fraction
    
print(Integral)