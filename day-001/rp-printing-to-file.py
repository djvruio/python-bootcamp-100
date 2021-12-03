'''
 standard streams provided by OS: 
 1. stdin: standard input (read only) , File Descriptor = 0
 2. stdout: standard output (write only), File Descriptor = 1, Ex. > same as 1>
 3. stderr: standard error (write only), File Descriptor = 2

All standard streams through sys module
By default, print() is bound to sys.stdout through its file argument

'''

import sys

print("1. stdin")
print(sys.stdin)
print(sys.stdin.fileno())

print("2. stdout")
print(sys.stdout)
print(sys.stdout.fileno())

print("3. stderr")
print(sys.stderr)
print(sys.stderr.fileno())

# new block print to a file
print("=" * 25)
import io
fake_file = io.StringIO()
print("Before", fake_file.getvalue())
print("Save in fake file, not showed up to screen", file=fake_file)
print("After",fake_file.getvalue())