## linux 파일/폴더 복사
### 원격 복사
```console
$ scp {host}:{복사하려는 원격 파일경로} {폴더 위치}
```
### 파일 복사 
```console
$ cp {복사하려는 경로} {대상 경로}
```
- `-a` : 파일 속성까지 복사
- `-p` : 원본 파일의 소유자, 그룹, 권한까지 복사
- `-i` : 덮어쓰기 여부를 물음x
- `-r` : 하위 디렉토리 , 파일까지 복사
- `-v` : 현재 복사 진행 상황 표시
- `-u` : 최신 파일이면 복사
- `-b` : 이미 존재하는 파일이면 백업 생성

*[출처] https://jframework.tistory.com/6*


## linux 파일 시간 확인
- 접근 시간 확인: `ls-lu`
- 수정 시간 확인: `ls-l`
- 변경 시간 확인: `ls-lc`

[ 폴더에서 pkl 파일 중 수정 시간이 3일 경과된 파일 갯수 ]
```console 
$ find [folder_name] -name '*.pkl' -mtime +3 | wc -l
```
`-mtime`/`-ctime`/`-atime` +일수 : 수정시간/생성시간/접근시간 일수 이전

`-mtime`/`-ctime`/`-atime` -일수 : 수정시간/생성시간/접근시간 일수 이내

[ 특정 시간 경과한 파일 제거 ]
```console
$ find 폴더 -name 파일명 -mtime +일수 -delete
$ find 폴더 -name 파일명 -mtime +일수 -exec rm -f {} \;
```

*[출처] https://zetawiki.com/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EB%82%A0%EC%A7%9C_%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C_%ED%8C%8C%EC%9D%BC_%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0*

## Windows Performance Monitoring 
### 성능 모니터 기록하기
- https://nogan.tistory.com/17
- https://sagittariusof85s.tistory.com/82


### 주요 성능 카운터 
- https://tshooter.tistory.com/93
- https://www.nextstep.co.kr/121

현재 기록중인 카운터는 
Memory 
- Memory: Commited Bytes( 서버에서 실행 중인 프로세스의 메모리 사용량 ) 
- Memory:Pages/sec( 페이지가 디스크에서 물리 메모리로 쓰여지거나 디스크로 페이지를 옮겨 쓰는 속도 )
- Paging File: %Usage( 현재 사용중인 페이징 파일의 % )
Disk
- Physcial Disk: %Disk Time( 디스크가 읽고 쓰는 요청 )
- Process: Private Bytes( 가상 메모리의 크기 ) 
Network
- Server:Bytes Total/sec( 서버가 네트워크 데이터를 송수신하는 속도 )
- Network Interface: Bytes Total/sec( 네트워크 카드가 데이터를 송수신하는 속도 )
Postgres
- Process: Working Set( 프로세스가 데이터를 저장하기 위해 사용하는 RAM 사용량 측정 )  

## 하드디스크 파티션 생성 및 마운트
/dev/sda, /dev/sdb 등이 하드디스크, /dev/sda1 등이 파티션이다

### 파티션 생성
```console
$ fdisk /dev/sdb
```
### 마운트
파티션을 특정 디렉토리에 연결하여 사용한다.

/dev/sdb1을 /home 디렉토리에 마운트한다.
```console
$ mount /dev/sdb1 /home
```

마운트 해제는 아래와 같다.
```console
$ umount /dev/sdb1
```

#### 리눅스에서 윈도우 파티션 마운트
1. 윈도우 파티션을 연결할 디렉토리를 생성한다.
```console
$ sudo mkdir /mnt/windows
```

