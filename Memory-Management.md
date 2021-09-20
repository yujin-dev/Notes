# Memory Management

### 메모리의 종류
![](./img/2021-09-16-10-38-58.png)

### 메모리 계층구조
![](./img/2021-09-20-16-11-33.png)

- block : 디스크에서 1bit를 메모리에 올리는 최소 단위. 보조기억장치와 주기억장치 사이의 데이터 전송 단위이다. block 단위만큼 메모리에 올라간다. 
- word: 메모리에서 레지스터에 올라가는 데이터 전송 단위. 32bit PC, 64bit PC에서의 bit 단위가 word 크기를 의미한다.

### Address Binding
프로그램 논리 주소를 실제 메모리의 물리 주소로 매핑하는 작업을 의미한다. 
- Compile time binding : 프로세스가 메모리에 적재된 위치를 컴파일러가 알 수 있는 경우.
- Load time binding: 메모리 적재 위치를 컴파일 시점에서 모르면 상대 주소로 생성한다. 적재 시점에 시작 주소를 반영하여 로드할 시 주소를 재설정한다.
- Run time binding: ready 에서 running에서 주소를 할당한다. 대부분의 OS가 사용하는 방식이다.

### Dynamic Loading
모든 루틴을 교체 가능한 형태로 디스크에 저장한다.

### Swapping
swap-in, swap-out

## Memory Allocation

### Continuous Memory Allocation
프로세스를 하나의 연속된 메모리 공간에 할당하는 정책이다. 

#### Uni-programming
프로세스에 한번에 하나만 올라가는 경우(  Multiprogramming degree = 1)
- 프로그램의 크기가 메모리 크기보다 클 경우, Overlay structure로 메모리에 현재 필요한 영역만 적재한다.
하지만 사용자가 프로그램의 흐름과 자료구조를 알고 있어야 가능하다.
- 커널을 보호하기 위해 경계 레지스터( boundary register )를 사용한다.
- 하나의 프로세스만 올라가기에 시스템의 활용도가 낮다. 

#### [ Multi-programming ] Fixed Parition Multiprogramming

- 메모리 공간을 고정된 크기로 미리 분할한다. 
- 각 프로세스는 하나의 partition에 적재된다. 
- Multiprogramming degree가 분할한 고정 크기와 동일하다.
- 단편화가 발생하여 메모리가 낭비되는 문제가 있다.

[ Fragmentation ]
- Internal Fragmentation : Partition 크기 > Process 크기

![](./img/2021-09-20-17-05-03.png)

Process1, 2 에서 할당된 메모리 공간 외의 남는 9MB, 10MB를 내부 단편화가 발생하여 메모리가 낭비된다.

- External Fragmentation: 남은 메모리 크기 > Process 크기 이지만, 연속된 공간이 아닌 경우이다. 마찬가지로 메모리 낭비가 발생한다.

#### [ Multi-programming ] Variable Parition Multiprogramming

- 프로세스를 처리하는 과정에서 필요할 때 메모리 공간을 동적으로 분할한다. 

![](./img/2021-09-20-17-13-03.png)

partion이 요청한 크기에 따라 할당된다.

[ 배치 전략 ]

![](./img/2021-09-20-17-22-54.png)

새로 들어오는 프로세스 P에 대해 남는 공간 중 어디에 배치할 것인가.

- First-Fit(최초 적합): 충분한 크기를 가진 partition 중 첫 번쨰를 선택한다. 간단하고 overhead가 적지만 공간 활용률이 떨어질 수 있다. -> (1)
- Best-Fit(최적 적합): 프로세스가 들어 갈 수 있는 partition중 가장 작은 곳을 선택한다. 모든 partition을 탐색해야 해서 overhead가 크다. 하지만 크기가 큰 partition을 유지할 수 있다. -> (1)
- Worst-Fit(최악 적합): 프로세스가 들어 갈 수 있는 partition중 가장 큰 곳을 선택한다. 모든 partition을 탐색해야 해서 overhead가 크다. 크기가 작은 partition을 유지할 수 있으나 큰 공간의 partition 확보가 어렵다. -> (3)
- Next-fit(순차 최초 적합): 마지막으로 탐색한 위치부터 탐색한다. 메모리 영역의 사용 빈도를 균등화할 수 있고 overhead가 작다. 

[ External fragmentation issue ]

![](./img/2021-09-20-17-25-45.png)

- Coalescing holes(공간 통합): 인접한 빈 영역을 하나의 partition으로 통합하여 공간을 확보하여 수행한다. 
- Storage Compaction(메모리 압축): 모든 빈 공간을 하나로 통합한다. 기존의 메모리에서 돌아가던 프로세스를 중지하고 재배치하여 overhead가 크다.