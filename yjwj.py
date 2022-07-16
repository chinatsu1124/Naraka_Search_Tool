import narakalib as naraka


# 主函数
def main():
    while True:
        name = input('请输入角色名(或exit退出):')
        if name == 'exit':
            break
        else:
            player_id = naraka.get_role_id(name, cookies)
            if player_id == 0:
                print('未搜索到该角色名')
            else:
                naraka.update(player_id, cookies)
                res = naraka.get_result(player_id, '5000001', naraka.seasons['无妄赛季'], cookies)
                while True:
                    func = input('1.查询概况\n2.查询最近战绩\n3.查询其他模式分数\n4.返回上层\n')
                    if func == '1':
                        naraka.analysis_overview(res)
                    elif func == '2':
                        naraka.analysis_recent_matches(res)
                    elif func == '3':
                        while True:
                            modes = {
                                '1': '4',
                                '2': '5',
                                '3': '6',
                                '4': '7',
                                '5': '5000000',
                                '6': '5000001'
                            }
                            f = input('1.天人之战-单排\n2.天人之战-三排\n3.快速匹配-单排\n4.快速匹配-三排\n5.天选之人-单排\n6.天选之人-三排\n7.返回上层\n')
                            if f == '7':
                                break
                            else:
                                res = naraka.get_result(player_id, modes[f], naraka.seasons['无妄赛季'], cookies)
                                naraka.analysis_overview(res)
                    else:
                        break


cookies = {
    'pkey': 'MTYyNTE1MDk1OS40OV8xMDU3ODA5bXduYWNob3Jya29xaG9vdA____',
    'user_pkey': 'MTYyNTE1MDk1OS40OV8xMDU3ODA5bXduYWNob3Jya29xaG9vdA____',
    'user_heybox_id': '1057809'
}
main()
