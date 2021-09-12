# Process Scheduling

## 스케줄링
*다중 프로그래밍*이란 여러 개의 프로세스가 시스템 내 존재하는 것을 의미한다.스케줄링은 자원을 할당 할 프로세스를 선택한다. 

### 자원 관리
- 시간 분할 관리 : 하나의 자원을 여러 스레드가 번갈아 사용하는 것을 의미한다.
- 공간 분할 관리 : 하나의 자원을 동시에 사용한다.

### 목적 
시스템의 성능을 향상시키기 위함이다. 아래의 성능 지표 중에 목적에 맞는 것을 고려하여 스케줄링 기법을 선택한다.
- 응답시간 : interactive system
- 작업 처리량(throughput): 단위 시간동안 완료된 작업 수, batch system
- 자원 활용도: 자원이 활용된 시간의 정도

### 기준
#### 프로세스의 특성
프로세스 수행은  CPU 사용 + I/O 대기로 이루어진다. 
- compute-bounded: CPU burst가 더 많은 경우
- I/O-bounded: I/O burst가 더 많은 경우

#### 시스템 특성
#### 프로세스의 긴급성
#### 프로세스의 우선순위

### 단계
발생하는 빈도 및 할당 자원에 따른 구분된다.
#### long-term scheduling
- Job scheduling
- Job -> created: 시스템에 등록할 Job을 결정하는 스케줄링
- 다중 프로그래밍 정도( 시스템 내 프로세스 수 조절)을 조절한다. 

#### mid-term scheduling
- 메모리 할당을 결정한다. 
- suspended ready -> ready로 넘어가는 swap-in에서 자주 발생한다.
- swapping( swap-in/ swap-out) 

#### short-term scheduling
- 프로세스 스케줄링: CPU를 할당하는 경우
- ready -> running로 넘어가는 dispatch에서 자주 발생한다.
- 가장 빈번하게 발생하여 매우 빨라야 한다.

### 정책

#### 선점 vs. 비선점 스케줄링
- Non-preemptive scheduling: 할당 받을 자원을 스스로 반납할 때까지 사용한다.
- Preemptive scheduling: 자원을 빼앗길 수 있다. 실시간 시스템에 적합하나 context switch overhead가 크다.

#### Priority
프로세스의 우선순위를 정한다.
- Static  Priority: 프로세스 생성시 결정된 우선순위가 유지된다.
- Dynamic Priority: 프로세스의 상태 변화에 따라 우선순위가 변경한다.

## 스케줄링 알고리즘

### FCFS( First Come First Service )
- 먼저 오는 프로세스를 할당한다.
- Non-preemptive scheduling
- 기준: 도착 시간( ready queue )
- 자원에 활용도가 높다: 스케줄링 overhead가 높고 CPU가 계속 가동된다.
- Batch system에 적합하다: 오는 순서대로 빠르게 처리할 때 유용하기 때문
- 평균 응답시간이 길기 때문에 interactive system에 부적합하다.
- 수행시간이 긴 프로세스 때문에 그 뒤에 실행될 프로세스의 대기시간이 길어진다( Convoy effect )

### RR( Round Robin )
- 돌아가면서 프로세서를 사용한다.
- Preemptive scheduling
- 기준: 도착 시간( ready queue )
- 자원 사용에 제한 시간( time quantum )이 있다.: 할당된 시간이 지나면 자원을 반납시켜 자원 독점을 방지한다.
- context switch overhead가 크다.
- interactive, time-sharing 시스템에 적합하다.
- time quantum이 성능을 결정한다. 

### SPN( Shortest Process Next )
- 실행 시간(Burst time)이 가장 작은 프로세스들 먼저 처리한다.
- Non-preemptive scheduling
- 평균 대기시간이 최소화되, 시스템 내 프로세스 수 최소화된다.
- 무한대기( Starvation )현상이 발생한다.
- 정확한 실행시간이 필요하여 실행시간 예측 기법이 필요하다.

### SRTN( Shortest Remaining Process Next )
- SPN -> 남은 시간이 적은 프로세스를 먼저 처라한다.
- Preemptive scheduling: 잔여 실행 시간이 더 적은 프로세스가 ready가 되면 선점된다.
- SPN 장점 극대화
- 총 실행시간에 더해 잔여 실행을 계속 추적해야 해서 사용하기에는 비현실적이다.

### HRRN( High-Response-Ratio-Next )
- SPN + Aging concepts
- Non-preemptive scheduling
- Aging concepts: 프로세스의 대기 시간을 고려한다.
- 기준: response ratio가 높은 프로세스가 우선된다.
- response ratio = (WT+BT)/BT으로, 실행시간 대비 대기 시간+실행시간
- 정확한 실행시간이 필요하여 실행시간 예측 기법이 필요하다.

### MLQ( Multi-Level Queue )
- 작업별 별도의 ready queue를 가진다: 최초 배정된 queue가 고정된다.
- queue사이에 우선순위를 가진다.
- queue관리에 대한 스케줄링 overhead가 있고 우선순위가 낮은 경우 무한대기가 발생할 수 있다.

### MFQ( Multi-Level Feedback Queue )
- queue간 이동이 허용된다: feedback을 통해 우선 순위가 조정된다.
