# AWS

##Creating lambda from cli
```
aws iam create-role `
  --role-name lambda-basic-execution-role `
  --assume-role-policy-document file://trust-policy.json
```
###execution policy 
```
aws iam create-role `
  --role-name lambda-basic-execution-role `
  --assume-role-policy-document file://trust-policy.json
```
### deploy the lambda function
```
aws lambda create-function `
  --function-name mockMongoLambda `
  --runtime python3.9 `
  --role arn:aws:iam::740918041352:role/lambda-basic-execution-role `
  --handler lambda_function.lambda_handler `
  --zip-file fileb://lambda_function.zip `
  --region ap-south-1

```
###invoking the lambda 
```
aws lambda invoke `
  --function-name mockMongoLambda `
  --payload '{}' `
  --region ap-south-1 `
  response.json

```
