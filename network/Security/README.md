> 빠르게 살펴보는 IT 보안

## IPS, IDS, Firewall
- IPS : 네트워크 트래픽을 스캐닝하여 악성 공격을 감지하고 방어한다.( ex. Dos, DDos )
- IDS : 수동적으로 시스템으로 트래픽을 모니터링 및 스캔하고 보고한다.
- Firewall : 미리 할당된 보안규칙을 기반으로 방어 대상 시스템으로 in-bound, out-bound 트래픽을 분석한다.

## 방화벽 vs. IPS
- 방화벽 : IP주소, 포트 번호 기반으로 트래픽을 필터링한다.
- IPS : 실시간 트래픽을 검사하고 트래픽 패턴이나 공격 시그니처를 공격을 탐지 및 방지한다.( ex. 표준길이가 아닌 IP 패킷, 버퍼 오버플로우, Dos, DDos 공격 )

## 네트워크의 비무장지대, DMZ 네트워크
DMZ 네트워크는 내부 네트워크(LAN)에 존재하지만 외부에서 접근이 가능한 구간이다.

## NAT(Network Address Translation)
라우터 등의 장비를 이용하여 사설 IP를 공인 IP로 변환하는 주소 변환 서비스이다.
NAT Forwarding Table에 IP주소 + 포트번호 정보를 보관하여 사용한다. 공인IP는 같으나 포트 번호를 다르게 할당하여 각각의 호스트를 구분한다.
### IP 마스쿼레이딩
하나의 공인 IP 뒤로 여러 개의 사설 IP를 은닉하는 마스쿼레이딩을 사용한다.

## HTTPS를 위한 SSL/TLS
웹 브라우저, 웹 서버에서 적용되는 보안 HTTP로, 웹 서버에 SSL/TLS 인증서를 설치하여 사용한다.

- 대칭키 암호화 : 하나의 키로 암호화 및 복호화한다.
- 공개키 암호화 : 공개키 - 개인키의 한쌍으로 각각 암호화 및 복호화한다. 일반적으로 공개키로 암호화하여 개인키로 복호화한다. 개인키를 먼저 생성하고 공객키를 파생시키는 형식이다.

### SSL handshaking
1. 웹 브라우저 -> 웹 서버 : client hello
2. 웹 서버 -> 웹 브라우저 : server hello
3. 웹 브라우저 : 받은 서버 인증서를 확인한다. 대부분의 브라우저에는 공신력 있는 CA 정보와 CA가 만든 공개키가 이미 설치되어 있어, 공개키를 통해 인증서를 복호화하여 확인한다.
4. 웹 브라우저 -> 웹 서버 : 공개키로 데이터를 암호화하여 premaster secret을 전송한다.
5. 웹 서버 : 서버의 개인키로 premaster secret을 복호화하여 master secret값으로 저장한다. 
6. HTTPS 통신 연결 : 대칭키 암호화인 session key를 생성하여 이후의 통신에 사용한다.

## DNS
인터넷 도메인의 레코드를 제공하기 위해 네트워크 구간에 설치되어 운영되는 서버이다.
### DNSSEC( DNS Security Extensions )
- 브라우저(클라이언트) : DNS Resolver에 요청한다.
- DNS Resolver : 도메인의 정보를 요청하고 캐시하는 서버로 DNS 서버에 요청한다.
- DNS Server : DNS 정보를 알려주는 서버이다.

## Root CA
Root CA 인증서는 CA에서 자체 서명한 인증서로, 공개키 기반 암호화를 사용한다.  
디지털 인증서는 보안이 필요한 인터넷 통신에서 상대방이 통신하고자 하는 대상이 맞음을 확인시켜준다.
- server -> CA : 사용자에서 keypair를 생성하여 CA에 신원을 증명한다.
- CA -> server : 인증서를 발급한다.
- server -> browser : 공개키를 포함한 인증서를 전달한다.
- browser -> CA : 인증서 확인을 요청하고 CA에서 확인한다.
- browser -> server : 공개키로 암호화된 데이터를 전달한다.
- server : 비밀키로 데이터 복호화 및 열람한다.

