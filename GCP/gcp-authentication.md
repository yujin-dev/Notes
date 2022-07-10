> authentication
Google Cloud API의 액세스 제어에는 인증 / 승인 / 감사가 포함된다.
**인증**은 사용자의 신원을 확인하고 **승인**은 사용자의 작업 범위를 결정하며 작업의 로그를 **감사**한다.

### Principal
principal은 리소스에 대한 액세스 권한을 부여받을 수 있는 항목이다(ID).  
2가지 유형의 principal을 제공한다.
- user account : **Google 계정**으로 관리되며, Google Cloud를 사용하는 모든 사람을 나타낸다. 사용자를 대신하여 리소스에 액세스하는 경우를 위한 계정이다.
- service account : **IAM**으로 관리되며, 사람이 아닌 사용자를 나타낸다. App Engine 실행이나 Compute Engine 인스턴스 사용 등 리소스에 액세스하거나 자체적으로 작업을 수행하는 경우를 위한 계정이다. 

### Application
등록된 application의 요청만 수락한다. 

### 인증 전략
Google Cloud APIs에서 OAuth 2.0 프로토콜을 사용하여 user account, service account를 모두 인증한다. 