2. 마운트할 파티션을 찾는다.
```console
$ sudo fdisk -l 
-------------------------------------------------------------------------------
Device          Start        End    Sectors   Size Type
/dev/sda1        2048    1023999    1021952   499M Windows recovery environment
/dev/sda2     1024000    1228799     204800   100M EFI System
/dev/sda3     1228800    1261567      32768    16M Microsoft reserved
/dev/sda4     1261568 1208397291 1207135724 575.6G Microsoft basic data
/dev/sda5  1952405504 1953521663    1116160   545M Windows recovery environment
/dev/sda6  1208397824 1952405503  744007680 354.8G Linux filesystem
```

3. 파티션을 마운트한다.
```console
$ sudo mount /dev/sda4 /mnt/windows
```

```console
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on

...
/dev/sda4      603567860 247545508 356022352  42% /mnt/windows
```
mount되었음을 알 수 있다.

## OOM Killer
### Memory Overcommit

Memory Commit은 malloc()의 시스템 콜을 통해 Linux 커널에 메모리 할당을 요청하면 커널이 바로 물리 메모리의 영역을 할당하지 않고 요청한 메모리 영역의 **주소값**만 반환하는 것을 의미힌다. 
즉, 물리 메모리에 할당되지 않은 상태이다.

Memory Overcommit은 가상 메모리 시스템은 현재 사용가능한 메모리 영역을 초과한 영역의 반환을 허락하는 것을 의미한다.
`fork()` 시스템 콜과 같은 순간적으로 많은 양의 메모리가 필요한 작업때문에 이러한 기능이 필요하다. 
`fork()` 는 새로운 프로세스를 만드는 시스템 콜인데 호출되면 자식 프로세스는 부모 프로세스의 모든 주소 공간을 복사한다.
부모 프로세스의 메모리 영역을 복사하는 과정에서 memory commit이 일어나고 경우에 따라 overcommit이 필요하다. 
대부분, `fork()` -> `exec()`로 넘어가기 때문에 복사해온 공간을 그대로 사용하는 경우는 거의 없다. 



### OOM Killer(Out of Memory Killer)
memory commit에서 먼저 주소값만 반환하고 해당 주소값에 쓰기 요청이 들어오는 순간에 주소값을 물리 메모리에 실제로 바인딩한다. 
이 때, 실제 메모리와 스왑 메모리를 전부 활용해도 메모리 확보가 불가능하다고 판단되면 프로세스를 강제 종료시키는 것을 OOM이라고 한다.
OOM Killer는 Heuristic하게 프로세스를 종료시킨다.

프로세스마다 커널에 의해 -100 ~ 1000사의 score가 매겨지는데, score가 높은 프로세스가 OOM Killer의 대상이 된다.
`/proc/{process_id}/oom_score`로 score값을 확인할 수 있다.

*[출처]*
- https://blog.2dal.com/2017/03/27/docker-and-oom-killer/
- https://brunch.co.kr/@alden/16


## 캐시 메모리 주기적 삭제
*[출처] https://blog.lael.be/post/1090*

## exit code
종료 상태는 리턴값이라고 부르기도 하는데 이전에 수행한 명령어가 종료될 때 넘겨주는 값을 의미하기 때문이다.

반환값이 필요한 것은 명령어의 성공 여부에 따라 다음 단계로 folk하기 위함이다.
- 종료 상태가 0이여야 성공으로 판단하고, 오류가 있으면 오류 코드를 반환한다.
    - 종료 상태는 0 ~ 255 : 0 = 성공, 1 ~ 255 = 오류 코드
- `exit 100`은 스크립트를 종료하면서 100을 반환한다는 것이다.

*(출처) https://gracefulprograming.tistory.com/70*

<<<<<<< HEAD

## json parser
json 형식의 데이터에서 원하는 key값에 맞는 value를 추출하기 위해 `jq`를 이용한다.
```console
$ sudo apt-get install jq
$ echo "$json" | jq -r '.access_token'
```
=======
## Process
프로세스는 실행 중인 프로그램을 의미한다.  
프로세스 모델은 하나의 프로세스가 하나의 제어 스레드로 프로그램을 실행하는 모델이다. *한 시점에서, 하나의 프로세스 코어에서는 하나의 프로세스만이 실행된다.( 단일 실행 스레드 )*
- 프로세스에는 I/O 바운드와 CPU 바운드가 있다. I/O 바운드는 I/O 작성이 계산 작업보다 많은 프로세스인 반면, CPU 바운드는 계산이 I/O 요청보다 많다.

