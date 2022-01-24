# About Network
## Web Design Pattern - MVC vs. MTV

### MVC(Model-View-Controller)
![](https://media.vlpt.us/images/inyong_pang/post/9205bb36-7b6b-45d3-bca5-f03e6c22ff92/image.png)

유저가 Controller를 조작하면 Model을 통해 데이터를 가져오고 데이터를 View를 통해 전달한다.
- Model : 쿼리에 대한 정보를 정의하여 DB에 접근하고 CRUD를 명시한다.  
- View : Controller로부터의 데이터를 브라우저에 랜더링하도록 변환한다.
- Controller : Model과 View사이의 로직을 담당하여 유저가 Model에 맞는 인자값을 요청한다.

## HTTP
HTTP(HyperText Transfer Protocol)은 stateless 프로토콜이다. 

- TCP/IP 상에서 작동 
- Connectless :  
요청해서 응답을 받으면 연결을 끊는다.
- Stateless :   
    stataless는 데이터를 주고 받는 요청이 서로 독립적이라는 의미다.  
    즉, 이전과 이후의 데이터 요청은 관련이 없다.
    이에 따라 서버는 세션과 같은 추가 정보를 관리하지 않아도 되고 다수의 요청에 의한 부하를 줄일 수 있는 이점이 있다. 하지만 클라이언트가 이전에 로그인 되더라도 
    정보를 유지할 수 없어 HTTP는 Cookie를 이용한다.


### HTTP Request & HTTP Response
![](https://joshua1988.github.io/images/posts/web/http/http-full-structure.png)

- URL 분석 및 접속 : 서버 IP주소와 port를 이용하여 TCP/IP 연결을 요청한다.
- Request Header 전송
- Request Body 전송
- Response Header 해석 : 상태 코드를 확인하고 Body의 Content-Type을 해석한다.
- Reponse Body 해석

#### Request
![](https://media.vlpt.us/images/dnjscksdn98/post/319733fc-8fcb-48d3-8880-7932485162ee/http_request.png)

#### Response
![](https://media.vlpt.us/images/dnjscksdn98/post/42caeb0f-83f0-41e3-bfc7-ad169dbed518/http_response.png)


### URL Format
![](https://joshua1988.github.io/images/posts/web/http/url-structure.png)

### HTTP Methods
- GET( 요청 )
- POST( 생성 )
- PUT( 수정 )
- DELETE( 삭제 )
- HEAD( 서버 헤더 정보, Body 반환하지 않음 )
- OPTIONS( 서버 옵션 확인 )

### HTTP 상태 코드
- 2xx : 성공( 200, 204, .. )
- 3xx : redirection( 301, 303, .. )
- 4xx : 클라이언트 오류( 400, 401, 403, ..)
- 5xx : 서버 오류( 501, 503, ..)

### vs. HTTPS
SSL은 보안을 위해 개발한 통신 layer이다. HTTPS는 SSL위에 HTTP를 통과시켜 암호화해서 주고 받는 형식이다.

![](https://media.vlpt.us/images/dnjscksdn98/post/e0fc9ec6-24fb-402b-a6bc-9492c5371a5b/https.png)


*(출처)*
- https://joshua1988.github.io/web-development/http-part1/
- https://velog.io/@dnjscksdn98/HTTP-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC

## OSI 7 Layer - TCP/IP
![](https://t1.daumcdn.net/cfile/tistory/99F6363359FDDC9E1F)

*(출처) https://mangkyu.tistory.com/15*
*(참고) https://helloworld-88.tistory.com/146*

### OSI 7 Layers

[ User Process ]

1. Application : Email, FTP, ..
2. Presentation 
3. Session : 논리적 접속

[ Kernel ]

4. Transport : TCP/UDP 프로토콜을 활용, 양쪽 간의 신뢰성 보장
5. Network : IP 주소 체계( IPv4, IPv6 )에 따라 경로 설정
6. Datalink : 두 node간 통신
7. Physical : 이진bit로 전달


#### Physical( 물리 계층 )
![](./png/2022-01-08-17-21-58.png)


## TCP vs. UDP

### TCP
TCP는 인터넷 상에서 데이터를 메시지 형태로 보내기 위해 IP와 함께 사용하는 프로토콜이다.
일반적으로 IP와 함께 사용하는데 TCP는 패킷을 추적, 관리한다.  
![](https://t1.daumcdn.net/cfile/tistory/991BEB3359FEB5712F)


- 연결형 서비스로, 가상 회선 방식을 제공(발신지 - 수신지를 연결하여 논리적 경로를 배정)
- 연결은 3-way handshaking( 목적지와 수신지를 확실히 하여 정확한 전송을 보장하고자 )으로, 해제는 4-way handshaking로 한다.
- 높은 신뢰성
- UDP보다 속도는 느림
- Point to point 방식
- 서버 : 클라이언트 연결이 1:1 연결

[ TCP Flow ]  
![](https://t1.daumcdn.net/cfile/tistory/99C5C63359FEB5DC06)


#### UDP
UDP는 데이터를 데이터그램(독립적인 관계를 지닌 패킷) 단위로 처리하는 프로토콜이다.  
![](https://t1.daumcdn.net/cfile/tistory/9969973359FEB59309)

- 비연결형 서비스로, 데이터그램 방식을 제공
- UDP 헤더의 CheckSum 필드를 통해 최소한의 오류만 검출
- 낮은 신뢰성
- TCP보다 속도가 빠름( 실시간 서비스에 주로 사용 )
- 서버 : 클라이언트는 N:M 연결이 가능

[ UDP Flow ]  
![](https://t1.daumcdn.net/cfile/tistory/9934293359FEB5EE38)

*(출처) https://mangkyu.tistory.com/15*

## NAT
NAT(Network Address Translation)은 패킷의 IP주소, 포트 등을 변환하는 방안이다.

- NAT는 private network가 외부 public network와 통신하기 위해 사용된다.
- 외부와 통신할 때 패킷에 기록된 IP, 포트를 변환하여 외부에서 활용할 수 있는 Public IP로 변환한다.

### AWS NAT
- NAT Instance
- NAT Gateway

*(출처) https://velog.io/@wowtjdwo/NAT%EC%99%80-IGW*


## XML vs. SOAP
- XML(EXtensible Markup Language)은 데이터와 텍스트를 인코딩하는 간단한 표준 방식을 제공하여 하드웨어, OS, application 간에 교환 가능한 마크업 언어이다.
- SOAP은 XML기반의 통신 프로토콜이다.


## TLS/SSL/HTTPS
- TLS/SSL은 TCP/IP 네트워크 통신에 적용되는 보안을 위한 암호 규약이다.
- HTTPS는 HTTP 통신에서 암호화되는 규약이다.

### 암호화
- 대칭키
    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb1qb4Z%2FbtqGfNniI1P%2FJIx3kglkOTpXZeT9WEOsUK%2Fimg.png)

- 비대칭키 : 한 쌍의 키로 암호화, 복호화를 하는 방식은 RSA 알고리즘이라 한다.
    ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcG84VM%2FbtqGnJpEXsr%2FJVefe1KT14Yo7nqkuhRzX0%2Fimg.png)

TLS는 RSA 비대칭키 방식을 이용하여 대칭키를 공유하고, 실제 통신은 CPU 리소스가 적은 대칭키로 데이터를 주고 받는다.

*(출처) https://babbab2.tistory.com/4*

## Protocal Buffers
프로토콜 버퍼란 구글에서 개발한 구조화된 데이터를 직렬화하기 위한 프로토콜이다.
- 파이썬에서는 pickling을 사용 : 언어에 내장되어 있지만 다른 언어간 호환이 되지 않음

###  예시 
주소록 파일에 개인 정보 기록하기 

#### 프로토콜 형식 정의
`addressbook.proto` 메시지를 정의한다.

```.proto
syntax = "proto2";

package tutorial;

message Person { // 메시지 정의
    optional string name = 1; 
    optional int32 id = 2;
    optional string email = 3;

    enum PhoneType {
        MOBILE = 0;
        HOME = 1;
        WORK = 2;
    }
    message PhoneNumber {
        optional string number = 1;
        optional PhoneType type = 2 [default = HOME];
    }
    
    repeated PhoneNumber phones=4;
}

message AddressBook {
    repeated Person people = 1;
}
```
#### 프로토콜 버퍼 컴파일
1. 컴파일러 패키지를 설치
2. `protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/addressbook.proto`

#### 프로토콜 버퍼 API
python에서 buffer compiler는 데이터 접근 코드를 직접 생성하지 않고 descriptors를 통한다.

```python
class Person(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType

  class PhoneNumber(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PERSON_PHONENUMBER
  DESCRIPTOR = _PERSON

class AddressBook(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDRESSBOOK

```
- `SerializeToString` : 메시지를 직렬화하여 문자열로 반환
- `ParseFromString` : 메시지를 분석

#### 메시지 작성
1. 프로토콜 버퍼 클래스 인스턴스를 만든 후 출력 스트림에 써야 한다.
2. `AddresssBook`파일에서 읽고 `Person` 입력에 따라 새 파일 다시 쓴다.

```python
import addressbook_pb2
import sys

def PromptForAddress(person):
  pass

address_book = addressbook_pb2.AddressBook()
try:
    f = open(sys.argv[1], "rb")
    address_book.PromptForAddress(f.read())
    f.close()
except IOError:
    print( sys.argv[1] + ": Could not open file.  Creating a new one.")

PromptForAddress(address_book.people.add())

f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
```
#### 메시지 읽기
```python
def ListPeople(address_book):
    pass

address_book = addressbook_pb2.AddressBook()
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)
```    

*(출처) https://developers.google.com/protocol-buffers/docs/pythontutorial*