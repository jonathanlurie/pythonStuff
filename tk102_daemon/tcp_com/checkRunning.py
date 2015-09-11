# this is supposed to be launched with python.
# Check if a program is currently running, if not, it launches it
# as an independaant process using "nohup" and ending "&"
#
# Particularly usefull on a cron task to check if a daemon is still running

from subprocess import Popen, PIPE
from re import split
from sys import stdout
import datetime

#programToFind = "/home/lurie/tmp/pythonstuff/loop.py"
programToFind = "/srv/madfish/projets/tk102_daemon/tcp_com/receive.py"
LaunchedWith = "python"


#procList = Popen(['ps', 'aux' ], shell=False, stdout=PIPE)
procList = Popen('ps aux | grep ' + programToFind , shell=True, stdout=PIPE)

isLaunched = False

for line in procList.stdout:
  launcherFound = False
  programFound = False

  arraySplit = line.strip().split(" ")

  #print arraySplit

  for i in arraySplit:
    if(i == LaunchedWith):
      launcherFound = True

    if(i == programToFind):
      programFound = True

  if( launcherFound and programFound):
    isLaunched = True


if(not isLaunched):
  # print essentially made for log
  print str(datetime.datetime.now()) + " program not running, we launch it in nohup mode..."
  Popen(['nohup', LaunchedWith,  programToFind, "&"], shell=False, stdout=PIPE)
#else:
#  print "program is currently launching..."

