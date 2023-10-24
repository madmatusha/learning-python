# уберём вызов !python2.6
import sys

print(sys.version.split()[0])

# Вывод 3.11.5 при "py what.py" и при "what.py" в cli при !# python3
# Вывод 