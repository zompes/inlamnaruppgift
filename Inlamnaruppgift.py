from os import system, name as os_name
from network_brython import connect, send
from browser import window, aio
j = window.jQuery

# anywhere when you want to clear the terminal/console
system('cls' if os_name == 'nt' else 'clear')
