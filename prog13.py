import itertools
letters="SENDMORY"
for p in itertools.permutations('0123456789',8):
    s=dict(zip(letters,p))
    if s['S']=='0' or s['M']=='0': continue
    send=int(s['S']+s['E']+s['N']+s['D'])
    more=int(s['M']+s['O']+s['R']+s['E'])
    money=int(s['M']+s['O']+s['N']+s['E']+s['Y'])
    if send+more==money:
        print(send,more,money)
        break
