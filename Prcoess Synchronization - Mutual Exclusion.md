# Prcoess Synchronization and Mutual Exclusion
동기화란 프로세스들이 서로 정보를 공유하여 동작을 맞추는 것을 의미한다.
병행 수행중인 비동기적 프로세스들이 공유자원에 동시 접근할 때 문제가 발생하므로 동기화가 필요하다.

- Shared Data: 여러 프로세스가 공유하는 데이터
- Critical Section: 공유 데이터를 접근하는 코드 영역
- Mutual Exclusion: 둘 이상의 프로세스가 동시에 Critical Section에 진입하는 것을 방지한다.

## Critical Section

- Machine Instruction: Atomicity, Indivisible의 특징으로 한 기계어 명령의 실행 도중에는 인터럽트 받지 않는다.

![](2021-09-12-20-06-44.png)

1,2,3,A,B,C은  Machine Instruction로 인해 개입될 수 없다. 1,2,3,A,B,C은 각각 끝날때 preemption이 발생할 수 있는데 순서에 따라 다른 결과가 나올 수 있다.

![](2021-09-12-20-09-44.png)

## Mutual Exclusion
프로세스가 Critical Section가 있을 때 다른 프로세스가 진입하는 것을 막는다.

### Mutual Exclusion Primitives( 기본연산 )
- enterCS() primitive:Critical Section진입 전 검사
- exitCS() primitive: Critical Section 벗어날때의 후처리 과정

### Mutual Exclusion Primitives 요구
- Mutual Exclusion
- Progress( 진행 ): Critical Section안에 있는 프로세스 외에는 다른 프로세스가 진입하는 것을 방해하지 않는다.
- Bounded waiting( 한정대기 )

## SW Algorithm

### Dekker's Algorithm
Two process Mutual Exclusion을 보장하는 최초의 알고리즘

#### Dijkstra Algorithm

## HW Algorithm

### TestAndSet( TAS ) instruction
busy waiting의 문제가 있다.

## OS supported SW Algorithm
### Spinlock
- 정수 변수
- 초기화, P(), V() 연산으로만 접근 가능

멀티 프로세서 시스템에서만 사용 가능
Busy waiting

### Semaphore