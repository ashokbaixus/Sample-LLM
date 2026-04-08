provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "llm_bucket" {
  bucket = "my-llm-data-bucket"
}

resource "aws_iam_role" "bedrock_role" {
  name = "bedrock-access-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}