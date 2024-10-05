from random import Random
from json_util.json_io import json_file_to_dict, dict_to_json_file
from time import time

#최초 승리, 패배, 무승부 확률
initial_win_probability = 5 / 12
initial_defeat_probability = 5 / 12
initial_draw_probability = 1 / 6

"""
주사위 게임을 진행하는 메소드

reply
{
    'result' : 'win' or 'defeat' or 'draw',
    'player' : 플레이어의 주사위 눈,
    'computer' : 컴퓨터의 주사위 눈,
    'point' : 플레이어의 포인트,
    'level' : 플레이어의 레벨
}
"""
def play(user_id : str) -> dict:
    random = Random(time())
    user_info_dict = json_file_to_dict()

    # user_id를 통해, 사용자 정보를 가져온다.
    player_info = user_info_dict[user_id]
    player_level = player_info['level']
    player_point = player_info['point']
    result = dict({'result' : 'win'})

    """
    사용자의 레벨에 따라, 승리 확률을 조정한다.
    """
    ###################작성필요########################
    # 힌트 : 레벨에 따라, 승리 확률을 조정 해야한다.
    #        승리할 확률이 증가한 만큼, 패배 및 무승부 확률도 조정이 필요하다.
    ##################################################
    win_probability = initial_win_probability + (player_level -1)*0.01
    defeat_probability = initial_defeat_probability -(player_level -1)*0.005
    draw_probability = initial_draw_probability -(player_level -1)*0.005

    # 승리 여부를 우선 결정한다.
    win_defeat_draw = random.choices(['win', 'defeat', 'draw'], [win_probability, defeat_probability, draw_probability])[0]

    ###################작성필요########################
    # 힌트 : random.choices는 각 확률에 맞게, 'win', 'defeat', 'draw' 중 하나가 선택된다.
    #        승리, 패배, 무승부에 맞게 인위적으로 주사위의 눈을 선택해준다.
    ##################################################
    player_roll = 0
    computer_roll = 0
    if win_defeat_draw == 'win':
        while player_roll <= computer_roll:
            player_roll = random.randint(2,6)
            computer_roll = random.randint(1,player_roll-1)
    elif win_defeat_draw == 'defeat':
        while player_roll >= computer_roll:
            player_roll = random.randint(1, 5)
            computer_roll = random.randint(player_roll+1,6) 
            result.update({'result' : 'defeat'})
    elif win_defeat_draw == 'draw':
            player_roll = random.randint(1,6)
            computer_roll = player_roll
            result.update({'result' : 'draw'})     
    
    ###################작성필요########################
    # 힌트 : 승리 시, 플레이어의 포인트 및 레벨 조정이 필요하다.
    #        그 후, result 및 기존 user_info_dict에 갱신해준다.
    ##################################################
    if win_defeat_draw == 'win':
         player_point +=10
    if player_level < 25:
         if player_point %100 == 0:
              player_level +=1

    player_info.update({'point' : player_point, 'level' : player_level})
    user_info_dict[user_id].update(player_info)
    result.update({'player' : player_roll, 'computer' : computer_roll, 'point' : player_point, 'level' : player_level})

    # 100000번의 시뮬레이션을 통해, 이론적 확률과 통계적 확률을 비교해준다.
    test_probability([win_probability, defeat_probability, draw_probability])
    
    dict_to_json_file(user_info_dict)
    return result

def test_probability(probabilities : list):
    random = Random(time())
    num_of_test = 100000
    count : dict = {'win' : 0, 'defeat' : 0, 'draw' : 0}
    for _ in range(num_of_test):
        choice_one = random.choices(['win', 'defeat', 'draw'], probabilities)
        count[choice_one[0]] += 1
    
    print(f'이론적 승리 확률 : {round(probabilities[0], 3)} ' + f'통계적 승리 확률 : {count['win'] / 100000}')
    print(f'이론적 패배 확률 : {round(probabilities[1], 3)} ' + f'통계적 패배 확률 : {count['defeat'] / 100000}')
    print(f'이론적 무승부 확률 : {round(probabilities[2], 3)} ' + f'통계적 무승부 확률 : {count['draw'] / 100000}')