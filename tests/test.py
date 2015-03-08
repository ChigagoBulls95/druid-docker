import subprocess
import os
import time
from retrying import retry

def printDockerComposeLogs():
  os.system('timelimit -t 1 docker-compose logs')

# Gets local host or docker host ip on osx.
def getHost():
  ip = os.popen('boot2docker ip').read().strip()
  if('.' not in ip):
    ip = 'localhost'

  print(ip)
  return ip

@retry(stop_max_delay=60000, wait_fixed=5000)
def indexData():
  command = "curl -X 'POST' -H 'Content-Type:application/json' --max-time 10 -d @wikipedia_index_task.json " + getHost() + ":8085/druid/indexer/v1/task"
  print(command)
  result = os.popen("curl -X 'POST' -H 'Content-Type:application/json' --max-time 10 -d @wikipedia_index_task.json " + getHost() + ":8085/druid/indexer/v1/task").read()
  if 'task' not in result:
    raise Exception('Response to query was incorrect')

  print('Indexing data!')

@retry(stop_max_delay=120000, wait_fixed=5000)
def queryData():
  result = os.popen("curl -X 'POST' -H 'content-type: application/json' --max-time 10 '" + getHost() + ":8082/druid/v2/?pretty' -d @time_bound_query.json").read()
  if '"maxTime" : "2013-08-31T12:41:27.000Z"' not in result:
    raise Exception('Response to query was incorrect')



os.chdir('..')

print('Building Docker images \n')
os.system('./build.sh')

print('Starting up docker images \n')
os.system('docker-compose kill && docker-compose rm --force && docker-compose up -d')

time.sleep(30)

os.chdir('tests')

try:
  indexData()
  queryData()
except:
  os.chdir('..')
  printDockerComposeLogs()
  raise


