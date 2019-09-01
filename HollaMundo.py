import subprocess

print("Hola magnifico mundo")
subprocess.call('espeak -ves ' + '"Hola, soy Fabián"', shell=True)
