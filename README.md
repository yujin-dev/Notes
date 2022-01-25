# Data Structure

## Array
- 논리적 저장 순서와 물리적 저장 순서가 일치 : 인덱스를 통해 해당 원소에 접근 가능
    - O(1)
    - random access가 가능
- 삭제 또는 삽입에서 해당 원소에 접근하여 작업을 완료하고(O(1)), 추가적으로 삭제한 원소보다 큰 인덱스의 원소들은 shift를 해줘야 함
    - O(n)
## Linked List
- 위의 문제를 해결하기 위한 자료구조
- 각각의 원소들은 다음 원소만을 기억
    - 삭제 및 삽입은 O(1)
- 원하는 위치에 삽입을 하거나 삭제, 정렬하려면 탐색 과정에서 첫번째 원소부터 전부 확인해야 함
    - O(n)

## Stack
- 선형 자료구조로 Last In First Out
## Queue
- 선형 자료구조로 First In First Out

## Tree
- 비선형 자료구조로 계층적 구조
- Node 
- Edge
- Root Node
- Terminal Node
- Internal Node

### Binary Tree
- Perfect Binary Tree : 모든 레벨이 전부 차있는 이진 트리
    ![](https://media.geeksforgeeks.org/wp-content/uploads/binary_tree-1.png)

- Complete Binary Tree : 위에서 아래로, 왼쪽에서 오른쪽으로 순서대로 채워진 이진 트리
    ![](https://cdn.programiz.com/sites/tutorial2program/files/comparison-4.png)

- Full Binary Tree : 모든 노드가 0 또는 2개의 자식 노드만 갖는 이진 트리
    ![](https://media.geeksforgeeks.org/wp-content/uploads/CompleteBinaryTree.png)

- Node갯수 = n개, root가 1에서 시작하면 
    - parent(i) = i/2
    - left child(i) = 2i
    - right chile(i) = 2i+1

### Binary Search Tree
다음과 같은 규칙이 있다.
1. 노드에 저장된 값은 유일
2. 부모 노도의 값 > 왼쪽 자식 노드의 값
3. 부모 노도의 값 < 오르쪽 자식 노드의 값
4. 왼쪽, 오른쪽 서브 트리도 이진 탐색 트리로 구성

- 트리의 높이가 한 층 더해질수록 추가할 수 있는 노드의 수도 2배씩 증가
    - O(log(n))
    - Worst : O(n)

## Binary Heap
- Comple Binary Tree의 일종으로 1번 index부터 Root Node가 시작
- Max Heap : 각 Node의 값이 해당 children 값보다 크거나 같음
    - Root Node의 값이 가장 큼( 최댓값을 찾는 경우 : O(1) )
- 노드 삭제시 맨 마지막 노드를 Root Node로 대체시킨 후 heapify를 거쳐 heap 구조를 유지한다.

## Graph
- Undirected Graph : 방향성이 없는 그래프
- Directed Graph : 방향성이 있는 그래프
- Degree : Undirected Graph에서 각 정점에 연결된 edge의 갯수

- DFS(Depth First Search) 
- BFS(Breadth First Search) :


## `Python`과 `Go`로 구현하는 자료구조
### Python
출처 : https://github.com/OmkarPathak/Data-Structures-using-Python  
참고 : https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html

- array : https://github.com/yujin-dev/Data-Structure/tree/master/Python/array
- dynamic algorithm : https://github.com/yujin-dev/Data-Structure/tree/master/Python/dynamic
- graph : https://github.com/yujin-dev/Data-Structure/tree/master/Python/graph
- heap : https://github.com/yujin-dev/Data-Structure/tree/master/Python/heap
- linked_list : https://github.com/yujin-dev/Data-Structure/tree/master/Python/linked_list
- queue : https://github.com/yujin-dev/Data-Structure/tree/master/Python/queue
- stack : https://github.com/yujin-dev/Data-Structure/tree/master/Python/stack
- tree : https://github.com/yujin-dev/Data-Structure/tree/master/Python/tree

### Go
출처: https://flaviocopes.com/golang-data-structures/

- graph : https://github.com/yujin-dev/Data-Structure/tree/master/Go/Graph
- hash : https://github.com/yujin-dev/Data-Structure/tree/master/Go/HashTable
- queue : https://github.com/yujin-dev/Data-Structure/tree/master/Go/Queue
- set : https://github.com/yujin-dev/Data-Structure/tree/master/Go/Set
- stack : https://github.com/yujin-dev/Data-Structure/tree/master/Go/Stack
- tree : https://github.com/yujin-dev/Data-Structure/tree/master/Go/Tree