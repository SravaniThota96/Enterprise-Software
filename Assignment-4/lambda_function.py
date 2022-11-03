import json
import urllib.parse
import boto3
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO


source_bucket = "aura-bucket-9"
destination_bucket = "cosmo-bucket-9"
aws_access_key_id=''
aws_secret_access_key=''

def read_image(key):
    s3=boto3.resource('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
    response = s3.meta.client.get_object(Bucket=source_bucket,Key=key)
    return response['Body'].read()
    
def upload_image(key,image_data):
    s3=boto3.resource('s3',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
    response = s3.meta.client.put_object(Body=image_data,Bucket=destination_bucket,Key=key)
    return response

def validate_extension(key):
    allowed_extensions=[".png",".img",".jpg",".jpeg"]
    for i in allowed_extensions:
        if (i in key):
            return True
        else:
            return False

def random_quote():
    with open("quotes.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines)


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print( "File named " + key +" was uploaded to bucket named "+ bucket)
    print("Validated Extension: "+str(validate_extension(key)))
    #if (validate_extension(key)):
    # Read this image into variable here - this is from source bucket
    image_data = read_image(key)
    #Get random quote
    quote = random_quote()
    print("The quote to print: "+quote)
    stream = BytesIO(image_data)
   
    image = Image.open(stream)
    
    I1 = ImageDraw.Draw(image)
    
    myFont = ImageFont.truetype('OpenSans-Medium.ttf', 65)
    I1.text((20, 10),str(quote),font=myFont, fill=(255, 0, 0))
    
    byte_io = BytesIO()
    
    image.save(byte_io,"jpeg")
    
    quoted_image_data = byte_io.getvalue()
    #Uplod this image to the destination bucket
    print("The Key name for cosmo is : "+str(key))
    upload_result= upload_image(key,quoted_image_data)
    print(upload_result)
    print("quoted image uploaded successfully to cosmo-bucket-9")

        
    
