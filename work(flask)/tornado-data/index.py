import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define, options
import os
from pymongo import MongoClient, ASCENDING, DESCENDING

col_local = MongoClient("106.14.147.212")['jd_entity_category']['posed_job_skill_font_end']

define("port", 3717 )


class Index(tornado.web.RequestHandler):
    def get(self):
        infos = col_local.find({"isTag": 0}).sort("ID", ASCENDING)
        info = infos[0]
        tags = info["tags"]
        infoWords = ""
        for words in tags:
            infoWords += words["word"]
        tagWord = []
        for myTag in tags:
            if myTag["tag"] == str(1):
                tagWord.append(myTag["word"])
        self.render('user/index.html', info=info, tags=tags, infoWords=infoWords, tagWord=tagWord,infoid=info["ID"])


class InfoHandler(tornado.web.RequestHandler):
    def post(self):

        print('111')
        infoid = self.get_argument("infoid")
        #用户对以前标注过得信息重新处理
        last_info=col_local.find_one({'ID':int(infoid)})
        #判断这条信息用户之前是否标注过
        if int(last_info["isTag"]) == 1:
            last_Tag=last_info["tags"]
            for last_Tagcolor in last_Tag:
                last_Tagcolor["color"]=0

        tag_info = self.get_argument("ret")
        infos = tag_info.split('~')

        tag_greens = infos[1]
        tag_blues = infos[2]
        if tag_greens != "tag_green=''" and tag_blues != "tag_blue=''":
            useTagGreen = tag_greens[11:-1]

            use_green = useTagGreen.split('%')
            for i in range(len(use_green)):
                use_green[i] = use_green[i].replace(' ', '')
            print(use_green)

            useTagBlue = tag_blues[10:-1]

            use_blue = useTagBlue.split('%')
            for i in range(len(use_blue)):
                use_blue[i] = use_blue[i].replace(' ', '')
            print(use_blue)

            info = col_local.find_one({"ID": int(infoid)})
            tags = info["tags"]

            for words in tags:
                if words["word"] in use_blue:
                    print('blue-%s' % (words["word"]))
                    words["color"] = 2
                elif words["word"] in use_green:
                    print('green-%s' % (words["word"]))
                    words["color"] = 1
            info["isTag"] = 1
            col_local.save(info)
        else:
            col_local.update({"ID":int(infoid)}, {"$set": {"isTag": 1}})

        next_infoid = int(infoid) + 1

        while True:
            next_info = col_local.find_one({'ID': next_infoid})
            if int(next_info["isTag"]) == 1:
                next_infoid += 1
            else:
                break

        next_info = col_local.find_one({'ID': next_infoid})
        tags = next_info["tags"]
        infoWords = ""
        for words in tags:
            infoWords += words["word"]
        tagWord = []
        for myTag in tags:
            if myTag["tag"] == str(1):
                tagWord.append(myTag["word"])

        self.render('user/index.html', tags=tags, infoWords=infoWords, tagWord=tagWord,infoid=next_infoid)

class Next(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        infoid = self.get_argument("infoid")
        nextInfoId = int(infoid) + 1
        info = col_local.find_one({"ID": nextInfoId})

        tags = info["tags"]
        infoWords = ""
        for words in tags:
            infoWords += words["word"]
        self.render('user/index.html', tags=tags, info=info, infoWords=infoWords,infoid=nextInfoId)

class Last(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        infoid = self.get_argument("infoid")
        lastInfoId = int(infoid) - 1
        if lastInfoId<1:
            lastInfoId = 1
        # while True:
        #     info = col_local.find_one({"ID": lastInfoId})
        #     if int(info['isTag']) == 1:
        #         lastInfoId -=1
        #         if lastInfoId <= 1:
        #             lastInfoId = 1
        #             break
        #     else:
        #         break
        info = col_local.find_one({"ID": lastInfoId})
        tags = info["tags"]
        infoWords = ""
        for words in tags:
            infoWords += words["word"]

        self.render('user/index.html', tags=tags, info=info, infoWords=infoWords,infoid=lastInfoId)

    # class UserRegister(tornado.web.RequestHandler):
    #     def get(self):
    #         self.render('user/register.html',list=list)
    #
    # class UserRegisterHandler(tornado.web.RequestHandler):
    #     def post(self):
    #         name=self.get_argument("name")
    #         pwd=self.get_argument("password")
    #         if name != "" and pwd != "":
    #             collections.insert_one({"name":name,"password":pwd})
    #
    #         self.render('user/login.html', list=list)
    #
    # class UserLogin(tornado.web.RequestHandler):
    #     def get(self):
    #         self.render('user/login.html',list=list)
    #
    # class UserLoginHandler(tornado.web.RequestHandler):
    #     def post(self):
    #         name=self.get_argument("username")
    #         pwd=self.get_argument("pwd")
    #
    #         print(name)
    #         print(pwd)
    #         info=collections.find_one({"name":name,"password":pwd})
    #         if info != None:
    #
    #             self.render('user/index.html', list=list)
    #         else:
    #             self.redirect('/login')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    print(options.port)

    app = tornado.web.Application(handlers=[
        (r'/', Index),
        (r'/handler', InfoHandler),
        (r'/next', Next),
        (r'/last', Last),
    ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        debug=True
    )

    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