## HSTS(HTTP Strict Transport Security)
HTTPS 요청에 대해서만 응답하도록 한다. HSTS에 등록되어 있으면 상태코드 307을 내뱉고 HTTPS로 재전송한다.

# API 보안
## API 구조
로그인, 상품 정보 조회, 구매 등 필요한 로직을 서버 백엔드에 구현하고 클라이언트 API를 통해 백엔드를 호출하는 구조로 많이 사용된다.
### MSA(MicroService Architecture)
*MSA*란,
- 하나의 어플리케이션을 작은 서비스의 집합으로 구현하는 개발 방법이며, 
- HTTP(S)에서의 REST API같은 가벼운 통신 방식을 사용하는 아키텍쳐이다. 

MSA의 일반적인 형태는 loosely coupled 형식이다.  
![](https://imgnew.megazone.com/2020/10/MSA2.jpg)  
> https://www.megazone.com/press_201019_megazonecloud/

API Gateway로 각 서비스의 API endpoint를 호출하여 API 서버로부터 응답을 받는다.

반면에 모놀리식 아키텍쳐는 stronly coupled 형식이다.  
![](https://miro.medium.com/max/714/1*F6y9GeBZwaOzNYnToahfQw.png)  

SOA(Service Oriented Architecture)는 SOAP, XML, UDDI, WSDL 등을 사용하여 웹 기반 분산 시스템의 시초가 된 아키텍쳐이다. HTTP 기반의 **RESTful + API Gateway**를 통해 MSA로 발전하였다.

### API Gateway
<u>MicroService = API</u>라는 전제 아래 대부분의 기능을 API로 정의하고, API Gateway를 매개로 여러 형태의 클라이언트와 public cloud 서버를 사용하였다. 

기능적인 측면은,
- 서비스 탐색
- 보안을 위한 API 인증
- 보안을 위한 API 사용빈도 제한
- API 캐싱
- API 등록 : API 명세를 통해 URL 포함된 REST API 형태로 등록한다. API 명세는 OAS(OpenAPI Specification) 표준으로 사용한다.
- API routing
    - API 요청을 URL, 요청 헤더, 쿼리 변수, 쿠키를 해석하여 API endpoint로 연결한다.
    - 로드밸런싱

## API 인증
API를 호출한 요청이 정상적인 권한이 있는 호출인지를 확인하는 과정이다. 인증은 클라이언트의 신원 확인을 위한 인증(authentication) + 역할 및 권한을 확인하는 인가(authorization)을 이루어진다.
- API key 사용 : 권한이 있는 유저에게만 API key를 발급한다.(ex. OPEN API)
- API token 사용 : ID/PW에 대한 증표로 토큰을 나누어주고, 이후 토큰을 사용한다. 
    1. ID/PW 정보를 base64 인코딩(Authorization:Basic로 요청)하여, HTTPS(암호화)를 통해 로그인한다.
    2. 로그인 성공 시, 인증 서버로쿠터 토큰을 받는다.(토큰은 JWT 형식으로 각 필드값을 claim이라고 한다.)
    3. 이후 요청에서 헤더에 토큰값을 포함하여 증명한다.(Authorization:Bearer + 헤더로 요청한다. *Bearer*는 OAuth 2.0에서 정의한 토큰 전달 방식이다.)

## 메시지 무결성 확인
API를 호출할 때 포함되는 쿼리 매개 변수 등 메시지 내용이 중간에 변경되지 않았음을 증명하는 과정이다.  
- MAC(Message Authenticaion)를 사용한다.(ex. *HMAC*는 해시값을 만들 개인키가 필요하다.)
- API 서버의 부하를 줄이고 빠른 응답을 위해 캐싱을 사용한다.
    - DB 앞단에 Redis, Memcached로 캐싱 레이어를 추가하거나,
    - XML, JSON 형태의 API 결과를 오픈소스 프록시(Nginx, HAProxy)에 캐싱한다.
### 예시
API 개발자(클라이언트)가 API 개발자 등록 서버에 등록하면 응답으로 APP ID, secret key를 전달한다. secret key를 통해 메시지 해시값을 생성하고 이후 API 호출에 함께 전송한다.

## ssh-keygen
SSH(Secure SHell)은 ID/PW를 사용하여 호스트에 접속하는 telnet, rlogin, rsh 등의 보안 취약점을 해소하기 위한 프로토콜이다. 
`ssh-keygen`은 개인키를 먼저 만들고, 개인키 + passphrase로 공개키를 생성하여 암호화 및 복호화에 사용한다. SSH 키는 RSA, DSA, ECDSA 등의 알고리즘을 사용한다.

- 엔터프라이즈 환경에서는 KMI(Key Management Infrastructure)를 사용한다.

# 암호화

## 해싱
해싱은 평문을 해시 함수를 통해 해시 문자열로 변환한다.

### 해싱 vs. 암호화
- 해싱 : 해시값을 생성하여, 데이터 변조가 없었는지 **무결성을 확인**한다.
- 암호화 : **암호화 + 복호화의 2단계**로 이루어지며, 인가되지 않은 제삼자에게 데이터를 노출시키지 않는다.

### 주요 특징
- 같은 문자열을 동일한 해시 알고리즘을 적용하면 같은 해시값이 나온다.
- 다른 문자열을 동일한 해시 알고리즘을 적용하면 다른 해시값이 나온다.
즉, **원본 메시지가 바뀌면 해시값도 변한다.**

### 알고리즘
해싱 알고리즘은, 
- MD 시리즈(MD4, MD5, MD6..)
- SHA 시리즈(SHA-1, SHA-2, SHA-3..)
- RIPEMD
- WhirlPod
등이 있고, 암호화 알고리즘에는
- AEC
- RSA
- 3DES
- ECDSA
등이 있다.

## DTLS(Datagram Transport Layer Security)
*TLS*는 HTTP 같은 TCP 기반의 프로토콜을 암호화하는 반면, *DTLS*는 UDP 기반의 보안으로 TLS에서 파생되었다.  
주로 VPN 클라이언트, WebRTC를 지원하는 브라우저 등이 대표적이다.


## HMAC(Hash-based MAC)
메시지 무결성 알고리즘으로, 해시 알고리즘 + 공유 개인키(shared secret)로 원본 메시지를 해싱 메시지로 변환한다.  
여기서 공유 개인키는 안전하게 공유되어야 하는데 주로 키 교환 알고리즘인 디피-할만 알고리즘을 사용한다.

HMAC은 `Hash(Message, Key) + Message` 형식으로, 송수신자만 공유하는 키 + 원본 메시지를 조합한 해시값을 비교하여 검증한다.

## SSO(Single Sign-On)
SSO는 한번의 로그인으로 여러 서비스를 추가 인증없이 사용한다.  
통합 인증은 AD(Active Directory)나 LDAP(Lightweight Directory Access Point)등을 적용한다. 초기 통합 인증은 SAML 방식을 사용하였으나 많은 태그로 인한 비효율성이 야기되었다.

### 인증 방식
- 세션 쿠키 방식 : SessionID 등을 쿠키로 받아 로그인의 증표로 사용한다. 모든 요청 헤더에 SessionID 쿠키로 넣고, 웹 서버에서 DB의 세션 정보와 비교하여 확인한다. 하지만 이는 리소스 부담이 있는 형식이다.
- 인증 토큰 방식 : 최초 인증이 성공한 사용자에게 인증서버가 토큰을 증표로 발급한다. 세션 정보를 보관하지 않아 리소스 부담이 덜하다.

프로세스는, 
1. 사전에 개인키를 공유한다.
2. ID/PW 확인되면 IdP에서 이메일 + 이름 + 유효기간 등을 사용한 토큰을 발급한다. 토큰은 base64 인코딩되어 개인키를 사용해 서명을 추가하여 JWT/SAML 형식으로 생성된다.
3. HTTPS로 전달된 토큰을 디코딩하여 복호화하여 내용을 확인한다.
4. Service 서버는 개인키로 토큰 변조 여부를 확인하고 인증 처리한다.

access token은 만료기간이 짧아 Refresh token으로 토큰을 갱신하거나 SessionID를 사용하여 로그인 유효기간을 늘린다.