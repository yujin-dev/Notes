
# AWS Solutions Architect Associate Certificate
자격증 준비를 위한 Udemy 강의를 정리
## IAM
IAM(Identity Access Management)은 Identity and Access Management, global service를 의미한다.

IAM user를 보호하기 위한 수단은 2가지가 있다.
1. password
2. MFA( Multi Factor Auethentication ) : password + security device 
    - Root 계정과 IAM user를 보호
    - Google Authenticator, Authy 등 virtual MFA가 있고, third party가 있다.
### IAM Roles
aws service에 접근하려 할때 IAM roles이 있는 경우에 가능하다.

## [EC2](https://github.com/yujin-dev/AWS-Tutorial/blob/master/EC2.md)
EC2는 Elastic Compute Cloud로 인프라를 서비스로 제공하는 것이다.
다음과 같이 사용할 수 있다.
- EC2 인스턴스로 virtual machines를 빌릴 수 있음 
- EBS volumes로 virtual drives에 데이터를 저장
- ELB( Elastic Load Balancer )로 machines 간 Load를 분산
- auto-scaling group인 ASG로 서비스를 scaling

## [Amazon S3](https://github.com/yujin-dev/AWS-Tutorial/blob/master/Amazon_S3.md)
AWS의 building blocks 개념이다.


## [Serverless](https://github.com/yujin-dev/AWS-Tutorial/blob/master/Serverless.md)
서비리스는 서버를 관리할 필요없이 서비스를 Function으로 배포한다.
AWS에서는 AWS Lambda, DynamoDB, AWS API Gateway, Amazon S3 등이 있다.
