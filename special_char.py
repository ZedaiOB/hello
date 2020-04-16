"""" input given is a string containing special character character and integers if the no of special character in
the string is even print the even integers first followed by odd inciters ,vice-versa. eg - input [asdf#$@%23456]
output [23456] """





s = input()
c = 0
ans=''
ev,od=[],[]
sp = '~`!@#$%^&*()_-+={}[]:;?/>.<,\|'
for i in s :
    if i in sp :
        c += 1 
    if i.isdigit():
        if int(i) % 2 == 0 :
            ev.append(int(i))
        else :
            od.append(int(i))
if c % 2 == 0 :
    if len(ev) > len(od) :
        for i in range(len(od)):
            ans += str(ev[i])
            ans += str(od[i])
        for i in ev :
            if str(i) not in ans :
                ans += str(i)
    elif len(od) > len(ev) :
        for i in range(len(ev)):
            ans += str(ev[i])
            ans += str(od[i])
        for i in od :
            if str(i) not in ans :
                ans += str(i)
    else :
        for i in range(len(od)):
            ans += str(ev[i])
            ans += str(od[i])
else :
    if len(ev) > len(od) :
        for i in range(len(od)):
            ans += str(od[i])
            ans += str(ev[i])
        for i in ev :
            if str(i) not in ans :
                ans += str(i)
    elif len(od) > len(ev) :
        for i in range(len(ev)):
            ans += str(od[i])
            ans += str(ev[i])
        for i in od :
            if str(i) not in ans :
                ans += str(i)
    else :
        for i in range(len(od)):
            ans += str(od[i])
            ans += str(ev[i])

print(ans)