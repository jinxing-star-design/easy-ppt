import random
import time
from queue import Queue
import threading
import datetime
import re
from pathlib import Path

#test = """123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
#    "GET /o2o/media.html?menu=3 HTTP/1.1" 200 8642 "-" \
#   "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"""""

pattern = '''(?P<remote>[\d].{7,15}) \S+ - \[(?P<datetime>[^\[\]]+)\] \
"(?P<method>[^" ]+) (?P<url>[^" ]+) (?P<protocol>[^" ]+)" \
(?P<status>\d+) (?P<size>\d+) \S+ "(?P<useragent>[^"]*)"'''
regex = re.compile(pattern)

ops = {
    'datetime': lambda dstr:datetime.datetime.strptime(dstr, "%d/%b/%Y:%H:%M:%S %z"),
    'status': int, 'size': int
}
def extract(line:str):
    matcher = regex.match(line)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
#   else:
#       return line
#print(extract(test))


def loadfile(filename:str):
    with open(filename) as f:
        for line in f:
            fields = extract(line)
            if fields:
                yield fields
            else:
                continue


def load(*paths, ext=('*.log',)):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for e in ext:
                logs = path.glob(e) #匹配所有符合条件的文件，并将其以列表的形式返回
                #print(list(logs),'~~~~~~')
                for log in logs:
                    yield from loadfile(str(log.absolute()))
        elif path.is_file():
            loadfile(str(path))

def source(seconds=1):
    while True:
        yield {'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
               'value': random.randint(1, 100)}
        time.sleep(seconds)


def donothing_handler(iterable):
#    return sum(map(lambda item: item['value'], iterable)) / len(iterable)
    return iterable
#窗口函数
def window(q:Queue,handler,width:int, interval:int):
    buf = []
    start = datetime.datetime.strptime('19700101 00:00:01 +0800', '%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('19700101 00:00:01 +0800', '%Y%m%d %H:%M:%S %z')
    delta = datetime.timedelta(seconds=width-interval)
    while True:
        data = q.get()   #阻塞的
        if data:
            buf.append(data)
            current = data['datetime']

        print(current, start)

        if (current - start).total_seconds() > interval:
            ret = handler(buf)
            print('{}'.format(ret))
            start = current

            buf = [x for x in buf if x['datetime'] > current - delta]

#window(s, avg_handler, 10 ,5)

def dispatcher(src):
    handlers = []  #线程对象，但里面其实是不同的handler
    queues = []
    def reg(handler, width, interval):
        q = Queue()
        t = threading.Thread(target=window, args=(q, handler, width, interval))
#在这里用线程调用window函数
        queues.append(q)
        handlers.append(t)

    def run():
        for t in handlers:
            t.start()

        while True:
            data = next(src)
            for q in queues:
                q.put(data)

    return reg, run

#if __name__ == '__main__':
src = load('.')
reg, run = dispatcher(src)
reg(donothing_handler, 10, 5)
reg(donothing_handler, 10, 5)  #创建不同的栈,将avg_handler传给函数reg中的handler，
print(threading.current_thread())
run()

