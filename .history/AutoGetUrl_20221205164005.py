import GetTargetUrls
import pandas as pd
import time

Cookie = 'appmsglist_action_3909106468=card; appmsglist_action_3888765809=card; appmsglist_action_3939421254=card; appmsglist_action_3867712421=card; appmsglist_action_3870777659=card; appmsglist_action_3940423674=card; appmsglist_action_3873514537=card; appmsglist_action_3230838785=card; ua_id=qgQSOwwPYk6QNmhLAAAAADFui5MyU1nHfqiejgcJL_M=; mm_lang=zh_CN; ptui_loginuin=1306994173; RK=70epH0ERNU; ptcz=f2443493d205a388bd0061df132f40252aad3fc2d9b223a9f36a961fecfe1b45; pgv_pvid=4490214787; o_cookie=1306994173; pac_uid=1_1306994173; noticeLoginFlag=1; remember_acct=lisiyuansven%40foxmail.com; iip=0; fqm_pvqid=938a7635-027c-4ab1-adf2-8e70fbf73adb; _clck=3909106468|1|f75|0; rewardsn=; wxtokenkey=777; uuid=c709f3567e680b745cc5e7d91371f5ca; rand_info=CAESIOKY2xxQeA50ZSfZeVmrgWJ+yV0Uc2jKCQK8Kh0+WWd+; slave_bizuin=3888765809; data_bizuin=3888765809; bizuin=3888765809; data_ticket=CI1FICv08x9LZ77tUZWZu/lEz7N7toqpYqxvVBG6LMS4Hr52DYZ55sixXTIgFg0o; slave_sid=Yml0YUdqX05RQ3NVNjBoeVVqTURPZF83X2l1aVl5aWtKVmVTWHYzaTAzSXJGRElxYUZFYnRYODlEckRsdko0V3E5Y045dEF1d2E2VE5tNHJmdkVoWk5xclFVUkRYT2pCZHMxckZ1ZEVaZXNzX1F5X2QzU3ZWbmJpcXZXcHZueXRscGFZQVpZV004R1pueWFV; slave_user=gh_6cae14a1a432; xid=ea3b950e12d9c8588d167ebc818577d9'
token = '1676706391'

lis0 = [
    # '东岳论丛',
    # '读书杂志',
    # '福建社会科学院福建论坛杂志2',que
    # '甘肃社会科学',
    # '广东社会科学',
    # '贵州社会科学',
    # '国外社会科学',
    # '河北学刊',
    # '江海学刊',
    # '江汉论坛',
    # '江淮论坛杂志社',
    # '江苏社会科学',
    # '江西社会科学',
    # '开放时代',
    # '南京社会科学',
    # '内蒙古社会科学',
    # '思想战线（思想战线THINKING）',
    # '探索与争鸣（探索与争鸣杂志）',
    # '天津社会科学',
    # '文化纵横',
    # '文史哲（文史哲杂志）',
    # '新疆社会科学（新疆社会科学杂志社）',
    # '学海（学海杂志）',
    # '学术界（学术界杂志社）',
    # '学术论坛（学术论坛杂志社）',
    # '学术研究'
    ######
    # '广西社会科学（广西社会科学杂志社）',
    # '河南社会科学',
    # '湖北社会科学（湖北社会科学杂志）',
    # '湖南社会科学（湖南省社会科学院）',
    # '兰州学刊',
    # '理论月刊',
    # '社会科学家（社会科学家杂志社）',
    # '天府新论'
    ###疑难杂症部分
    # '开放时代',
    # '探索与争鸣3',
    # '文化纵横3'
    ### C_Plus
    #'广西社会科学',
    #'河南社会科学',
    #'湖北社会科学',
    #'湖南社会科学',
    #'兰州学刊',
    #'理论月刊',
    #'社会科学家',
    #'天府新论',
    #####
    #'探索与争鸣b',
    #'学术月刊b',
    #'云南社会科学b',
    #'中国社会科学201802'
    #'读书杂志'
    #'江淮论坛杂志社',
    #'人民论坛',
    #'学术前沿'
    '文化纵横2021/1-2020/8'

]

