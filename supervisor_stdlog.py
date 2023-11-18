#!/usr/bin/env python
from __future__ import print_function
from sys import stdin, stdout, stderr
from itertools import cycle
from supervisor.childutils import listener, eventdata

# https://github.com/docker/compose/blob/main/cmd/formatter/colors.go
# RAINBOWS = [ 36, 33, 32, 35, 34, 96, 93, 92, 95, 94 ]
RAINBOWS = [ 36, 33, 32, 35, 34 ] * 2
LOGCOLOR = {'stderr': 31, 'stdlog': 34, 'stdout': 37}
CHANNELS = {'stderr': stderr,  'stdout': stdout}
COLORSIT = cycle(RAINBOWS)
COLORMAP = dict()
PADWIDTH = 1

def chomp(data):
  return data[:-1] if data.endswith('\n') else data

def log_handler(event, response):
  try:
    global PADWIDTH
    headers, data = eventdata(response.decode('utf-8'))
    PADWIDTH = max(len(headers['processname'])+1, PADWIDTH)

    prefixed = '\033[{}m{}\033[{}m%s\033[m\n'.format(
      COLORMAP.setdefault(headers['processname'], next(COLORSIT)),
      '{:<{}}| '.format (headers['processname'], PADWIDTH),
      LOGCOLOR.get(headers['channel'], LOGCOLOR['stdlog']))

    channel=CHANNELS.get(headers['channel'], stdout)
    channel.writelines((prefixed % line) for line in chomp(data).split('\n'))
  except:
    import traceback
    traceback.print_exc()

def main():
  while True:
    headers, payload = listener.wait(stdin, stdout)
    listener.send(payload, stdout)

if __name__ == '__main__':
  main()
