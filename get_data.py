# -*- cording:utf-8 -*-

import csv
import pprint
import requests
import datetime


def get_registered(url, word, **kwargs):
    """
    登録されているか確認
    :param url:
    :param word:
    """
    res = requests.get(url, params=kwargs)
    result = [s[word] for s in res.json()]
    if word == 'id':
        if len(result) > 1:
            return result
        else:
            return result
    return result


def requests_post(url, **data):
    res = requests.post(url, json=data)
    if res.status_code == 201:
        return print(str(res.status_code))
    else:
        return print('error:' + str(res.status_code))


def trans_word(word, **kwargs):
    """
    :param word:
    """
    trans = str.maketrans(kwargs)
    result = word.translate(trans)
    return result


def get_id(**kwargs):
    """

    """
    url = kwargs['url']
    word = kwargs['word']
    add_params = kwargs['add_params']
    params = kwargs['params']
    result_id = get_registered(url, 'id', **params)
    if len(result_id) == 0:
        if word != '' or add_params != '':
            params[word] = add_params
            requests_post(url, **params)
        else:
            requests_post(url, **params)
        result_id = get_registered(url, 'id', **params)
    return result_id[0]


def get_service_and_team_id(url, team_code, service, status):
    team_url = url + 'teamInfo/team/'
    service_url = url + 'phonePlat/service/'
    result = {}
    if team_code != '':
        if team_code.isdecimal():
            get_team_id = get_registered(team_url, 'id', **{'code': team_code})
        else:
            get_team_id = get_registered(team_url, 'id', **{'name': team_code})
        team_id = get_team_id[0]
        result['team_id'] = team_id
        if service != '':
            service_number = service.split(' ')[0]
            service_params = {
                'team': team_id,
                'holiday': False,
                'always': False,
                'start_date': None,
                'remind': None,
                'channel_count': 0
            }
            get_service_id = {
                'url': service_url,
                'word': 'status',
                'add_params': status,
                'params': service_params
            }
            if service_number.isdecimal():
                service_params['number'] = service_number
                service_params['name'] = '_'.join(service.split(' ')[1:])
                service_params['category'] = 'CSIM'
            else:
                name = '_'.join(service.split(' '))
                service_params['name'] = name
                service_params['category'] = 'その他'
            service_id = get_id(**get_service_id)
            result['service_id'] = service_id
        else:
            result['service_id'] = service
    else:
        result['team_id'] = team_code
        result['service_id'] = service
    return result


def get_site(url):
    """
    サイトを取り込み
    """
    site_url = url + 'teamInfo/site/'
    file = r'/temp/01_サイト一覧_一覧表示画面_2021_12_29 11_56_18.Csv'
    with open(file, encoding='utf-8-sig') as f:
        next(csv.reader(f))
        reader = csv.reader(f)
        total = 0
        for r in reader:
            get_name = r[0]
            status = '使用中'
            description = r[2]
            translate = {
                '（': ' ',
                '）': ''
            }
            make_category = trans_word(get_name, **translate).split(' ')
            name = make_category[0]
            if len(make_category) > 1:
                category = make_category[1]
            else:
                category = None
            params = {
                'name': name,
                'category': category
            }
            site_name = get_registered(site_url, 'name', **params)
            if len(site_name) == 0 or name not in site_name:
                data = {
                    'name': name,
                    'category': category,
                    'status': status,
                    'description': description
                }
                requests_post(site_url, **data)
                total += 1
        print('site: ' + str(total))
        print('----------------------')


def get_tenant(url):
    """
    tenant取り込み
    """
    tenant_url = url + 'teamInfo/tenant/'
    site_url = url + 'teamInfo/site/'
    file = r'/temp/02_テナント一覧_一覧表示画面_2021_12_30 15_38_13.Csv'
    with open(file, encoding='utf-8') as f:
        next(csv.reader(f))
        reader = csv.reader(f)
        total = 0
        for r in reader:
            name = r[1]
            get_status = r[2]
            site_name = r[3].split('（')[0]
            description = r[4]
            if get_status == '稼働中':
                status = '使用中'
            elif get_status == '不稼働':
                status = '停止中'
            site_params = {
                'name': site_name,
            }
            site = get_registered(site_url, 'id', **site_params)
            params = {
                'name': name,
                'site': site[0]
            }
            tenant_name = get_registered(tenant_url, 'name', **params)
            if len(tenant_name) == 0 or name not in tenant_name:
                data = {
                    'name': name,
                    'site': site[0],
                    'status': status,
                    'description': description,
                }
                requests_post(tenant_url, **data)
                total += 1
        print('tenant:' + str(total))
        print('----------------------')


