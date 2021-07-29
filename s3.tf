provider "aws" {  
  region = "us-east-1"
}

resource "aws_s3_bucket" "s3" {
  bucket = "com-rhinogram-test-fday"
  #bucket = file("bucket.txt") 
  acl = "private"
  force_destroy = true

  versioning {
    enabled = true
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "AES256"
      }
    }
 }

 
}


output "s3_arn" {
  value       = aws_s3_bucket.s3.arn
  description = "ARN of the new S3 bucket"
}
