Securing Amazon RDS with IAM and VPC involves
  Secure Access with IAM
  Configure VPC for Network Security
  Encrypt Data
  Monitor and Audit

Secure Access with IAM
  1.Create IAM policies to control access to RDS resources.
  2.Configure IAM database authentication to allow users to connect to RDS using temporary IAM credentials.
  3. Place your RDS instance in a private subnet within a VPC to restrict public access.
  4. Create security groups to control inbound and outbound traffic to your RDS instance.
Configure VPC for Network Security
  1.Run RDS in a Private Subnet:
  2.Use Security Groups:
  3.Enable Network ACLs:

Encrypt Data
  1. AWS KMS to encrypt your RDS instance

Monitor and Audit
  1.Enable CloudTrail( tracks account activity )
  2.Monitor with CloudWatch


  STEPS:

  1. create a VPC with 2 subnets-1 private and 1 public
  2. we will deploy RDS in private subnet
  3. create a SG that allows only ec2 instance to connect
  4. we will enable IAM Authentication in RDS
