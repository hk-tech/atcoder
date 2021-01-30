S = input()
if 'AA' in S:
    print('NO')
    exit()
else:
    if S.replace('A', '') != 'KIHBR':
        print('NO')
        exit()
    else:
        for x in ['KAI', 'IAH']:
            if x in S:
                print('NO')
                exit()

print('YES')
        