def get_team(url):
    """
    チーム取り込み
    :param url:
    """
    tenant_url = url + 'teamInfo/tenant/'
    team_url = url + 'teamInfo/team/'
    dept_url = url + 'teamInfo/dept/'
    file = r'/temp/03_チーム一覧_一覧表示画面_2021_12_30 16_02_26.Csv'
    with open(file, encoding='utf-8') as f:
        next(csv.reader(f))
        reader = csv.reader(f)
        team_total = 0
        dept_total = 0
        for r in reader:
            team_name = r[1].split(' ')
            if len(team_name) > 1:
                code = team_name[0]
                name = '_'.join(team_name[1:])
            else:
                code = None
                name = team_name[0]
            get_status = r[2]
            get_tenant_name = r[3]
            dept_name = r[5]
            dept_code = r[6]
            translate = {
                '(': '',
                ')': ''
            }
            trans_dept_name = trans_word(dept_name, **translate)
            if get_status == '稼働中':
                status = '使用中'
            elif get_status == '不稼働':
                status = '停止中'
            else:
                status = get_status
            if get_tenant_name == '':
                tenant = [None]
            else:
                tenant_params = {
                    'name': get_tenant_name
                }
                tenant = get_registered(tenant_url, 'id', **tenant_params)
            team_params = {
                'name': name,
            }
            team_name = get_registered(team_url, 'name', **team_params)
            if len(team_name) == 0 or name not in team_name:
                team_data = {
                    'name': name,
                    'code': code,
                    'tenant': tenant[0],
                    'status': status,
                    'proportion': False
                }
                requests_post(team_url, **team_data)
                team_total += 1
            team_id = get_registered(team_url, 'id', **team_params)
            dept_params = {
                'team': team_id[0],
                'code': dept_code,
                'name': trans_dept_name
            }
            registered_dept = get_registered(dept_url, 'name', **dept_params)
            if len(registered_dept) == 0 or trans_dept_name not in registered_dept:
                if dept_code != '' or dept_name != '':
                    dept_data = {
                        'name': trans_dept_name,
                        'code': dept_code,
                        'status': '使用中',
                        'aggregate_code': None,
                        'team': team_id[0],
                        'active': True
                    }
                    requests_post(dept_url, **dept_data)
                    dept_total += 1
        print('team:' + str(team_total))
        print('----------------------')
        print('dept' + str(dept_total))
        print('----------------------')


def get_service(url):
    """
    :param url:
    """
    service_url = url + 'phonePlat/service/'
    team_url = url + 'teamInfo/team/'
    service_file = [
        # r'D:\PycharmProjects\pcsy\temp\04_サービス一覧（CSIM）_一覧表示画面_2022_01_07 09_57_02.Csv',
        r'D:\PycharmProjects\pcsy\temp\04_サービス一覧（その他）_一覧表示画面_2022_01_07 09_57_15.Csv'
    ]
    for file in service_file:
        with open(file, encoding='utf-8') as f:
            next(csv.reader(f))
            read = csv.reader(f)
            total = 0
            for i, r in enumerate(read):
                get_name = r[1].split(' ')
                status = r[2]
                get_team_name = r[3].split(' ')
                if 'CSIM' in file:
                    category = 'CSIM'
                    holiday = r[4]
                    always = r[5]
                    get_start_date = r[6]
                    remind = r[7]
                else:
                    category = 'その他'
                    holiday = False
                    always = r[4]
                    get_start_date = r[5]
                    remind = r[6]
                if holiday == '':
                    holiday = False
                if always == '':
                    always = False
                if remind == '':
                    remind = None
                number = ''
                name = '_'.join(get_name)
                if len(get_name) > 1:
                    if get_name[0].isdecimal():
                        number = get_name[0]
                        name = '_'.join(get_name[1:])
                if len(get_team_name) > 1:
                    team_code = get_team_name[0]
                    team_name = '_'.join(get_team_name[1:])
                else:
                    team_code = ''
                    team_name = '_'.join(get_team_name)
                if get_start_date == '':
                    start_date = None
                else:
                    start_date = get_start_date.replace('/', '-')
                team_params = {
                    'code': team_code,
                    'name': team_name,
                }
                team_id = get_registered(team_url, 'id', **team_params)
                service_params = {
                    'name': name,
                    'team': team_id[0]
                }
                service_name = get_registered(service_url, 'name', **service_params)
                if len(service_name) == 0 or name not in service_name:
                    service_data = {
                        'category': category,
                        'number': number,
                        'name': name,
                        'status': status,
                        'team': team_id[0],
                        'holiday': holiday,
                        'always': always,
                        'start_date': start_date,
                        'remind': remind,
                        'channel_count': 0
                    }
                    requests_post(service_url, **service_data)
                    total += 1
                    print(name)
            print('service:' + str(total))
            print('----------------------')


