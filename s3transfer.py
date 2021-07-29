import json
import random
import string
import datetime
import boto3

def makeRandomStr(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

with open('data.json') as f:
  data = json.load(f)

s3 = boto3.resource('s3')

s3Bucket = 'nihniehs-dai3-terraform'

for item in data:
   ranStr = makeRandomStr()

   fileName = ranStr + '.json'
   with open(fileName,'w') as fPtr:
      aDict = {}
      aDict['name'] = item['name']
      json.dump(aDict,fPtr)
      fPtr.flush()

      org = item['org']
      today = datetime.date.today()
      year = today.strftime('%Y')
      month = today.strftime('%m')
      day = today.strftime('%d')
      bucketKey = f'{org}/{year}/{month}/{day}/{fileName}'
      print(f'bucketKey: {bucketKey}')
      s3.meta.client.upload_file(fileName, s3Bucket, bucketKey)
