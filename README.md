# aws-provisioning-boto3

# 📦 Top 50 Boto3 Interview Programs (10+ Yrs Experience)

This document contains a curated list of 50 advanced-level Boto3 interview programs and real-world tasks that showcase deep AWS and automation expertise.

---

## 🔐 IAM & Identity Management

1. ✅ List all IAM users and their attached policies.
2. 🔁 Create an IAM role with assume-role policy and attach custom policies.
3. 🔑 Rotate access keys for a given IAM user programmatically.
4. 📊 Detect unused IAM users or roles (based on last activity).
5. 🔄 Assume a cross-account role and access resources using STS.

---

## 🪣 S3 (Simple Storage Service)

6. 📂 List all S3 buckets with creation date and region.
7. 🚚 Upload and download large files using multipart upload.
8. 🔁 Sync local directory with an S3 bucket (like `aws s3 sync`).
9. ⚙️ Enable versioning and lifecycle rules on a bucket.
10. 🧹 Detect and delete all empty folders from a bucket.
11. 🔐 Generate pre-signed URLs for secure object access.
12. 🔒 Implement encryption at rest and in transit for S3.
13. 🧪 List and group duplicate files in S3 by hash (MD5).
14. 🛡️ Automate bucket policy assignment via script.
15. 🧊 Archive old files to Glacier using Boto3.

---

## ☁️ EC2 (Elastic Compute Cloud)

16. 🖥️ List all EC2 instances with Name, Type, State, and AZ.
17. 🛑 Start/Stop/Terminate EC2 instances in a specific tag group.
18. 🧰 Launch EC2 instance with user-data script and IAM role.
19. 📦 Attach and detach EBS volumes to/from instances.
20. 📸 Create an AMI from a running instance and copy across regions.
21. 🔁 Create and restore EBS volume snapshots.
22. 🌐 Get public IPs of all running instances.
23. 📅 Schedule instance backups using Lambda + Boto3.

---

## 🧠 CloudWatch

24. 📂 Fetch and filter CloudWatch logs using pattern (e.g., errors).
25. 🛎️ Create custom CloudWatch metrics and alarms.
26. 📤 Export logs to S3 and set retention policy.
27. 📧 Monitor Lambda error rate and send alerts via SNS.

---

## 🧰 Lambda

28. 🚀 Deploy a Lambda function from a ZIP file via Boto3.
29. 📞 Invoke a Lambda function synchronously and parse the result.
30. 📃 List all Lambda functions with runtime and timeout settings.
31. 🔄 Create event source mapping (e.g., SQS → Lambda).

---

## 📊 DynamoDB

32. 🗂️ Create a DynamoDB table and insert sample data.
33. 🔍 Query and scan tables with pagination.
34. 🗃️ Export DynamoDB data to S3.
35. 💾 Enable on-demand backups and restore tables programmatically.

---

## 📦 CloudFormation

36. 🏗️ Deploy a CloudFormation stack from a template.
37. 🧪 Get stack events and validate template syntax.
38. 🧹 Detect and delete failed stacks automatically.

---

## 📫 SNS & SQS

39. 📬 Create an SNS topic and subscribe an email endpoint.
40. 💬 Send SMS/email via SNS using Boto3.
41. 📥 Create and poll messages from an SQS queue.
42. 🚫 Implement dead-letter queue handling for failed messages.

---

## 🔐 Secrets Manager & SSM Parameter Store

43. 🔐 Create, retrieve, and rotate secrets in AWS Secrets Manager.
44. 🔍 Fetch secure strings from SSM Parameter Store for apps.

---

## 🌍 Multi-Region & Cross-Account

45. 🌎 Copy AMI from one region to another.
46. 🧳 Assume cross-account role and list S3 buckets.
47. 🧠 List EC2 instance types (SKUs) available in a given region.

---

## 🧠 Advanced Use Cases

48. 🧵 Use Boto3 with `asyncio` or threading for parallel ops.
49. 🔁 Implement retry logic and exponential backoff.
50. 💰 Monitor Boto3 API usage costs using Cost Explorer.

---
---

## 📡 VPC & Networking

51. 🌐 List all VPCs with CIDR blocks and tags.
52. 🧱 Create a custom VPC with public/private subnets, route tables, and NAT gateway.
53. 🕳️ List all security groups and associated rules.
54. 🚧 Add or revoke an inbound rule to a security group programmatically.
55. 📍 Find all EC2 instances without a public IP.

---

## 🚀 EKS (Elastic Kubernetes Service)

56. 🧭 List all EKS clusters in a region.
57. 🏗️ Create an EKS cluster with managed node group via Boto3.
58. 🔧 Update cluster version and configuration settings.
59. 🎯 Retrieve the kubeconfig for a given cluster programmatically.
60. 🧼 Delete an EKS cluster and clean up all associated resources.

---

## 🛢️ RDS (Relational Database Service)

61. 🧾 List all RDS instances and their status, engine, and size.
62. 🚀 Create an RDS instance with specific parameters (engine, size, multi-AZ).
63. 🛑 Stop and start RDS instances (where supported).
64. 📸 Take manual snapshot of an RDS instance and tag it.
65. 🔁 Restore a new RDS instance from snapshot.

---

> 💡 These tasks demonstrate experience in automating infrastructure provisioning, scaling, networking, and high availability — a must for senior DevOps/cloud roles.

---
## 🛠️ Bonus Tips

- Use `boto3.session.Session()` for multi-account/multi-region support.
- Use `botocore.config.Config()` to fine-tune retries and timeouts.
- Combine Boto3 with automation tools like Lambda, Step Functions, or Terraform.

---

> 📌 Need sample scripts for each? Let me know — I can generate a GitHub-style project scaffold.