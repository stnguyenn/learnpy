
import fibo

fibo.fib(1000)

print(fibo.__name__)


fib = fibo.fib
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib, fib2
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import *
fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo as fib
fib.fib(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib as fibonacci
fibonacci(500)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import fibo, sys
dir(fibo)
# ['__name__', 'fib', 'fib2']
dir(sys)  
# ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
#  '__package__', '__stderr__', '__stdin__', '__stdout__',
#  '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
#  '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
#  'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
#  'call_tracing', 'callstats', 'copyright', 'displayhook',
#  'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
#  'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
#  'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
#  'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
#  'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
#  'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
#  'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
#  'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
#  'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
#  'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
#  'thread_info', 'version', 'version_info', 'warnoptions']

