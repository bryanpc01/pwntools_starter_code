from pwn import *

context.terminal = ['tmux', 'splitw', '-f', '-h']
context.arch = 'amd64'

debug = False
local = True

local_process = './path_to_file'                    # Change path to local binary here.
e = ELF(local_process)

r_host = 'offsec-chalbroker.osiris.cyber.nyu.edu'   # Change remote host here
r_port = xxxx                                       # Change remote port here

nyu_netID = b'abc123'                               # Change NYU NetID here

if local:
    if debug:
        context.log_level = 'debug'
        p = gdb.debug( local_process, '''
            b main
            continue
        ''')
    else:
        p = process(local_process)
else:
    p = remote( r_host, r_port)
    p.sendlineafter(b'abc123): ', nyu_netID)

# Add pwntools code below

# Add pwntools code above
p.interactive()