lis1 = [
    # 'MzI4MTY1NzQ3MQ==',
    # 'MzA3ODk5NTAzNA==',
    # 'MzI5Mzk3NTEyMw==',
    # 'MzAxNjkyMTQ3MQ==',
    # 'MzkyNTM5NDE5MA==',
    # 'MzIzNDY5MTM4Nw==',
    # 'MzAwNDYzNzAwNw==',
    # 'MzIzOTQ4Nzg4Ng==',
    # 'MzI0NTA2NjIxOQ==',
    # 'MzkzMTE5NzMxMQ==',
    # 'MzkyMDE5MTA4NQ==',
    # 'MzI3OTQxNDQ2Mg==',
    # 'MzIwMDUwNjY3Mg==',
    # 'MzA4Mjg3MTYyMA==',
    # 'MzIzNzcxNjM5Mg==',
    # 'MzAwMzQyMDk2Ng==',
    # 'MzIxNDE2OTYyOA==',
    # 'MzA4MjcxMDEwNQ==',
    # 'MzUzNjg4OTU0NQ==',
    # 'MzA5MjM2NDcwMg==',
    # 'MzAwNzM4MjQ0Mw==',
    # 'MzkxNDE5Mjk1Ng==',
    # 'MzAwNzU3OTQwMw==',
    # 'MzIwOTAyNzcwMQ==',
    # 'MzU0MTY1NDUzNQ==',
    # 'MjM5NzU4NTU4NA=='
    #####
    # 'MzIwNTEwNzUzOQ==',
    # 'MzI4Mjc4MzIzNA==',
    # 'MzI0MDc4ODcxMg==',
    # 'Mzg2MzU2MzI0Nw==',
    # 'Mzg5NjY1NjIxMg==',
    # 'Mzg2NTA0MDE5OQ==',
    # 'MzA5NTkyNzkwMg==',
    # 'MzI0MjEwODA0Ng=='
    ##### 疑难杂症部分
    # 'MzA4Mjg3MTYyMA==',
    # 'MzA4MjcxMDEwNQ==',
    # 'MzA5MjM2NDcwMg=='
    #'MzIwNTEwNzUzOQ==',
    #'MzI4Mjc4MzIzNA==',
    #'MzI0MDc4ODcxMg==',
    #'Mzg2MzU2MzI0Nw==',
    #'Mzg5NjY1NjIxMg==',
    #'Mzg2NTA0MDE5OQ==',
    #'MzA5NTkyNzkwMg==',
    #'MzI0MjEwODA0Ng=='
    ###
    #'MzA4MjcxMDEwNQ==',
    #'MzA5NTk5ODQwOQ==',
    #'MzU3NDQzNTY4Ng==',
    #'MzA4NDUwMjMxNA=='
    #'MzA3ODk5NTAzNA=='
    #'MzkyMDE5MTA4NQ==',
    #'MzU1ODgzOTcwMQ==',
    #'MjM5NzA4MDIxNw=='
    'MzA5MjM2NDcwMg=='

]

lis_startPpage = [
    #278,
    #157,
    #200,
    #154
    #0,
    #0,
    184
]

lis_post_count = [
    #138,
    #784,
    #994,
    #666
    #0,
    #0,
    233
]
 
columns = ['account_name', 'fakeid', 'start_page', 'post_count']

todf = [lis0, lis1, lis_startPpage, lis_post_count]
df0 = pd.DataFrame(todf)
df0 = df0.T
df0.columns = columns
print(df0)

for index, row in df0.iterrows():
    print(row)
    fakeid = row['fakeid']
    account_name = row['account_name']
    sleep_time = 30
    start_page = row['start_page']
    post_count = row['post_count']

    GetTargetUrls.GetTargetUrls(Cookie, token, fakeid, account_name=account_name, sleep_time=sleep_time, start_page=start_page, post_count=post_count)
