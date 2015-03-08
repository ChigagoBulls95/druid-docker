import subprocess
import os
import time
from retrying import retry

def printDockerComposeLogs():
  os.system('docker-compose logs &')


@retry(stop_max_delay=60000, wait_fixed=5000)
def indexData():
  result = os.popen("curl -X 'POST' -H 'Content-Type:application/json' -d @wikipedia_index_task.json 192.168.59.103:8085/druid/indexer/v1/task").read()
  if 'task' not in result:
    raise Exception('Response to query was incorrect')

  print('Indexing data!')

@retry(stop_max_delay=120000, wait_fixed=5000)
def queryData():
  result = os.popen("curl -X 'POST' -H 'content-type: application/json' '192.168.59.103:8082/druid/v2/?pretty' -d @time_bound_query.json").read()
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


