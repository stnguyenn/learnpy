

import os
# os.getcwd()      # Return the current working directory

# os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir today')   # Run the command mkdir in the system shell

# dir(os)

# help(os)

# import shutil
# shutil.copyfile('data.db', 'archive.db')

# shutil.move('./build/executables', 'installdir')

# import glob
# glob.glob('*.py')

import sys
print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')

import math
math.cos(math.pi / 4)

math.log(1024, 2)

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(data)
print(statistics.mean(data))

print(statistics.median(data))

print(statistics.variance(data))


from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)



# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org

# Beware the Ides of March.
# """)
# server.quit()

# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
print(len(t))

zlib.decompress(t)
print(len(t))


zlib.crc32(s)

print(len(t))

from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

Timer('a,b = b,a', 'a=1; b=2').timeit()

