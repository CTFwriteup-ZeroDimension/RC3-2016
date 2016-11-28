# Log Me In (Reverse 100)
The flag is encrypted by XOR a key: 28537194573619560 = 0x65626D61726168.  
The key is stored in a int_64 type but read as a char, so just be careful with the int is stored with little endian. The key is 'harambe'. 
After XOR the encrypted flag and the key, we got the flag:  
RC3-2016-XORISGUD
