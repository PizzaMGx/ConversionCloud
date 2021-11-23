Task: the client need to automate conversion of files to JPG or PNG through AWS and a script
Steps:
1- Create the resources needed for the task in a CloudFormation template
  1.1- 2 S3 buckets, one for uploading the files which are gonna be modified
       and the other for storing the ones already modified
  1.2- An SQS queue with a CloudWatch event that detects when a file is going to
       be uploaded to the first bucket 
  1.3- Create a role that gives permission to get and delete objects from an S3 bucket
  1.4- Create a Lambda Function using Python and a conversion module to convert the file and assign
       to it the S3permissions role

2- Link the resources to create the system architecture
  2.1- When the SQS catches the file, send it to the lambda function, process the file 
       and if there was no errors send it to the second bucket
  2.2- Erase the file from the firs bucket

Steps to create the lambda:
  1- Import the necessary modules (
      - boto3 with 2 variables, one for SQS and the others to the s3 buckets
     
      )
  2-Build the function 