def get_scenario(url):
    """
    :param url:
    """
    file = r'/temp/05_シナリオ一覧_一覧表示画面_2022_01_07 09_57_38.Csv'
    scenario_url = url + 'phonePlat/scenario/'
    
    with open(file, encoding='utf-8') as f:
        next(csv.reader(f))
        read = csv.reader(f)
        total = 0
        for r in read:
            get_name = r[1].split(' ')
            number = get_name[0]
            name = '_'.join(get_name[1:])
            status = r[2]
            service = r[3].split(' ')[0]
            team_code = r[4].split(' ')[0]
            get_result = get_service_and_team_id(url, team_code, service, status)
            service_id = get_result['service_id']
            team_id = get_result['team_id']
            scenario_param = {
                'number': number,
                'name': name,
                'service': service_id,
                'team_param': team_id
            }
            
            scenario_names = get_registered(scenario_url, 'name', **scenario_param)
            if len(scenario_names) == 0 or name not in scenario_names:
                scenario_data = {
                    'number': number,
                    'name': name,
                    'service': service_id,
                    'team': team_id,
                    'status': status,
                }
                requests_post(scenario_url, **scenario_data)
                total += 1
        print('scenario:' + str(total))
        print('---------------------')


def get_access_line(url):
    """
    :param url:
    """
    file = r'/temp/09_アクセス回線一覧_一覧表示画面_2022_01_11 16_58_33.Csv'
    career_url = url + 'line/career/'
    line_category_url = url + 'line/category/'
    parent_number_url = url + 'line/parentNumber/'
    location_url = url + 'teamInfo/location/'
    access_line_url = url + 'phonePlat/accessLine/'
    
    with open(file, encoding='utf-8') as f:
        next(csv.reader(f))
        read = csv.reader(f)
        total = 0
        for r in read:
            parent_number = r[1].split('_')[0]
            status = r[2]
            line_category = r[4]
            career = r[5]
            surplus = r[6]
            allowance = r[7]
            translate = {
                '（': ' ',
                '）': ''
            }
            
            # location
            get_location = trans_word(r[3], **translate).split(' ')
            location_name = get_location[0]
            location_ridge = ''
            if len(get_location) > 1:
                location_ridge = get_location[1]
            location_params = {
                'name': location_name,
                'ridge': location_ridge
            }
            get_location_id = {
                'url': location_url,
                'word': '',
                'add_params': '',
                'params': location_params
            }
            location_id = get_id(**get_location_id)
            # career
            career_params = {
                'name': career
            }
            career_id = get_registered(career_url, 'id', **career_params)[0]
            
            # line_category
            line_category_params = {
                'name': line_category,
                'career': career_id
            }
            get_line_category = {
                'url': line_category_url,
                'word': 'status',
                'add_params': status,
                'params': line_category_params
            }
            line_category_id = get_id(**get_line_category)
            # parent_number
            parent_number_params = {
                'number': parent_number,
                'line_category': line_category_id
            }
            get_parent_number = {
                'url': parent_number_url,
                'word': 'status',
                'add_params': status,
                'params': parent_number_params
            }
            parent_number_id = get_id(**get_parent_number)
            access_params = {
                'location': location_id,
                'parent_number': parent_number_id,
                'line_category': line_category_id,
            }
            registered_access_line = get_registered(access_line_url, 'parent_number', **access_params)
            if len(registered_access_line) == 0 or parent_number_id not in registered_access_line:
                access_params['status'] = status
                access_params['proportion'] = False
                access_params['surplus_count'] = surplus
                access_params['allowance_count'] = allowance
                access_params['threshold_value'] = 0
                requests_post(access_line_url, **access_params)
                total += 1
        print('access_line:' + str(total))
        print('---------------------------')


