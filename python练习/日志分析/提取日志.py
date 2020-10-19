import datetime
import re
from pathlib import Path
test = """123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
    "GET /o2o/media.html?menu=3 HTTP/1.1" 200 8642 "-" \
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"""""
# def makekey(line:str , CHARS = set(""" []"'""")):
#     start = 0
#     length = len(test)
#     flag = False
#     for i, c in enumerate(test):
#         if c in CHARS:
#             if c == '[':
#                 start = i + 1
#                 flag = True
#             elif c == ']':
#                 flag = False
#             if flag: continue
#
#             if start == i:
#                 start = i + 1
#                 continue
#             yield test[start:i]
#             start = i + 1
#     else:
#         if start < length:
#             yield test[start:]
#

pattern = '(?P<remote>[\d].{7,15}) \S+ - \[(?P<datetime>[^\[\]]+)\] \
"(?P<method>[^" ]+) (?P<url>[^" ]+) (?P<protocol>[^" ]+)" \
(?P<status>\d+) (?P<size>\d+) \S+ "(?P<useragent>[^"]*)" '
#找不到上面两行错误在哪里
regex = re.compile(pattern)

#names = ('remote', '', '', 'datetime', 'request', 'status', 'size', '', 'useragent')
# ops = (None, None, None,
#        lambda dstr:datetime.datetime.strftime(dstr, "%d%b%Y:%H:%M:%s %z"),
#        lambda request: dict(zip(['method', 'url',  'protocol'], request.split())),
#        int, int, None, None
#        )
ops = {
    'datetime': lambda dstr:datetime.datetime.strptime(dstr, "%d/%b/%Y:%H:%M:%S %z"),
    'status': int, 'size': int
}
def extract(test:str):
    matcher = regex.match(test)
    if matcher:
        return {k: ops.get(k, lambda x: x)(v) for k, v in matcher.groupdict().items()}
#   else:
#       return line
print(extract(test))

def loadfile(filename:str):
    with open(filename) as f:
        for line in f:
            fields = extract(line)
            if isinstance(fields, (dict,)):
                yield fields
            else:
                print('NO match. {}.format{fields}')



def load(*paths,encoding='utf-8',ext=('*.log',)):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for e in ext:
                logs = path.glob(e) #匹配所有符合条件的文件，并将其以列表的形式返回
                #print(list(logs),'~~~~~~')
                for log in logs:
                    print(log)
                    with log.open(encoding=encoding) as f:
                        for line in f:
                            print(line)
        elif path.is_file():
            pass





