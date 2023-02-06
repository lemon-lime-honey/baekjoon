def solution(id_pw, db):
    for element in db:
        if element[0] == id_pw[0]:
            if element[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
            break
    else:
        return "fail"