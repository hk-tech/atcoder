S = input()

iflag = False
cflag = False
tflag = False

for s in S:
    if not iflag and s in ('i', 'I'):
        iflag = True
    elif iflag and not cflag and s in ('c', 'C'):
        cflag = True
    elif iflag and cflag and not tflag and s in ('t', 'T'):
        tflag = True

if iflag and cflag and tflag:
    print('YES')
else:
    print('NO')