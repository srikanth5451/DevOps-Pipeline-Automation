# AWS EKS Cluster
resource "aws_eks_cluster" "main" {
  name     = "devops-cluster"
  role_arn = aws_iam_role.eks.arn
  vpc_config {
    subnet_ids = [aws_subnet.main.id]
  }
}

# chore: Upgraded K8s

# fix: Resolved auth issue

# chore: Optimized CI/CD

# feat: Added ECS config

# feat: Added ECS config

# feat: Added GKE setup

# feat: Added GKE setup

# feat: Added ECS config

# chore: Refactored K8s

# feat: Added GKE setup

# fix: Resolved scaling issue

# fix: Resolved scaling issue

# fix: Resolved scaling issue
