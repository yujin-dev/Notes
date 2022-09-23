# File System

## Files
보조 기억 장치에 저장된 연관된 정보들의 집합이다. sequence of bytes라고 정의된다.

### operations
OS는 file operation에 대한 system call을 제공해야 한다.
- create
- write 
- read
- reposition
- delete

### File Access Methods
- sequential access( 순차 접근 ): File을 record(또는 bytes) 단위로 순서대로 접근한다.
- directed access( 직접 접근 ):  원하는 block을 직접 접근한다.
- indexced access: index를 참조하여 원하는 block을 찾아 데이터를 접근한다.

### File System Organization
- Partitions: 논리적인 디스크
- Directory
- Mounting: 현재 FS 에 다른 FS를 붙이는 것

## Directory structure
### Logical directory structure

#### Flat directory structure
FS에 하나의 directory만 존재한다.

#### 2-Level directory structure
사용자마다 하나의 directory를 배정한다.

#### Hierarchical directory structure
tree형태의 계층적 directory 사용 가능하다.
사용자가 하부 directory 생성 및 관리가 가능한 형태로 대부분의 OS가 사용한다.

#### Acyclic Graph directory structure
Hierarchical directory structure의 확장이다. directory 안에 shared directory, shared file을 담을 수 있다.
link를 생성하여 폴더 바로가기를 만들 수 있다.

#### General Graph directory structure
cycle을 허용하기에 파일 탐색 시, infinite loop를 고려해야 한다.

## File Protection
파일에 대한 부적절한 접근을 방지하여 다중 사용자 시스템에서 필요하다.

### File Protection Mechanism
#### Password
각 파일에 password를 입력

#### Access Matrix
도메인과 개체 사이의 접근 권한을 명시한다.

- Global Table: 시스템 전체 파일에 대한 권한을 테이블로 유지한다.
- Access List: Access Matrix의 Column을 list로 표현한다. 파일 생성 시 각 도메인에 대한 권한을 부여한다. 리눅스에서 `ls -a`를 실행할 시 파일마다 표시되는 권한을 나타낸다.
- Capability List: Access Matrix의  Row를 list로 표현한다. 각 도메인에 대한 파일의 접근 권한을 나열한다.

#### Lock-key Mechanism
Access list와 Capability list를 혼합한 개념이다.

### 파일 입출력 시스템
- 유닉스에서는 모든 것을 파일로 취급( virtual file system )
- network를 사용한다는 것도 socket 파일을 열고 읽고 쓰는 개념으로 적용됨

Example> 표준입력/출력/에러를 이용한 간단한 나눗셈
```c
int main()
{
    int a;
    int b;
    char buf[80];

    read(STDIN, buf, 80);
    a = atoi(buf);

    read(STDIN, buf, 80);
    b = atoi(buf);
    if (b==0) 
    {
        write(STDERR, ERRMSG, strlen(ERRMSG)); // 표준에러면 buffer를 사용하지 않고 바로 출력
        return 1;
    }
    sprintf(buf, "%d/%d = %d", a, b, int(a/b));
    
    write(STDOUT, buf, strlen(buf)); // 표준출력이면 buffer를 사용, write하여 출력
    return 0;
}
```

Example> `read()` operaion
```c
# define MAXLEN 80

int main()
{
    int fd; // file description
    int readn = 0;
    char buf[MAXLEN];
    fd = open("test.txt", 0_RDONLY); // read-only
    if(fd<0>)
    {
        perror("File Open Error");
        return 1;
    }
    memset(buf, 0x00, MAXLEN); // 처음 buf를 정의하면 가바지 값이 들어감
    while((readn=read(fd, buf, MAXLAEN-1))>0)
    {
        printf("%s", buf);
    }
}
```

Example> `write()` operation
```c
int main() {
    int fd;
    int i;
    int wdate = 0;
    int wsize = 0;
    fd = open("test.txt", 0_CREAT | 0_WRONLY);
    if (fd<0) {
        perror("File Open Error");
        return 1;
    }
    for (i=0; i<100; i++) {
        wdata = i*2;
        wsize = write(fd, (void*)&wdata, sizeof(int));
        printf("Write %d(%d byte)", wdata, wsize);
    }
    close(fd);
}   
```