# RC3Cipher (Reverse 350)
1. I find the encrpyted string to be accepted.  
```
'1b65380f084b59016875513c6373131d2a6a327172753a2918243d7b181a051e5f1e104c32331c0842777b375f100113'
```
2. There are many steps in the program but I notice that the largest order of char plays an important role. (Many functions use the value.)
3. Try some input and find out that given the largest order of char, the previous cipher text won't change. It seems that it encrypts the input from the first char to the last char.
4. So we can try to find the input char by char.  
## Decode process
1. Find out what combination of the first character and the largest order can get '1b'. Using the property 3 I found, I can append any character.  
Example: aa, ab, ac, bb, bc, ...
2. Find the char one by one and we get.  
```
$ python3 decode.py 
RC3-2016-Y0UR-KSA-IS-BAD-@ND-Y0U-SH0ULD-F33L-BAD 
flag: RC3-2016-Y0UR-KSA-IS-BAD-@ND-Y0U-SH0ULD-F33L-BAD
```  
The code:  
``` python3
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
```
