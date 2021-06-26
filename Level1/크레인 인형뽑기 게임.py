EMPTY = 0

def put(bucket, doll):
    '''bucket에 인형을 넣는다. 
    만약 동일한 타입의 인형이 두 개라면 터뜨리고 그 개 수를 반환한다.'''
    if doll == EMPTY:
        return 0
    if bucket and bucket[-1] == doll:
        bucket.pop(-1)
        return 2
    bucket.append(doll)
    return 0

def get(board, col):
    'board에서 모든 row, 특정 col을 순회하여 인형을 꺼낸다.'
    for row in range(len(board)):
        doll = board[row][col]
        if not doll == EMPTY:
            board[row][col] = EMPTY
            return doll
    return 0

def solution(board, moves):
    '''
    Args:
        board: List[List[Int]]
        * 5x5 ~ 30x30 크기의 게임 판
        * 0은 빈칸, 1~100은 특정 종류의 인형을 의미
        moves: List[Int]
        * 1~board의 가로크기
        * 해당 위치의 인형을 하나 꺼낸다.
    Returns:
        Int: 사라진 인형의 개수를 출력한다.
    '''
    bucket = []
    count  = 0

    for move in moves:
        # move와 배열의 인덱스는 1의 차이가 있다.
        doll = get(board, move-1)  
        count += put(bucket, doll)
    return count
