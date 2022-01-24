# HBase Documentation

[HBase 공식문서](https://hbase.apache.org/book.html)

## Architecture
Hbase는 NoSQL 분산 데이터베이스이다.

다음과 같은 특징이 있다.
- 일관된 Read/Write
- 자동 샤딩
- 자동 RegionServer 장애 조치
- Hadoop/HDFS 통합
- MapReduce : 대규모 병렬처리 지원
- 대용량 쿼리 최적화를 위한 블록 캐시 및 블룸 필터를 지원

1. 보통 수억, 수십억 개의 행이 있는 경우에 좋은 후보이다.
    수천/수만 개의 행만 있는 경우 모든 데이터가 단일 노드에 있기에 기존 RDBMS를 사용하는 것이 더 나을 수 있다.

2. RDBMS가 제공하는 기능( 정형화, 보조 인덱스, 트랜잭션, 고급 쿼리 등) 없이도 사용 가능한지 확인해야 한다.
3. 하드웨어가 충분하지 : 5개 미만의 DataNode와 NameNode에서는 잘 작동하지 않는다.

### HDFS와 차이점
HDFS는 대용량 파일 저장에 적합한 분산 파일 시스템으로 HBase는 HDFS 기반으로 구축된 큰 테이블에 대한 빠른 레코드 조회를 제공한다.

### 클라이언트
HBase 클라이언트는 특정 행 범위를 제공하는 RegionServer를 찾는다.
필요한 서버를 찾으면 마스터를 거치지 않고 서버에 접속하여 Read/Write 요청한다.

### 마스터
`HMaster` 마스터 서버의 구현이다.
마스터 서버는 클러스터의 모든 RegionServer 인스턴스를 모니터링하며 모든 메타데이터 변경에 대한 인터페이스다.

### RegionServer
`HRegionServer` RegionServer 구현이다.
지역 서비스 및 관리를 담당한다. 분산 클러스터에서 RegionServer는 DataNode에서 실행된다.

`Replica_id` = 0이면 primary 지역 서비이다.

### HDFS
NameNode는 파일 시스템 메타 데이터를 유지 관리한다.
DataNode는 HDFS 블록 저장을 담당한다.

### 고가용성 읽기
고가용성 Read를 위해 HBase는 region replication를 이용한다. 테이블의 각 영역에 대해 서로 다른 RegionServer에서 여러 복제본이 있다. 기본적으로 복제는 1로 설정되어 있으면 2이상 설정되면 마스터는 테이블 영역에서 복제본을 할당한다.

#### Timeline Consistency
```
public enum Consistency {
    STRONG.
    TIMELINE
}
```

![](https://hbase.apache.org/images/timeline_consistency.png)

위에서 모든 쓰기는 primary 지역 복제본에서 처리된다. 쓰기는 WAL을 통해 미리 쓰기로 저장되고 다른 복제본에 비동기식으로 복제된다.

>>https://hbase.apache.org/book.html#arch.timelineconsistent.reads