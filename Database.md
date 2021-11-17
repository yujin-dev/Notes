# About Database
데이터베이스는 기본적으로 오라클을 기반으로 한다.

## COMMIT & ROLLBACK
COMMIT을 통해 트랜젝션을 완료한다.

COMMIT, ROLLBACK 이전의 데이터는
- 메모리 버퍼에만 영향을 받았기에 데이터 변경 이전으로 복구할 수 있다.
- 현재 사용자는 SELECT문으로 결과를 확인할 수 있으나,
- 다른 사용자는 현재 사용자가 수정한 결과를 확인할 수 없다.
- 변경된 행은 잠금이 걸려있어 다른 사용자가 동시에 수정할 수 없다.

### COMMIT
COMMIT 이후의 데이터는
- 변경 사항이 DB에 반영된다.
- 이전 데이터는 폐기된다.
- 모든 사용자는 결과를 확인할 수 있다.
- 관련된 행에 대한 잠금이 풀려 다른 사용자가 수정할 수 있다.

#### ROLLBACK
COMMIT 이전이면 ROLLBACK을 통해 데이터 변경 사항이 취소되어 이전 상태로 복구된다.

*(출처) https://mozi.tistory.com/209* 

## WAL in PostgreSQL(WIP)
DBMS에서 데이터는 RAM에 저장된 후 비동기적으로 disk에 쓰여진다. 하지만 DBMS나 OS에 이상이 생기면 데이터가 증발할 수 있어 이를 방지하기 위해 Write-ahead logging(WAL)을 사용한다.

buffer cache는 RAM에 저장되는 구조이다. buffer cache를 통해 RAM과 disk에 접슨하는 시간 차이를 줄인다.

OS에서도 disk cache를 사용하는데 buffer cache는 disk에 직접적으로 접근하여 중복 캐싱을 피한다.

### Buffer cache

#### DBMS buffer cache
각각의 buffers는 하나의 데이터 page + header로 구성된다. header는, 
- buffer에서 page의 위치
- page에서 데이터 변경 사항
- buffer의 usage count
- buffer의 pin count
를 포함한다.

buffer cache는 서버의 공유 메모리에 위치하며 모든 프로세스에 접근 가능하다. 데이터를 이용하려면 프로세스는 cache로 page를 읽어드린다. page가 cache에 있는 동안 RAM에서 작업하여 disk에 저장한다.

![](https://habrastorage.org/r/w780/webt/az/jk/2b/azjk2b81tsv0jj1_yeb-fhv7xjm.png)

cache는 처음에는 빈 buffer를 포함한다. cache의 hash table를 통해 page를 빠르게 찾도록 한다.

#### Search for a page in the cache
프로세스가 page를 읽을 때면 hash table을 이용해 buffer cache에서 탐색한다. 필요한 page를 찾으면 프로세스는 pin count를 증가시켜 buffer를 *pin*시킨다.  

*(출처) https://habr.com/en/company/postgrespro/blog/491730/*


## Random Access
**랜덤 액세스**는 데이터를 저장하는 블록을 한번에 여러 개 접근하는 것이 아니라 한 번에 하나의 블록만을 접근하는 싱글 블록 I/O 방식이다.
반대로, Table Full Scan은 한 번에 여러 개의 블록을 접근하는 멀티 블록 I/O 방식인다.

Index Scan시 Read 블록에는 테이블의 행을 가리키는 ROW ID가 존재한다.  
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmxJq2%2FbtqAjnBactq%2FsVikDrOeHCCWCdOlL8kkU1%2Fimg.png)

Index Scan에서 데이터를 탐색하는 주소 값인 ROW ID를 확인하여 테이블에 액세스한다.

- 확인 랜덤 액세스 : `WHERE`조건에서 컬럼이 인덱스에 존재하지 않아 테이블을 액세스한다.
- 추출 랜덤 액세스 : `SELECT`절의 컬럼을 결과로 추출하기 위해 테이블에 액세스한다.
- 정렬 랜덤 액세스 : `ORDER BY`, `GROUP BY`절 컬럼이 인덱스에 존재하지 않아 추가하기 위해 테이블에 액세스한다.

랜덤액세스 중 추출되는 데이터를 감소시키는 확인 랜덤 액세스르르 감소시키는 방안이 성능에서 중요하다.

*(출처) https://blackhairdeveloper.tistory.com/3*

### Sequential Access vs. Random Access
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F99F0DA385B34CA9811F88F)

Sequential Access는 논리적, 물리적으로 연결된 순서에 따라 차례대로 블록을 읽어들이는 방식이다. 
인덱스 Reaf 블록은 앞뒤를 가리키는 주소값으로 연결되어 있기에 이를 이용하여 순차적으로 스캔한다.(Full Scan)

Random Access는 논리적, 물리적 순서가 아닌 레코드 하나를 위기 위해 한 블록씩 접근하는 방식이다.

*(출처) https://wedul.site/400*

## 데이터베이스 I/O 메커니즘
데이터베이스는 디스크로 구성되어 있기에 SQL튜닝은 I/O튜닝이다.
SQL이 느린 이유는 디스크 I/O를 처리하는 동안 프로세스가 놀기 때문이다. 
디스크에서 데이터를 읽어야 할 경우, CPU를 OS에 반환하고 waiting 상태에서 I/O 가 완료되길 기다린다.


### 데이터베이스 저장 구조

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F9927AB345B28631024F7A6)

*(출처) https://wedul.site*

데이터베이스는 테이블스페이스라는 논리적 저장 영역 단위로 나뉘어진다.
- 테이블스페이스에는 다수의 논리적 데이터 블록이 있다.( 블록의 크기는 기본 8kb이고, 2kb ~ 32kb이다. ) 데이터 블록은 가장 작은 논리적 I/O 단위이다.
- 연속된 논리적 블록이 일정 갯수가 되면 extent가 형성된다.
- 논리적 구조에 할당된 extent 집합은 하나의 segment를 형성하게 된다.


**[ 테이블 데이터가 저장되는 방식 ]**

![](https://mblogthumb-phinf.pstatic.net/20120430_168/scleemct2_1335763547494Q68j2_JPEG/K-2.jpg?type=w2)

- 논리적으로, Table은 각 Column의 값이 기입된 Row들로 구성된다.
- Row는 데이터베이스 블록에 저장된다.

![](https://mblogthumb-phinf.pstatic.net/20120430_227/scleemct2_13357644485348wNlB_JPEG/K-3.jpg?type=w2)

#### DBA( Data Block Address )
데이터 블록에서 고유 주소값으로 디스크에서 몇 번 데이터 파일의 몇 번째 블록인지를 의미한다.

인덱스를 이용해 테이블 레코드를 읽을 때 인덱스 ROW ID를 이용하며 ROW ID는 DBA + Row 번호로 구성된다.

### 논리적 I/O vs. 물리적 I/O
SQL 처리하는 과정에는 2가지 I/O가 존재한다. 
- 논리적 I/O : 메모리 버퍼 캐시에서 발생하나 총 블록 I/O로, 메모리에 접근하여 데이터를 가져온 블록 수이다.
- 물리적 I/O : 디스크에서 발생한 총 블록 I/O.

*(출처)*
- https://wedul.site
- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=scleemct2&logNo=40158022542
- https://velog.io/@berry719/1.3-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%80%EC%9E%A5-%EA%B5%AC%EC%A1%B0-%EB%B0%8F-IO-%EB%A9%94%EC%BB%A4%EB%8B%88%EC%A6%98
