# Python 라이브러리 활용하기

### 데이터 수집 방법
#### Parsing
* 어떤 데이터를 원하는 형태의 데이터로 가공하는(변환하는) 것
* Parser = parsing을 하는 processor

#### Crawling
* 웹 페이지의 링크(url)를 순회하며 웹 페이지의 정보를 얻고 분류하는 것
* 스파이더링(Spidering)이라고 부르기도 함
* robots.txt : 가져와야 할 페이지가 많은 경우, 검색 속도를 높이기 위해 robot이라는 프로그램을 사용하는데 개인정보가 포함된 경우 무분별한 크롤링을 막기 위해 robots.txt을 작성하여 크롤링 허가 여부를 설정. https://naver.com을 방문할 경우 https://naver.com/robots.txt를 참고하여 허가된 내용을 크롤링.

#### Scraping
* = 데이터를 수집하는 일련의 모든 과정
* 웹 페이지의 구조를 분석하여 원하는 특정 데이터를 추출
* 즉, 스크레이핑 과정 중 크롤링이 포함, 크롤링해서 얻은 정보를 통해 특정 데이터 추출

### 파일 형식
#### JSON (JavaScript Object Notation)
* 데이터 교환 포맷
* JavaScript에서 객체를 만들 때 표현하는 사용식을 의미
* 사람과 기계 모두 이해하기 쉽고 용량이 작음
* key-value 형태 or array, list 형태

#### XML (eXtensible Markup Language)
* html과 비슷한 마크업 언어
* 데이터를 보여주기보다는 전송, 배포할 목적으로 사용
* 사용자가 태그명을 임의로 만들어서 사용

- - -
##### Same-Origin-Policy
* 문제 발생 : Javascript로 외부 서버에 ajax 요청을 하는 경우 에러 발생
* 이유 : Same-Origin-Policy 보안 규칙때문
* 자바스크립트(XMLHttpRequest)로 다른 웹페이지에 접근할 때 같은 페이지에서만 접근 가능 (= 프로토콜, 호스트명, 포트번호가 같아야 함)

##### CORS (Cross-Origin Resource Sharing)
* 서버와 클라이언트가 정해진 header를 이용해 서로 응답, 요청에을 반응할 수 있음.
* 외부에서 ajax 요청 가능해짐.

- - -
* JSON.parse() : string객체를 json 객체로
* JSON.stringify() : json객체를 string객체로
