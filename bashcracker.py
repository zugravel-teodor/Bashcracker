import os
import getpass
user = getpass.getuser()
os.system(f'echo echo "Bash code has been executed in your .bashrc using bashcracker." >> /home/{user}/.bashrc')