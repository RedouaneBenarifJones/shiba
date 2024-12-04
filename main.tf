terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.AWS_REGION
}

# ECS Cluster
resource "aws_ecs_cluster" "cluster" {
  name = "shiba-cluster"
}

# Capacity provider [FARGATE]
resource "aws_ecs_cluster_capacity_providers" "ec2_capacity_provider" {
  cluster_name = aws_ecs_cluster.cluster.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    capacity_provider = "FARGATE"
    base              = 0
    weight            = 1
  }
}
# CloudWatch Logs
resource "aws_cloudwatch_log_group" "ecs_logs" {
  name              = "/ecs/shiba-service"
  retention_in_days = 1
}
