import re
#
# username = input("请输入用户名")
# if re.match(r"^\w{6,15}$",username):
#     passdword = input("请输入密码")
#     if re.match(r"^(?=.+[a-zA-Z])(?=.+[0-9])(?=.+[_])[a-z0-9A-Z_]{6,20}$", passdword):
#         passdword2 = input("请再次输入密码")
#         if passdword2 == passdword:
#             mail = input("请输入邮箱")
#             if re.match(r"^\w{6,20}@(163|126|189)\.com$",mail):
#                 print("注册成功")
#             else:
#                 print("邮箱格式错误")
#         else:
#             print("两次输入的密码不一样")
#     else:
#         print("密码格式错误")
# else:
#     print("用户名格式错误")


# str00 = '''资源内容：
#         腾讯好莱坞账号2737568171腾讯好莱坞密码eeee65292
#         腾讯好莱坞账号3310483024腾讯好莱坞密码eeee62332
#         腾讯好莱坞账号2158567715腾讯好莱坞密码pppp95942
#         腾讯好莱坞账号3432147819腾讯好莱坞密码pppp24336
#         腾讯好莱坞账号2180196140腾讯好莱坞密码pppp68629
#         腾讯好莱坞账号2135681497腾讯好莱坞密码pppp82627
#         腾讯好莱坞账号2128840963腾讯好莱坞密码cfkgo91
# '''
#
#
# listTest2 = re.findall(r'(密码.*)',str00)
# print(listTest2)



# str01 = "hello world ha ha"
# newStr = re.split(" ",str01)
# print(newStr)




str03 = r"话说天下大势，上海韬沃网络科技有限公司15216793676分久必合，合久必分。上海蓝茂软件技术有限公司17730015099周末七国分争，并入于秦。北京讯飞工作室17055613706及秦灭之后，楚、汉分争，又并入于汉。上海市授权码有限公司13094757747汉朝自高祖斩白蛇而起义，上海因子软件有限公司18148969698一统天下，上海川颐智能科技有限公司15921638003后来光武中兴，传至献帝，遂分为三国。上海米飞网络科技有限公司15625252891推其致乱之由，殆始于桓、灵二帝。协购（上海）电子商务有限公司13524231172桓帝禁锢善类，崇信宦官。上海佳碟计算机科技有限公司13800000000及桓帝崩，灵帝即位，大将军窦武、太傅陈蕃共相辅佐。时有宦官曹节等弄权，窦武、陈蕃谋诛之，机事不密，反为所害，中涓自此愈横。"
#
#
# phoneNum = re.findall(r'\d+',str03)
# print(phoneNum)


str04 = r'''
        ·人民网-图片http://www.people.com.cn/GB/tupian/
        ·中国新闻图片网http://www.cnsphoto.com/
        ·全景图片网http://www.quanjing.com/
        ·八目妖http://www.haha168.com/
        ·美图http://www.6to23.com/pic/
        ·新华网-图片频道http://www.xinhuanet.com/photo/
        ·国内新闻精彩图片集http://news.sina.com.cn/photo/c/index.shtml
        ·中国花卉图片网http://www.fpcn.net/
        ·超景图片库http://www.gettyimages.cn/
        ·精美扫图http://www.enet.com.cn/eschool/includes/zhuanti/cg/index.shtml
'''
urlStr = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str04)
print(urlStr)



