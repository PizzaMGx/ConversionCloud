1- Create the resources needed for the task in a CloudFormation template
  1.1- 2 S3 buckets, one for uploading the files which are gonna be modified
       and the other for storing the ones already modified
  1.3- Create a role that gives permission to get and delete objects from an S3 bucket
  1.4- Create a Lambda Function using Python and a conversion module to convert the file and assign
       to it the S3permissions role

2- Link the resources to create the system architecture
  2.1- When the S3 catches the create file, the lambda gets the element trough the lambda trigger event, process the file 
       and if there was no errors send it to the second bucket
  2.2- Erase the file from the firs bucket
