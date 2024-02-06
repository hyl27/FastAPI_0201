## 프로젝트명
파이보(Pybo): QnA 게시판


## 프로젝트 소개
파이보는 회원가입과 로그인을 통해 질문과 그 질문에 대한 답변을 달 수 있다.


## 프로젝트 설치 및 실행 방법
* Installation:
  
`$ git clone https://github.com/hyl27/FastAPI_0201.git`

* Requirements:
  
`$ pip install -r requirements.txt`  


* Backend:
  
```
$ uvicorn main:app --reload
```

* Frontend:
  
```
$ cd frontend
$ npm install
$ npm run dev
```


## 프로젝트 사용 방법
`cd frontend`에서 
`npm run build` 하여 프론트엔드 서버없이 접속 가능하다.  
http://127.0.0.1:8000/ 

## 참고자료
[점프 투 FastAPI](https://wikidocs.net/book/8531)

