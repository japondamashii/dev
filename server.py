import web
import json
import datetime
import os
import subprocess

urls = ('/', 'hooks' ,'/resourcepack/(.*)','files')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = json.loads(web.data())
        datime = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f')
        datime_log = datetime.datetime.now().strftime('%Y/%m/%d-%H:%M:%S')
        #print("")
        #print('DATA RECEIVED:')
        #print(data["repository"]["html_url"])
        #print("")
        print(f"[{datime_log}] webhookを受信しました")
        try:
            if data["repository"]["html_url"] == "https://github.com/ErmdeirRPG/dev" and data["ref"] == "refs/heads/master":
                print(f"[{datime_log}] New commit")
                subprocess.Popen(["git","pull"],shell=True)
        except Exception as e:
            print(e)
        #with open(f"./log/{datime}.json","a") as f:
        #    f.write(json.dumps(data,indent=2))
        return 'OK'

#class files:
#    def GET(self, name):
#        raise web.seeother(f"/static/{name}")

if __name__ == '__main__':
    print("webhookサーバーを起動中...")
    app.run()
