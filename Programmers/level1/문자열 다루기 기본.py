def solution(s):
    length = len(s)
    try: int(s)
    except: return False
    return True if length == 4 or length == 6 else False