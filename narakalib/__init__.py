import requests
import json
import time


# 获取角色id
def get_role_id(player_name, cookies):
    url = 'https://api.xiaoheihe.cn/game/yjwj/search'
    params = {
        'q': player_name
    }
    r = requests.post(url, params=params, cookies=cookies)
    user_list = json.loads(r.text)['result']['user_list']
    if len(user_list) == 0:
        return 0
    else:
        count = 1
        for i in user_list:
            print('%s.角色名: %s 段位: %s 分数: %s 游戏场次: %s' % (
                str(count).zfill(2), i['role_name'], i['level'], i['rank_score'], i['game_count']))
            count += 1
        print('-' * 40)
        if len(user_list) == 1:
            s = 0
        else:
            s = int(input('请输入角色序号:')) - 1
        player_id_out = user_list[s]['role_id']
        print('角色名: %s\n角色id: %s' % (user_list[s]['role_name'], user_list[s]['role_id']))
        return player_id_out


# 更新信息
def update(player_id_in, cookies):
    url = 'https://api.xiaoheihe.cn/game/yjwj/update'
    params = {
        'server': '163',
        'role_id': player_id_in
    }
    r = requests.post(url, params=params, cookies=cookies)
    result = json.loads(r.text)
    print('角色数据' + result['result']['btn_desc'])


# 获取结果(角色id,游戏模式,赛季)
def get_result(player_id_in, mode_in, season_in, cookies):
    url = 'https://api.xiaoheihe.cn/game/yjwj/home/data'
    params = {
        'battle_tid': mode_in,
        'season': season_in,
        'server': '163',
        'role_id': player_id_in,
        'heybox_id': '1057809'
    }
    r = requests.post(url, params=params, cookies=cookies)
    result = json.loads(r.text)
    return result


# 解析总览(结果)
def analysis_overview(r):
    mode = {
        '4': '天人之战-单排',
        '5': '天人之战-三排',
        '6': '快速匹配-单排',
        '7': '快速匹配-三排',
        '5000000': '天选之人-单排',
        '5000001': '天选之人-三排',
        '5000010': '无尽试炼'
    }
    print('游戏模式: %s\n排位分: %s\n段位: %s' % (
        mode[r['result']['battle_tid']], r['result']['player_info']['rating'], r['result']['player_info']['level']))
    overview = r['result']['overview']
    for i in overview:
        print('%s: %s' % (i['desc'], i['value']))


# 分析最近对局(结果)
def analysis_recent_matches(r):
    mode = {
        '4': '天人之战-单排',
        '5': '天人之战-三排',
        '6': '快速匹配-单排',
        '7': '快速匹配-三排',
        '5000000': '天选之人-单排',
        '5000001': '天选之人-三排',
        '5000010': '无尽试炼'
    }
    heroes = {
        '1000001': '土御门胡桃',
        '1000003': '宁红夜',
        '1000004': '迦南',
        '1000005': '特木尔',
        '1000006': '季沧海',
        '1000007': '天海',
        '1000009': '妖刀姬',
        '1000010': '崔三娘',
        '1000011': '岳山',
        '1000013': '无尘',
        '1000015': '顾清寒',
        '1000016': '武田信忠',
        '1000017': '殷紫萍'
    }
    matches = r['result']['matches']
    count = 1
    for i in matches:
        # 判断英雄名称是否在heroes字典中，如果是，返回英雄名称，如果不是，返回英雄id
        if i['hero_id'] in heroes:
            hero = heroes[i['hero_id']]
        else:
            hero = i['hero_id']
        print('%s.游戏模式: %s 击杀数: %s 总伤害量: %s 评级: %s 使用英雄: %s 排名: %s 排位分: %s 分差: %s 时间: %s 总人数: %s' % (
            str(count).zfill(2), mode[i['battle_tid']], i['kill_times'], i['damage'], i['grade'],
            hero, i['rank'],
            i['rating'],
            i['rating_delta'],
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['time'])), i['total_users_count']))
        count += 1


seasons = {
    '全部': 'pre-01',
    '先行者赛季': 'pre',
    '浪潮赛季': 'wave',
    '破阵赛季': 'break',
    '凌霄赛季': 'sky',
    '无妄赛季': 'unforeseen',
    '辉光赛季': 'glory'
}
