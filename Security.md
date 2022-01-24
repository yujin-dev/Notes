# AWS IAM 
>>Udemy
IAM(Identity Access Management)은 Identity and Access Management, global service를 의미한다.

### IAM Users & Groups 

#### IAM Permissions
- least privilege principle : user가 필요한 permissions 이상을 주지 않는다.

### IAM Policies

### Policy Structure
![](./2022-01-13-13-54-21.png)

- Version
- ID
- Statement
    - Sid
    - Effect : allow OR deny
    - Principal : account/user/role 
    - Action : list of actions
    - Resource : list  of resources
    - Condition

### IAM MFA
#### Password Policy

IAM user를 보호하기 위한 수단은 2가지가 있다.
1. password
2. MFA( Multi Factor Auethentication ) : password + security device 
    - Root 계정과 IAM user를 보호
    - Google Authenticator, Authy 등 virtual MFA가 있고, third party가 있다.

### AWS Access Keys, CLI and SDK
AWS에 접근하는데 다음과 같이 3가지 방법이 있다.
- AWS Managemnt Console
- AWS CLI
- AWS SDK

Access Key, Secret Access Key로 접근해야 한다. AWS Managemnt Console를 통해 Access Key를 생성한다.

### IAM Roles for AWS Services
aws service에 접근하려 할때 IAM roles이 있는 경우에 가능하다.


### IAM Security
- IAM Credentials Report( account-level ) : account의 users나 여러 credentials에 대한 리포트
- IAM Access Advisor( user-level ) : user에 부여된 service permission


## Summary
- AWS account setup외에는 root account를 사용하지 않는다.
- 하나의 physical user = 하나의 AWS user
- users를 groups에 할당시키고 groups에 permissions을 부여한다.
- 강한 password policy를 생성한다.
- CLI / SDK에 Access Keys를 사용한다.
- IAM Credentials Report로 permissions을 관리한다.
- IAM users & Access Keys를 공유하지 않는다.
