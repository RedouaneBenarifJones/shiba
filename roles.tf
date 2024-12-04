# IAM Role
# resource "aws_iam_role" "task_execution_role" {
#   name = "task-execution-role"
#   assume_role_policy = jsonencode({
#     Version = "2012-10-17"
#     Statement = [
#       {
#         Action = "sts:AssumeRole"
#         Effect = "Allow"
#         Principal = {
#           Service = "ecs.amazonaws.com"
#         }
#       }
#     ]
#   })
# }

# AWS Managed Policy: AmazonECSTaskExecutionRolePolicy
# data "aws_iam_policy" "ecs-task-execution-role-policy" {
#   name = "AmazonECSTaskExecutionRolePolicy"
# }
data "aws_iam_role" "ecs-task-execution-role" {
  name = "ecsTaskExecutionRole"
}

# Attach AWS Managed Policy to the ECS Task Execution Role
# resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_managed_policy" {
#   role       = data.ecs-task_execution_role.name
#   policy_arn = data.aws_iam_policy.ecs-task-execution-role-policy.arn
# }

