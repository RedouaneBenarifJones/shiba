resource "aws_default_vpc" "default_vpc" {}
resource "aws_default_subnet" "default_subnet_a" {
  availability_zone = "${var.AWS_REGION}a"
}
resource "aws_default_subnet" "default_subnet_b" {
  availability_zone = "${var.AWS_REGION}b"
}
resource "aws_default_subnet" "default_subnet_c" {
  availability_zone = "${var.AWS_REGION}c"
}
