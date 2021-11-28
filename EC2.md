# EC2

EC2 User data script를 통해 인스턴스를 bootstrap할 수 있다. Bootstrapping은 machines이 시작할 때의 launching 명령어이다.

### SSH
SSH로 EC2 인스턴스에 접속하기 위해서는 보안 그룹에서 프로토콜 TCP로 port 22가 열려있어야 한다. 
보안을 위해 key파일을 다운받아 인증한다.

