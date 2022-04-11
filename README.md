

### 1. 파이썬 가상환경 세팅 (virtualenv)

해당 프로젝트 디렉토리로 이동 후에

```shell
virtualenv venv
```

그러면 터미널에서 앞에 `(venv)` 가 붙여져 있는 것을 확인할 수 있다.
이러면 현재 가상 환경이다.

<br>

참고 : https://jaemunbro.medium.com/python-virtualenv-venv-%EC%84%A4%EC%A0%95-aaf0e7c2d24e


<br><br>

### 2. 라이브러리 설치

```shell
pip install
```

프로젝트에 필요한 라이브러리 설치(가상환경 사용하면 좋음)
해당 명령어는 requirements.txt 에 기재된 의존성 설치하는 명령어다.


<br><br>

### 3. .env 세팅

DB_USER, DB_PASSWORD 는 mysql 서버를 설치했을 때 정한 유저명과 패스워드를 넣어준다.

<br>
예를 들어 유저명을 `root` 으로 하고 비밀번호도 `root` 로 정했다면

```dotenv
DB_USER=root
DB_PASSWORD=root
```

그리고 Mysql 서버도 꼭 켜져 있어야 한다.
확인법은

```shell
mysql -u root -p
```

<br>

mysql 설치 
참고 : https://hyunmin1906.tistory.com/80

<br>

DB_HOST 는 DB 호스트 주소인데 현재는 내 컴퓨터에 로컬 서버를 돌리기 때문에 `localhost` 를 넣는다.
나중에 배포할 때는 AWS 서버 주소를 넣으면 된다.

```dotenv
DB_HOST=localhost
```

<br>

DB_NAME 은 데이터베이스명이다. 일단 연결하기 전에 데이터베이스를 만들어야 한다.
데이터베이스명은 예를 들어 `capstone` 이라고 하자.

<br>

* 데이터베이스 먼저 만들기

```sql
CREATE DATABASE capstone
```

<br>

데이터베이스를 만들었다면 데이터베이스명을 적어준다.

```dotenv
DB_NAME=capstone
```


<br><br>

### 요약

현재까지 예시를 든 내용으로 `.env` 파일을 만든다면

```dotenv
DB_USER=root
DB_PASSWORD=root
DB_HOST=localhost
DB_NAME=capstone
```

로 만들 수 있다. 비밀번호는 자신이 정한 값으로 넣어줘야 한다.

