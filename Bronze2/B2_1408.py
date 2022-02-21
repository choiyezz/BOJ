h, m, s = map(int, input().split(':'))
h1, m1, s1 = map(int, input().split(':'))

now = h*3600 + m*60 + s
start = h1*3600 + m1*60 + s1
time = start - now

if time < 0:
    time += 24 * 3600

hour = time//3600
minute = (time % 3600) // 60
sec = (time % 3600) % 60
print('%02d:%02d:%02d' % (hour, minute, sec))







