variable "AWS_REGION" {
  default = "eu-west-3"
  type    = string
}

variable "PYTHONPATH" {
  description = "Path to the Python source code"
  type        = string
}

variable "MONGODB_HOST" {
  description = "The hostname of the MongoDB server"
  type        = string
}

variable "MONGODB_PORT" {
  description = "The port of the MongoDB server"
  type        = string
}

variable "MONGODB_DATABASE" {
  description = "The MongoDB database to use"
  type        = string
}

variable "MONGO_INITDB_ROOT_USERNAME" {
  description = "MongoDB root username"
  type        = string
}

variable "MONGO_INITDB_ROOT_PASSWORD" {
  description = "MongoDB root password"
  type        = string
}
