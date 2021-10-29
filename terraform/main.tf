provider "aws" {
  region = "us-east-1"
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "wm_api_lambda"
  description   = "My awesome lambda function"
  handler       = "wm_api-lambda.lambda_handler"
  runtime       = "python3.8"

  source_path = "../app/"

  tags = {
    Name = "WM-Challenge_Lambda"
  }
}
