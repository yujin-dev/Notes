# About Database

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

*[출처] https://mozi.tistory.com/209* 

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

![] (https://habrastorage.org/r/w780/webt/az/jk/2b/azjk2b81tsv0jj1_yeb-fhv7xjm.png)

cache는 처음에는 빈 buffer를 포함한다. cache의 hash table를 통해 page를 빠르게 찾도록 한다.

#### Search for a page in the cache
프로세스가 page를 읽을 때면 hash table을 이용해 buffer cache에서 탐색한다. 필요한 page를 찾으면 프로세스는 pin count를 증가시켜 buffer를 *pin*시킨다.  

*[출처] https://habr.com/en/company/postgrespro/blog/491730/*
