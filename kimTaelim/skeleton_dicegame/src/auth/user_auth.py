from json_util.json_io import dict_to_json_file, json_file_to_dict

"""
회원가입을 수행하는 메소드

new_user_info 
{
    'id' : 아이디,
    'password' : 비밀번호
}

reply
{
    'success' : True or False,
    'id' : 아이디,
    'level' : 레벨,
    'point' : 포인트,
    'rank' : 랭크
}
"""
def register(new_user_info : dict) -> dict:
    # 사용자 정보를 불러온다.
    user_info_dict = json_file_to_dict()
    new_user_id = new_user_info['id']
    result_dict : dict = {'success' : True, 'id' : new_user_id}

    ###################작성필요########################
    # 힌트 : 중복 아이디가 존재할 경우, 'success' : False로 설정해야 한다.
    #        update 메소드를 활용하면, 기존에 존재하는 값은 덮어쓰기, 존재하지 않는 값은 추가할 수 있다.
    #        ex) user_info_dict = {'asd123' : {'password' : '1234', 'level' : 1, 'point' : 0, 'rank' : 0}}
    #
    #            user_info_dict['asd123'].update({'level' : 2, 'point' : 100, 'rank' : 1})
    #
    #            user_info_dict -> {'asd123' : {'password' : '1234', 'level' : 2, 'point' : 100, 'rank' : 1}}
    ##################################################
    if new_user_id in user_info_dict:
        result_dict.update({'success' : False})

    else:
        user_info_dict[new_user_id] = new_user_info
        new_user_game_info = {'point' : 0, 'level' : 1, 'rank' : 1}
        user_info_dict[new_user_id].update(new_user_game_info)
        result_dict.update(new_user_game_info)

    dict_to_json_file(user_info_dict)
    return result_dict

"""
로그인을 수행하는 메소드

new_user_info 
{
    'id' : 아이디,
    'password' : 비밀번호
}

reply
{
    'success' : True or False,
    'id' : 아이디,
    'level' : 레벨,
    'point' : 포인트,
    'rank' : 랭크
}
"""
def login(new_user_info : dict) -> dict:
    user_info_dict = json_file_to_dict()
    new_user_id = new_user_info['id']
    new_user_passwd = new_user_info['password']
    result_dict :dict = {'success' : False, 'id' : new_user_id}

    ###################작성필요########################
    # 힌트 : 아이디가 존재하고, 비밀번호가 일치할 경우, 'success' : True로 설정해야 하고,
    #        추가로, 'level', 'point', 'rank'를 설정해야 한다.
    #        아이디가 존재하지 않거나, 비밀번호가 일치하지 않을 경우에는, 따로 설정할 필요가 없다.
    ##################################################
    if new_user_id in user_info_dict:
        if new_user_passwd == user_info_dict[new_user_id]['password']:
            result_dict.update({'success' : True, 'point' : user_info_dict[new_user_id]['point'], 'level' : user_info_dict[new_user_id]['level'], 'rank' : user_info_dict[new_user_id]['rank']})
        



    return result_dict