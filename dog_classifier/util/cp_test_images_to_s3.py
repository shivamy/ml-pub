import boto3

BUCKET = '[YOUR_BUCKET]'
NUM_FILES = 200
s3 = boto3.resource('s3')

with open('./dog_test.lst', 'r') as f:
    for ix, line in enumerate(f):
        if (ix >= NUM_FILES):
            break
        local_file = line.split()[2]
        local_file = 'Images'+'/'+local_file
        print(local_file)
        s3.Bucket('[YOUR_BUCKET]').upload_file(local_file, 'stanford_dogs_2/test/'+local_file)

