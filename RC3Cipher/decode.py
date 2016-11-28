import subprocess
cipher = b'1b65380f084b59016875513c6373131d2a6a327172753a2918243d7b181a051e5f1e104c32331c0842777b375f100113'
cipher = [cipher[:idx+2] for idx in range(0, len(cipher), 2)]

def decode(offset, prefix, max_chr):
    if offset == len(cipher):
        if prefix.startswith(b'RC3-2016'):
            print('')
            print('flag:', prefix.decode('utf-8'))
            exit()
        return
    for x in range(1, max_chr+1):
        with subprocess.Popen(['./RC3Cipher', prefix + bytes([x, max_chr])], stdout=subprocess.PIPE) as proc:
            rd = proc.stdout.read()
        c = rd.strip().split(b'\n')[0]
        c = c.split(b': ')[1][:-2]
        if c == cipher[offset]:
            print('\r' + (prefix + bytes([x])).decode('utf-8'), end='')
            decode(offset+1, prefix + bytes([x]), max_chr)
known_text = b'RC3-2016'
for i in range(ord('R'), 128):
    decode(len(known_text), known_text, i)

