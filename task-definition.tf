# ECS Task Definition
resource "aws_ecs_task_definition" "task_definition" {
  family                   = "service"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 1024
  memory                   = 3072
  execution_role_arn       = data.aws_iam_role.ecs-task-execution-role.arn
  container_definitions = jsonencode([
    {
      name      = "nginx"
      image     = "79adamjones/custom-nginx:latest"
      cpu       = 256
      memory    = 256
      essential = true
      # dependsOn = [
      #   {
      #     containerName = "users"
      #     condition     = "START"
      #   }
      # ]
      portMappings = [
        {
          containerPort = 81
          hostPort      = 81
        }
      ]
      logConfiguration = {
        logDriver = "awslogs",
        options = {
          "awslogs-group"         = "/ecs/shiba-service",
          "awslogs-region"        = "eu-west-3",
          "awslogs-stream-prefix" = "nginx"
        }
      }
    },
    {
      name      = "users"
      image     = "79adamjones/shiba-users-service-image:latest"
      cpu       = 512
      memory    = 512
      essential = true
      # dependsOn = [
      #   {
      #     containerName = "mongodb"
      #     condition     = "HEALTHY" # or "START"
      #   }
      # ]
      # healthCheck = {
      #   command = [
      #     "CMD-SHELL",
      #     "curl -f http://users:80 || exit 1"
      #   ],
      #   interval    = 30
      #   timeout     = 5
      #   retries     = 3
      #   startPeriod = 60
      # }
      environment = [
        {
          name  = "PYTHONPATH"
          value = var.PYTHONPATH
        },
        {
          name  = "MONGODB_HOST"
          value = var.MONGODB_HOST
        },
        {
          name  = "MONGODB_PORT"
          value = var.MONGODB_PORT
        },
        {
          name  = "MONGODB_DATABASE"
          value = var.MONGODB_DATABASE
        },
        {
          name  = "MONGO_INITDB_ROOT_USERNAME"
          value = var.MONGO_INITDB_ROOT_USERNAME
        },
        {
          name  = "MONGO_INITDB_ROOT_PASSWORD"
          value = var.MONGO_INITDB_ROOT_PASSWORD
        }
      ]
      logConfiguration = {
        logDriver = "awslogs",
        options = {
          "awslogs-group"         = "/ecs/shiba-service",
          "awslogs-region"        = "eu-west-3",
          "awslogs-stream-prefix" = "nginx"
        }
      }
    },
    {
      name      = "mongodb"
      image     = "mongo:latest"
      cpu       = 256
      memory    = 256
      essential = true
      # healthCheck = {
      #   command = [
      #     "CMD",
      #     "mongosh",
      #     "--quiet",
      #     "--eval",
      #     "db.runCommand('ping').ok"
      #   ],
      #   interval    = 30,
      #   timeout     = 5,
      #   retries     = 3,
      #   startPeriod = 60
      # }
      environment = [
        {
          name  = "MONGO_INITDB_ROOT_USERNAME"
          value = var.MONGO_INITDB_ROOT_USERNAME
        },
        {
          name  = "MONGO_INITDB_ROOT_PASSWORD"
          value = var.MONGO_INITDB_ROOT_PASSWORD
        }
      ]
      logConfiguration = {
        logDriver = "awslogs",
        options = {
          "awslogs-group"         = "/ecs/shiba-service",
          "awslogs-region"        = "eu-west-3",
          "awslogs-stream-prefix" = "nginx"
        }
      }
    }
  ])
}