def get_paying_code(url):
    """
    :param url:
    """
    file = r'/temp/08_課金コード一覧_一覧表示画面_2022_01_12 10_47_54.Csv'
    dept_url = url + 'teamInfo/dept/'
    paying_code_url = url + 'phonePlat/payingCode/'
    
    with open(file, encoding='utf-8') as f:
        next(csv.reader(f))
        read = csv.reader(f)
        total = 0
        for r in read:
            code = r[1]
            status = r[2]
            team_code = r[3].split(' ')[0]
            service = r[4].split(' ')
            target_did = r[6]
            dept_code = r[7].split(' ')[0]
            dept = r[8]
            translate = {
                '(': ' ',
                ')': ''
            }
            dept_name = trans_word(dept, **translate)
            get_result = get_service_and_team_id(url, team_code, service, status)
            team_id = get_result['team_id']
            service_id = get_result['service_id']
            dept_params = {
                'code': dept_code,
                'name': dept_name,
                'team': team_id
            }
            get_dept_id = {
                'url': dept_url,
                'word': '',
                'add_params': '',
                'params': dept_params
            }
            dept_id = get_id(**get_dept_id)
            paying_data = {
                'code': code,
            }
            registered_paying = get_registered(paying_code_url, **paying_data)
            paying_data['service'] = service_id
            if len(registered_paying) == 0:
                paing_data['status'] = status
                paying_data['dept'] = dept_id
                paying_data['target'] = target_did
                paying_data['tems'] = False
                requests_post(paying_code_url, **paying_data)
                total += 1
        print('paying_code:' + str(total))
        print('--------------------------')


def get_incoming_number(url):
    """
    :param url:
    """
    file = r'/temp/07_着信課金番号一覧_一覧表示画面_2022_01_13 11_00_30.Csv'
    incoming_number_url = url + 'phonePlat/incomingNumber/'
    paying_service_url = url + 'phonePlat/payingService/'
    
    with open(file, encoding='utf-8') as f:
        next(csv.reader(f))
        read = csv.reader(f)
        for r in read:
            if int(r[0]) >= 0:
                number = r[1]
                status = r[2]
                holder = r[3]
                paying_service = r[4]
                ch_count = r[6]
                team_code = r[7].split(' ')[0]
                service = r[8]
                did = r[9]
                incoming_number_params = {
                    'number': number,
                    'status': status,
                    'holder': holder,
                    'channel_count': ch_count,
                    'target_did': did,
                    'service': ''
                }
                get_result = get_service_and_team_id(url, team_code, service, status)
                incoming_number_params['service'] = get_result['service_id']
                paying_translate = {
                    '(': ' ',
                    ')': ''
                }
                translate_paying_service = trans_word(paying_service, **paying_translate).split(' ')
                paying_service_params = {}
                if len(translate_paying_service) > 1:
                    paying_service_params['name'] = translate_paying_service[1]
                else:
                    paying_service_params['name'] = translate_paying_service[0]
                if paying_service_params['name'] == '':
                    paying_service_params['name'] = '?'
                get_paying_service_id = {
                    'url': paying_service_url,
                    'word': '',
                    'add_params': '',
                    'params': paying_service_params
                }
                paying_service_id = get_id(**get_paying_service_id)
                incoming_number_params['paying_service'] = paying_service_id
                registered_incoming_number = get_registered(incoming_number_url, 'number', **incoming_number_params)
                if len(registered_incoming_number) == 0:
                    requests_post(incoming_number_url, **incoming_number_params)
    print('----------------------------')


