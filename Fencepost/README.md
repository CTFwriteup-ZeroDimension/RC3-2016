# Fencepost (Pwn 150)
It was reverse 150 when I solved it.  
The process is trapped in a loop, and the way out is a local variable to be zero. The variable is declared after a char array, and the array will be written by strcpy. We got the change to overwrite the local variable. The char buffer is 44 bytes, so the payload is 44 bytes char and follows with four '\x00'.  
```
payload = 'a'*44 + '\x00'*4
```
