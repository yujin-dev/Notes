# EC2
### EC2( Elastic Compute Cloud )
- virtual machines를 빌려주고(EC2)
- virtual drives에 데이터를 저장하고(EBS)
- machines에 로드를 분산시키고(ELB)
- auto-scaling으로 서비스를 스케일링(ASG)

#### sizing & configuration options
- OS
- CPU
- RAM
- Storage
    - netword-attached : EBS, EFS
    - hardware : EC2 Instance Store
- Network card : public IP address
- Firewall rules : security group
- Bootstrap script : EC2 User Data

#### EC2 User Data
- EC2 User data script를 통해 인스턴스를 bootstrap할 수 있다. 
- Bootstrapping은 machines을 시작할 때의 명령어를 의미한다. 인스턴스가 생성되고 맨 처음 부팅에서만 한번 실행된다.
- 설치나 업데이트 등 
- root user로 실행해야 한다

![](./img/2021-12-29-15-05-11.png)

### EC2 Instance Types
EC2 instance는 원하는 스펙에 맞춰 선정해 사용하면 된다.
- Compute Optimized : batch processing 등 high performance가 필요한 경우
- Memory Optimized : 실시간 대용량 데이터 처리 등 메모리 상 대용량 데이터를 처리하는데 빠른 속도가 필요한 경우
- Storage Optimized : OLTP systems,관계형 & NoSQL DB 등 read, write 작업량이 많이 필요한 경우

#### naming convention
`m5.2xlarge`의 의미는,
- m : instance class
- 5 : generation
- 2xlarge : size within the instance class

### Security Groups
EC2 Instances의 내부로, 외부를 허용하는 traffic에 대한 제어를 담당한다.
- Ports 허용
- IP ranges( IPv4, IPv6 )
- inbound network
- outbound networkd
를 제어한다.

#### Tips 
- 여러 instances에 붙일 수 있다.
- region / VPC에 따른다.
- SSH access에 하나의 security group을 유지하는 것이 좋다.
- default로, inbound traiffic은 막혀있고, outbound traffic은 허용된다.

#### Ports
- 22 = SSH : log into Linux
- 21 = FTP : upload files 
- 22 = SFTP : upload files using SSH
- 80 = HTTP : access unsecured websites
- 443 = HTTPS : access secured websites
- 3389 = RDP : log in Windows


### SSH
- SSH로 EC2 인스턴스에 접속하기 위해서는 보안 그룹에서 프로토콜 TCP로 port 22가 열려있어야 한다. 
- 보안을 위해 key파일을 다운받아 인증히먄 SSH로 접속 가능하다.

### EC2 Instance Connect 
브라우저에서 EC2 instance에 접속할 수 있다. key file은 필요없다.
마찬가지로 port 22는 열려있어야 한다.

### EC2 Instances puchasing options
- On Demand : short workload, predictable pricing
- Reserved : 최소 1년, long workload
- Spot Instances : short workload, highest discount, max price가 현재의 spot price보다 낮으면 instance가 없어질 수 있음.  
    - batch jobs, data analysis 등에 적합
    - critical jobs / DB에는 적합하지 않음

- Dedicated Hosts : physical server
- Dedicated Instances : hardware를 공유하지 않음


### Spot Instances & Spot Fleet
Spot Fleets : Sport Instances의 묶음 + On-Demand Instances
- 가격 제한에서 target capacity를 맞추고자 한다.

Spot Instances를 할당하는데는 전략이 있다.
- lower price
- diversified
- capacityOptimized

### private vs. public vs. Elastic IP
- IPv4 : 1.16.10.240
- IPv6 : 3ffe:1900:4545:3:200:f8ff:fe21:67cf

IPv4가 가장 보통의 형식으로 [0-255].[0-255].[0-255].[0-255]. 으로 이루어진다.

#### public IP
- internet(WWW)에서 식별 가능한 IP
- 전체 웹에서 고유해야 한다.

#### private IP
- private network에서만 식별 가능하다.
- private network만에서 고유하면 된다.
- NAT + internet gateway로 인터넷에 연결된다.

#### Elastic IP
EC2 instance를 멈추거나 시작하는 경우 public IP가 바뀐다. 고정된 public IP를 가지기 위해서는 Elastic IP가 필요하다.
- 하나의 instance에만 붙여서 사용할 수 있다.
- account당 5개까지만 Elastic IP를 가질 수 있다.

### EC2 Placement Groups

#### Cluster
하나의 Availability Zone의 low-latency group에서 instance를 클러스터링한다.

![](./img/2022-01-02-09-08-55.png)

- network 성능이 좋다( 10 Gbps bandwidth )
- rack failure가 발생하면 모든 인스턴스가 failure.
- 빨리 끝내야 하는 Big Data Job이나 low-latency, high network throughput가 필요한 경우에 주로 사용된다.

#### Spread
hardware에 instance를 분산시킨다.

![](./img/2022-01-02-09-09-47.png)
- 여러 Availability Zones에서 분산된다.
- 여러 physical hardware에 instance를 생성한다.
- placement group에서 AZ당 인스턴스 7개까지만 지원된다.
- high availability가 필요하거나 failure를 방지하기 위해 서로 분리가 필요한 경우

#### Partition
여러 partitions를 분산시킨다.

![](./img/2022-01-02-09-14-48.png)

- AZ당 partitions 7개까지만 지원된다.
- 같은 region에서 여러 AZ에 분산시킬 수 있다.
- 100 EC2 instances까지 지원된다.
- partition failure는 여러 EC2에 영향을 미치지만 다른 partitions엔 영향을 주지 않음
- metadata같은 정보를 갖고 있다.
- HDFS, HBase, Cassandra, Kafka를 사용하는 경우에 주로 사용한다.

### Elastic Network Interfaces(ENI)

![](./img/2022-01-02-09-18-15.png)
- parim 

### EC2 Hibernate

## EC2 Instance Storage

### EBS

### EBS Snanpshot

### AMI

### EC2 Instance Store

### EBS Volume Types

### EBS Multi-Attach

### EBS Encryption

### EFS

### EFS vs. EBS 

## High Availability and Scalability : ELB & ASG

### High Availability and Scalability

### ELB( Elastic Load Balancing )

#### Cross Zone Load Balancing
#### SSL Certificates
#### Connection Draining


### CLB( Classic Load Balancer )

### ALB( Application Load Balancer )

### NLB( Network Load Balancer )

### GWLB( Gateway Load Balancer )

### ASG ( Auto Scaling Groups )

#### Scaling Policies 