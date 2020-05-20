"""
このファイルに解答コードを書いてください
"""
with open('input.txt') as f:
    lines = [l.strip().split(':') for l in f.readlines()]
    m = 0
    for i in range(0,len(lines)-1):
        if i == len(lines):
            m = int(lines[i][0])
        
        else:
            n = int(lines[i][0])
            s = lines[i][1]
            lines[i][0] = n

    m = int(lines[-1][0])
    lines.pop(-1)
    lines.sort(key=lambda x: x[0])
    ans = ''
    judge = False
    for l in lines:
        if m % l[0] == 0:
            ans += l[1]
            judge = True
    
    if judge:
        print(ans)
    else:
        print(2)


    

