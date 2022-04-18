# 링크
node.js 관련 링크
https://rateye.tistory.com/637
node.js 강좌
https://wikidocs.net/book/4776  
ext.js
https://wikidocs.net/book/372
브라켓 확장 기능 사용 안 될 때 해결방법
https://takefive.studio/49
node.js 바이너리 설치
https://lucidmaj7.tistory.com/282

# 메모
- 서식문자 %j
=> json object 출력
exports와 module.exports는 동작원리와 사용방식이 다르다.
- var 대신 let을 쓰는 것이 낫다고 한다. 보안상의 이유?
https://velog.io/@bathingape/JavaScript-var-let-const-%EC%B0%A8%EC%9D%B4%EC%A0%90

# 파일 입출력 함수
`readFile` -> 비동기식 파일 읽어들이는 메서드  
`writeFile` -> 비동기식 파일 쓰는 메서드  
`readFileSync` -> 동기식 파일 읽어들이는 메서드  
`readFileSync` -> 동기식 파일 쓰는 메서드 

## URL 구조
http://opentutorials.org;3000/main?id=HTML&page=12
`http` -> 프로토콜
`opentutorials.org` -> 도메인 네임
`3000` -> 포트 번호
`main` -> 경로, 해당 컴퓨터의 어떤 경로에서 파일을 가져올 것인지
`?id=HTML&page=12` -> 쿼리스트링, 웹서버에 전달할 데이터

## CRUD
정보 시스템의 핵심 메커니즘  
Create, Read, Update, Delete  

# 배열
배열.push -> 배열에 항목 추가
배열.length -> 배열의 길이 출력
배열[i].xx -> 인덱스를 이용한 배열 참조

# 클로저(closure)
실행 컨텍스트
https://poiemaweb.com/js-execution-context
클로저
https://poiemaweb.com/js-closure

## vscode에서 node.js 메소드 사용 시, 취소선이 나타는 이유
https://okky.kr/article/1153356
deprecated 되서 취소선이 나타난다고 한다.  
url.parse 함수의 deprecated 설명
```
function parse(urlString: string): url.UrlWithStringQuery (+3 overloads)
The url.parse() method takes a URL string, parses it, and returns a URL object.

A TypeError is thrown if urlString is not a string.

A URIError is thrown if the auth property is present but cannot be decoded.

Use of the legacy url.parse() method is discouraged. Users should use the WHATWG URL API. Because the url.parse() method uses a lenient, non-standard algorithm for parsing URL strings, security issues can be introduced. Specifically, issues with host name spoofing and incorrect handling of usernames and passwords have been identified.

@since — v0.1.25

@deprecated — Legacy: Use the WHATWG URL API instead.

@param urlString — The URL string to parse.

@param parseQueryString
If true, the query property will always be set to an object returned by the querystring module's parse() method. If false, the query property on the returned URL object will be an unparsed, undecoded string.

@param slashesDenoteHost
If true, the first token after the literal string // and preceding the next / will be interpreted as the host. For instance, given //foo/bar, the result would be {host: 'foo', pathname: '/bar'} rather than {pathname: '//foo/bar'}.

'url.parse'의 시그니처 '(urlString: string): UrlWithStringQuery'은(는) 사용되지 않습니다.ts(6387)
url.d.ts(63, 8): 선언이 여기에 사용되지 않음으로 표시되었습니다.
빠른 수정을 사용할 수 없음
```