여러 섹션으로 구성되는데 다음과 같다.
- 텍스트 섹션 : 실행 코드
- 데이터 섹션 : 전역 변수
- 힙 섹션 : 실행 중 동적으로 할당되는 메모리
- 스택 섹션 : 함수 호출 시 임시 저장소로 쓰이는 공간. 함수 매개변수, 복귀주소, 지역 변수를 포괄하는 활성화 레코드를 스택에 push, pop하며 쓰인다.
텍스트 섹션과 데이터 섹션은 크기가 고정되어 있는 반면, 힙 섹션과 스택 섹션은 크기가 동적으로 바뀐다.'

### 프로세스 상태 
- new 
- running
- waiting
- ready
- terminated

### 프로세스 제어 블록( PCB )
PCB에는 프로세스 상태, PC(Process Counter: 다음에 실행할 명령어의 주소), CPU 레지스터, CPU 스케줄링, 메모리 관리, 회계 정보, I/O 상태와 같은 정보가 포함되어 있다.


### 프로세스 스케줄러
- 프로세스 스케줄러에 따라 코어에서 실행 가능한 여러 프로세스 중 하나를 선택하게 된다.
- **다중 프로그래밍 정도**는 현재 메모리에 있는 프로세스의 수를 의미힌다.



## Thread
스레드는 스레드ID + PC(Program Counter) + 레지스터 + 스택으로 구성된다.

### 다중 스레드
- 다중 스레드는 여러 개의 프로세서가 있을 때 여러 스레드를 동시에 실행시킬 수 있는 것을 의미한다.
    - 예를 들어 클라이언트로부터 요청이 들어오면 요청을 서빙할 새로운 스레드를 생성하고 추가적인 클라이언트 요청을 listen하는 작업을 재개하는 케이스가 있다.
- 다중 스레드는 응답성을 높이고 자원 공유할 수 있으며 경제성과 scalability의 장점을 가진다.
- 여러 컴퓨터 코어를 가지는 다중 코어의 병렬성을 증진시킨다.
- 병렬성과 병행성을 다른 개념인데 병렬 실행에는 데이터 병렬 실행과 태스크 병렬 실행이 있다. **데이터 병렬 실행**은 하나의 연산에 대해 데이터를 분배하여 실행하고 **태스크 병렬 실행**은 태스크를 분배하여 실행시키는 것을 의미한다.
- 스레드 라이브러리는 커널이 아닌 사용자 공간에서 지원되는 경우와 커널 수준에서 지원되는 경우가 있다. 커널 수준의 라이브러리에는 unix 시스템의 pthreads가 있다.
- 다수의 스레드를 생성하는데 **비동기 스레딩**과 **동기 스레딩**이 있다. 비동기 스레딩은 부모가 자식 스레드를 생성하고 독립적으로 실행되며 데이터를 거의 공유히지 않는다. 동기 스레딩은 부모가 자식 스레드를 생성하고 자식 스레드가 종료될 떄까지 기다리다가 부모 스레드가 실행된다. 동기 스레딩에서는 데이터를 공유하는 부분이 많다.

#### 암묵적 스레딩
- 스레드 풀 : 여러 스레드를 pool로 묶어 스레드 요청이 들어오면 사용 가능한 스레드를 실행시키는 방식이다. 새로운 스레드를 생성하는 비해 속도가 빠르며 스레드 갯수를 제한할 수 있는 장점이 있다.
    - Fork Join : 실제 스레드 수를 결정하는 동기 버전의 스레드 풀이다.
>>>>>>> edb4f444679801f1a3d6c9da4b0670ac611bef1c
