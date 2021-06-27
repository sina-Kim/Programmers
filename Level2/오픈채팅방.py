from collections import defaultdict
from typing      import List, DefaultDict


def init_database(database: DefaultDict[str, str], records:List[str]):
    # 각 로그를 순회하여 Enter, Change로 시작하는 로그에 대해서
    # 사용자의 user id에 대한 nickname을 설정한다.
    for record in records:
        if record.startswith('Enter') or record.startswith('Change'):
            command, identifier, nickname = record.split(' ')
            database[identifier] = nickname

def create_messages(database, records):
    # 데이터베이스를 기반으로 로그를 압축한다.
    # Enter와 Leave의 내용은 수정하여 저장하고
    # Change는 무시한다.
    messages = []
    for record in records:
        command, *args = record.split(' ')
        identifier = args[0]
        
        if command == 'Enter':
            message = f'{database[identifier]}님이 들어왔습니다.'
        elif command == 'Leave':
            message = f'{database[identifier]}님이 나갔습니다.'
        else:
            continue
        messages.append(message)
    return messages
            
    
def solution(records: List[str]):
    '''
    Args:
        records: 오픈채팅방의 로그가 담긴 리스트
        * 로그의 종류는 아래와 같다.
        * Enter {uid} {name}
        * Leave {uid}
        * Change {uid} {name}
    Returns:
        List[str]: 오픈채팅방의 로그를 압축한 리스트
        * 사용자의 최종 변경된 이름으로 로그를 수정하여 압축한다.
    '''
    database = defaultdict(str)
    init_database(database, records)
    answer = create_messages(database, records)
    
    return answer