#!/bin/bash

# Load .env.terraform
set -o allexport
source .env.terraform
set +o allexport

# Run Terraform commands
terraform init
terraform apply "$@"
