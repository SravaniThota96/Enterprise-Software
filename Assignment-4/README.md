# Serverless_Application-ImageEdit

Deployed a simple serverless web application using lambda function which
edits any new image uploaded to source S3 bucket by random quotes and saves it in
destination bucket. Random quotes are saved in the lambda function folder as .txt
file. The function code is written in python. The code execution logs can be seen on
CloudWatch.

## Use case

Similar function can be used to watermark any image uploaded to S3 bucket.

### Input Image:

![image](https://user-images.githubusercontent.com/85700971/197364149-49fc6e41-161b-419a-9a76-ca3ead7d9498.png)


### Output Image:


![image](https://user-images.githubusercontent.com/85700971/197364168-ac4562a1-713a-40bb-8cbc-2952c745e06b.png)

### CloudWatch Log:

![image](https://user-images.githubusercontent.com/85700971/197364243-c582c404-4dc0-4dd9-bbe4-1ec360b81a49.png)
