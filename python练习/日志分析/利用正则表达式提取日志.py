import re

test = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
     "GET /o2o/media.html?menu=3 HTTP/1.1" 200 8642 \
     "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"'''

pattern = '(?P<remote>[\d].{7,15}) \S+ - \[(?P<datetime>[^\[\]]+)\] \
"(?P<method>[^" ]+) (?P<url>[^" ]+) (?P<protocol>[^" ]+)" \
(?P<status>\d+) (?P<size>\d+) \S+ "(?P<useragent>[^"]*)"'

regex = re.compile(pattern)
matcher = regex.match(test)
if matcher:
    print(matcher)
    print(test[matcher.start():matcher.end()])
    print(matcher.groups())
    print(matcher.groupdict())