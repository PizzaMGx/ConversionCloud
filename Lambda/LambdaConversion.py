from __future__ import print_function
import time
import urllib
import urllib.parse
import boto3
import json
import os
from PIL import Image
import mimetypes
import urllib3
import io

print("*"*80)
print("Initializing..")
print("*"*80)


s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')


def lambda_handler(event, context):
    # TODO implement
    # Buckets and keys
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'])
    inputBucket = "testbucketinput27001"
    outputBucket = "testbucketoutput27002"
    # Log
    print("Source bucket : ", source_bucket)
    print("Target bucket : ", outputBucket)
    print("Log Stream name: ", context.log_stream_name)
    print("Log Group name: ", context.log_group_name)
    print("Request ID: ", context.aws_request_id)
    print("Mem. limits(MB): ", context.memory_limit_in_mb)
    try:
        # Upload
        print("Using waiter to waiting for object to persist through s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=object_key)
        print(object_key)
        # <---Image Metadata--->
        image_Mdata = {'bucket': source_bucket, 'Key': object_key}
        url = f"https://{source_bucket}.s3.amazonaws.com/{object_key}"
        print(url)

        # <---Get the image--->
        var = urllib3.PoolManager()
        r = var.request('GET', url)

        # <---Transform To Data--->
        ContentType = mimetypes.guess_type(object_key, strict=False)[0]
        print(ContentType)
        image_data = io.BytesIO(r.data)
        buf = io.BytesIO()

        # <---Use Pillow--->
        image = Image.open(image_data)

        # <---Format--->
        format = "JPEG"
        image = image.convert('RGB')
        image = image.save(buf, format=format)
        print("hellooo")
        body = buf.getvalue()
        print(body)

        newKey = object_key[:-4]
        # <---Copy the object--->
        s3.put_object(Bucket=outputBucket, Key=f'{newKey}.jpg', Body=body)

        # <---Delete the object--->
        print('Deleting object :'+str(object_key))
        s3.delete_object(Bucket=source_bucket, Key=object_key)

    except Exception as err:
        print(f"Error: {err}")
