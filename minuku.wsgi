#!/usr/bin/python
import sys
sys.path.insert(0, '/home/ubuntu/minuku')
sys.path.append('/home/ubuntu/.local/lib/python3.5/site-packages')
sys.stdout = sys.stderr
from minuku import app as application
