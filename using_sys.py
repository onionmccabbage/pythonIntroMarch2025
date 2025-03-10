# Python has access to many aspects of the system it is running on
import sys
# we can assign our OWN locations for our libraries
sys.path.append('d:/pythonIntroMarch2025/demo_stuff')

print( sys.path )

print(sys.version, sys.version_info)

print( sys.maxsize ) # 2**64-1 (on a 64 bit machine)

# however, Python will always look for a way to exceed limiations....
biggy = 2**9024

print(biggy)