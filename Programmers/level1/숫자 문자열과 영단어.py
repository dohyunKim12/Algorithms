def solution(s):
    # num_str = ['zero','one','two','three','four','five','six','seven','eight','night']
    # num_int = [0,1,2,3,4,5,6,7,8,9]
    num_dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    for key, val in num_dic.items():   # num_dic의 key,val하나씩 빼와서 문자열에 존재하는 모든 key들을 val값으로 변경.
        s = s.replace(key,val)

    return int(s)