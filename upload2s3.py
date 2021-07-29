import json
import random
import string
import datetime
import boto3

# randomly generate a string of numbers and uppercase letters. The length is configurable and 6 by default.
def makeRandomStr(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# define S3 bucket name
s3Bucket = 'com-rhinogram-test-fday'

s3 = boto3.resource('s3')

if __name__ == "__main__":   # program starts here
# open input file and start processing
 with open('data.json') as f:
    data = json.load(f)

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
      #print(f'bucketKey: {bucketKey}')
      s3.meta.client.upload_file(fileName, s3Bucket, bucketKey)
      print(f'{fileName} transferred')

 print('End of program')
