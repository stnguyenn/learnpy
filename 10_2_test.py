
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average([20, 30, 70])

# unittest.main()  # Calling from the command line invokes all tests

import reprlib
it = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(it)

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]

pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# conv = locale.localeconv()          # get a mapping of conventions
# x = 1234567.8
# it = locale.format("%d", x, grouping=True)
# print(it)

# it = locale.format_string("%s%.*f", (conv['currency_symbol'],
#                      conv['frac_digits'], x), grouping=True)
# print(it)


from string import Template
t = Template('${village}folk send $$10 to $cause.')
it = t.substitute(village='Nottingham', cause='the ditch fund')
print(it)

# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# it = t.substitute(d)
# print(it)
  

# it = t.safe_substitute(d)
# print(it)

# import time, os.path
# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# class BatchRename(Template):
#     delimiter = '%'
# fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')


# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))


# import struct

# with open('myfile.zip', 'rb') as f:
#     data = f.read()

# start = 0
# for i in range(3):                      # show the first 3 file headers
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

#     start += extra_size + comp_size     # skip to the next header

# import threading, zipfile

# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile

#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)

# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')

# background.join()    # Wait for the background task to finish
# print('Main program waited until background was done.')

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# import weakref, gc
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)

# a = A(10)                   # create a reference
# d = weakref.WeakValueDictionary()
# d['primary'] = a            # does not create a reference
# d['primary']                # fetch the object if it is still alive

# del a                       # remove the one reference
# gc.collect()                # run garbage collection right away

# d['primary']                # entry was automatically removed

from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)

it = a[1:3]
print(it)

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
it = scores
print(it)


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries

from decimal import *
it = round(Decimal('0.70') * Decimal('1.05'), 2)
print(it)

it = round(.70 * 1.05, 2)
print(it)

it = Decimal('1.00') % Decimal('.10')
print(it)

1.00 % 0.10


it = sum([Decimal('0.1')]*10) == Decimal('1.0')
print(it)

it = sum([0.1]*10) == 1.0
print(it)


getcontext().prec = 36
it = Decimal(1) / Decimal(7)
print(it)

