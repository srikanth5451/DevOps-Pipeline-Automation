module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.0"

  cluster_name    = "devops-cluster-${var.env}"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    default = {
      min_size     = 1
      max_size     = 3
      desired_size = 2
      instance_types = ["t3.medium"]
    }
  }
}
# 2024-02-01 - chore: Refactor manifests
# 2024-02-05 - fix: Patch security vulnerability
# 2024-02-07 - feat: Add EKS autoscaling
# 2024-02-07 - docs: Add architecture diagram
# 2024-02-07 - chore: Upgrade Terraform
# 2024-02-09 - chore: Refactor manifests
# 2024-02-12 - chore: Refactor manifests
# 2024-02-13 - chore: Upgrade Terraform
# 2024-02-14 - fix: Resolve networking issue
# 2024-02-15 - feat: Implement Azure pipeline
# 2024-02-19 - docs: Improve runbook
# 2024-02-19 - feat: Add EKS autoscaling
# 2024-02-21 - feat: Add EKS autoscaling
# 2024-02-27 - fix: Fix deployment bug
# 2024-02-28 - chore: Refactor manifests
# 2024-02-29 - feat: Add EKS autoscaling
# 2024-03-05 - docs: Improve runbook
# 2024-03-11 - docs: Improve runbook
# 2024-03-12 - fix: Resolve networking issue
# 2024-03-12 - fix: Patch security vulnerability
