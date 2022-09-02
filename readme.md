# Backend Test

This project uses the [Serverless Framework](https://serverless.com), Python 3.8, AWS Lambda, AWS API Gateway, AWS DynamoDB, AWS S3.

## The test

1. Your task is to build and deploy on AWS an API with a CRUD of **Blog posts** using the Serverless Framework, Lambda functions and DynamoDB.
   
2. The Blog posts can have medias attached to them, in that case, Create and Delete medias must also have endpoints. You should store the medias uploaded on a S3 Bucket and save its url on the post 'medias' array field.

3. Obs:
   - At task completion, make a pull request to this repository with the API url at the end of the README.md
   - The [Create function](/src/api/create_post.py) and [Insert Media](src/api/insert_media.py) are already implemented as an example, but you'll have to modify it to fit the requirements
   - If you have any trouble to complete this task you can add comments to the Problems section of this README explaining your situation
   - Each blog post must have the following schema, and you have to **make sure** the API doesn't allow different objects and that it returns the proper HTTP codes

```python
# Blog Post Object description

# _id: identifier uuid string
# author: string 
# title: string
# body: string
# medias: List[string]

{
    '_id': uuid,
    'author': str,
    'title': str,
    'body': str,
    'medias': list
}
```

## Deployment

To deploy to the AWS Cloud, simply run:

```sh
make build
make deploy
```

When you are done with the challenge, please remove the resources and clean the stack by running:

```sh
make remove
make clean
```

## Tools

We encourage you to read the documentation of the tools used in this task:

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Serverless](https://www.serverless.com/framework/docs/)

## Environment

### AWS
You are required to create an [AWS account](https://aws.amazon.com) if you don't have one yet.

### Setting up AWS

1. Install ```aws-cli```: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
2. Configure credentials on your local machine, by running:

```bash
$ aws configure
AWS Access Key ID [None]: <Your-Access-Key-ID>
AWS Secret Access Key [None]: <Your-Secret-Access-Key-ID>
Default region name [None]: us-west-1
Default output format [None]: json
```
View [CLI Config](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) for reference.

3. Create AWS credentials including the following IAM policies: ```AWSLambdaFullAccess```, ```AmazonS3FullAccess```, ```AmazonAPIGatewayAdministrator``` and ```AWSCloudFormationFullAccess```.

Run:
```sh
aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AWSLambdaFullAccess --user-name <username>

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --user-name <username>

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AmazonAPIGatewayAdministrator --user-name <username>

aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/AWSCloudFormationFullAccess --user-name <username>
```

## Requirements

- aws-cli
- serverless
- python3.8

## Problems

## API url goes here

https://i47qivqvnf.execute-api.us-west-1.amazonaws.com/prod
https://i47qivqvnf.execute-api.us-west-1.amazonaws.com/prod/post