def get_phone_number(url):
    """
    :param url:
    """
    file_list = [
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（asterisk）_一覧表示画面_2022_01_13 14_39_10.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（bcp）_一覧表示画面_2022_01_13 14_42_20.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（csim）_一覧表示画面_2022_01_13 14_38_26.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（fax）_一覧表示画面_2022_01_13 14_41_02.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（inin）_一覧表示画面_2022_01_13 14_42_56.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（later）_一覧表示画面_2022_01_13 14_44_17.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（others）_一覧表示画面_2022_01_13 14_43_34.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（webfax）_一覧表示画面_2022_01_13 14_39_59.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（実回線）_一覧表示画面_2022_01_13 14_41_27.Csv',
        r'D:\PycharmProjects\pcsy\temp\06_電話番号一覧（転送元）_一覧表示画面_2022_01_13 14_41_53.Csv'
    ]
    dept_url = url + 'teamInfo/dept/'
    parent_number_url = url + 'line/parentNumber/'
    phone_number_url = url + 'phonePlat/phoneNumber/'
    system_url = url + 'phonePlat/system/'
    
    for file in file_list:
        if 'asterisk' in file:
            system_name = 'Asterisk'
        elif 'bcp' in file:
            system_name = 'BCP転送用'
        elif 'csim' in file:
            system_name = 'CSIM'
        elif 'fax' in file:
            system_name = 'FAX回線'
        elif 'inin' in file:
            system_name = 'ININ'
        elif 'webfax' in file:
            system_name = 'WebFAX'
        elif '実回線' in file:
            system_name = '実回線'
        elif '転送元' in file:
            system_name = 'システム転送元'
        else:
            system_name = 'その他'
        system_id = get_registered(system_url, 'id', **{'name': system_name})[0]
        with open(file, encoding='utf-8') as f:
            next(csv.reader(f))
            read = csv.reader(f)
            for r in read:
                phone_id = int(r[1])
                if phone_id >= 8188:
                    category = r[0].split('（')[1]
                    number = r[2]
                    status = r[3]
                    team_code = r[6].split(' ')[0]
                    service = r[7]
                    description = r[8]
                    dept_code = r[9].split(' ')[0]
                    dept_name = r[10]
                    parent_numbers = r[12].split('_')
                    get_result = get_service_and_team_id(url, team_code, service, '使用中')
                    team_id = get_result['team_id']
                    service_id = get_result['service_id']
                    translate_category = category.replace('）', '')
                    replace_word = {
                        '(': '',
                        ')': ''
                    }
                    if '単独' in parent_numbers:
                        parent_number = parent_numbers[0] + parent_numbers[1]
                        location_name = parent_nubmers[3]
                    else:
                        parent_number = parent_numbers[0]
                        location_name = parent_numbers[1]
                        location_ridge = None
                    if '（EAST）' in parent_numbers[1]:
                        location = parent_numbers[1].replace('（EAST）', '_EAST').split('_')
                        location_name = location[0]
                        location_ridge = location[1]
                    elif '（WEST）' in parent_numbers[1]:
                        location = parent_numbers[1].replace('（WEST）', '_WEST').split('_')
                        location_name = location[0]
                        location_ridge = location[1]
                    elif '（サテライト）' in parent_numbers[1]:
                        location = parent_numbers[1].replace('（サテライト）', 'サテライト').split('_')
                        location_name = location[0]
                        location_ridge = location[1]
                    if parent_number != '':
                        parent_number_params = {
                            'number': parent_number
                        }
                        get_parent_number_id = {
                            'url': parent_number_url,
                            'word': '',
                            'add_params': '',
                            'params': parent_number_params
                        }
                        parent_number_id = get_id(**get_parent_number_id)
                    else:
                        parent_number_id = ''
                
                if dept_code != '' and dept_name != '':
                    translate_dept_name = trans_word(dept_name, **replace_word)
                    dept_params = {
                        'code': dept_code,
                        'name': translate_dept_name,
                        'team': team_id,
                        'active': True
                    }
                    get_dept_id = {
                        'url': dept_url,
                        'word': '',
                        'add_params': '',
                        'params': dept_params
                    }
                    dept_id = get_id(**get_dept_id)
                else:
                    dept_id = ''
                phone_number_params = {
                    'category': translate_category,
                    'number': number,
                    'status': status,
                    'system': system_id,
                    'service': service_id,
                    'description': description,
                    'parent_number': parent_number_id,
                    'dept': dept_id
                }
                phone_number = get_registered(phone_number_url, 'id', **phone_number_params)
                if len(phone_number) == 0:
                    requests_post(phone_number_url, **phone_number_params)
print('finished.')

if __name__ == '__main__':
    root = 'http://127.0.0.1:8000/api/v1/'
    # get_site(root)
    # get_tenant(root)
    # get_team(root)
    # get_service(root)
    # get_scenario(root)
    # get_access_line(root)
    # get_paying_code(root)
    # get_incoming_number(root)
	# c8f56f4d343bcd87ae7458a0baa16a95a1b2298f19122532f9ae52476c9b0b4fb650400ef6a9cb37201228af8b9b9bb4c93a3ba29eac572516fbc5a48e48949d
    get_phone_number(root)
