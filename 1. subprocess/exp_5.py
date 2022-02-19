"""Запуск скрипта-дочернего процесса"""

from subprocess import Popen, PIPE

PROC = Popen(
    "python3 test_ex.py",
    shell=True,
    stdout=PIPE, stderr=PIPE
)

# получить tuple('stdout', 'stderr')
RES = PROC.communicate()
print(PROC.returncode)
print()
if PROC.returncode == 0:
    print(RES)
else:
    print('error')
print()
print('result:', RES[0])
