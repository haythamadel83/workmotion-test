provider "aws" {
  region = "us-east-1"
}

module "lambda_function" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "wm_api-lambda"
  description   = "My awesome lambda function"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"

  source_path = "../app/app.py"

  tags = {
    Name = "WM-Challenge_Lambda"
  }
}
