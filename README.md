# YoonSeoHee
숙명여대 멋사 아기사자 윤서희🦁
<br><br>
### 🦁 멋사  1학기 4주차 과제 🦁

| 실습 <br> 번호 | 캡쳐 | 
|:------:|:------|
|`17번`| ![17](https://github.com/Likelion-at-SMWU-11th/YoonSeoHee/assets/102652293/ba935a18-0baa-44a3-b221-9a43738f570a)|
|`19번`| ![19](https://github.com/Likelion-at-SMWU-11th/YoonSeoHee/assets/102652293/4284faaa-a6fb-4b42-97b9-209cc99b11f1)|
|`21번`| ![21](https://github.com/Likelion-at-SMWU-11th/YoonSeoHee/assets/102652293/949c8c00-df00-4af9-994a-ad453f021d24)|
|`23번`| ![23](https://github.com/Likelion-at-SMWU-11th/YoonSeoHee/assets/102652293/675a68e0-0d43-4eb9-b097-3408c96b6ca4)|
|`24번`| ![24](https://github.com/Likelion-at-SMWU-11th/YoonSeoHee/assets/102652293/5c1a9c0b-19f0-4f2a-b0a6-1148412664d4)|

### 🦁 멋사  2학기 2주차 과제 🦁
### Controller (Web)

- 기능
    - 요청 url에 따라 적절한 view와 mapping 처리
    - `@Autowired` 를 통해 Service의 method를 이용
    - 적절한 ResponseEntity(DTO)를 body에 담아 Client에 반환
- `@Controller` 와 `@RestController`
    - **Controller**
        - API와 View를 동시에 사용하는 경우
        - API 서비스로 사용하는 경우 @ResponseBody를 사용하여 객체 반환
        - View (화면) 반환이 목적
    - **RestController**
        - API만 지원하는 서비스일 경우 (View 필요 X)
        - `@RequestMapping` 메서드에 @ResponseBody 의미를 가정
        - data(json, xml 등) return이 목적
        
        ⇒ `@Controller` + `@ResponseBody`
        

### Service

- Controller와 Repository 사이의 Middleware
- Model이 DB에서 받아온 데이터를 전달받아 가공하는 역할
- Controller에서 전달받은 사용자의 요청사항에 맞게 데이터를 가공해서 DB에 전달하거나 DB에서 데이터를 전달받아 가공하여 유저에게 전달
- DB 정보가 필요할 때 Repository에게 요청

### Repository

- DB 관리
- DB에 CRUD의 명령을 실행하게 만드는 인터페이스
- Repository 인터페이스 → CrudRepository<Entity, 기본키 타입>을 상속받으면 기본적인 CRUD가 자동으로 생성

### DTO를 사용하는 이유

- DTO : 데이터 저장 담당 클래스 → Controller, Service, View처럼 계층 간의 데이터 교환을 위해 사용
- DTO를 사용하지 않을 경우 통신의 횟수 증가 + 로직 비효율적
- Entity가 아닌 DTO를 전달함으로써 레이어 간 역할을 분리할 수 있음
- 데이터 전송을 위한 직렬화 메커니즘을 캡슐화 → 원하는 경우 직렬화를 변경할 수 있는 명확한 지점을 제공

### 실습 코드 JPA 구조로 설명

- JPA vs Spring JPA
    - Spring JPA는 JPA를 쓰기 편하게 만들어놓은 모듈
    - Sprin JPA가 JPA를 추상화했다 = Repository의 구현에서 JPA를 사용
    - JPA의 핵심 : EntityManagerFactory, EntityManager, EntityTransaction
    - JPA에서의 CRUD
        - 저장 : jpa.persist(post)
        - 조회 : Post post = jpa.find(id)
        - 수정 : member.setTitle(”변경할 제목”)
        - 삭제 : jpa.remove(post)
    ![image](https://github.com/Likelion-at-SMWU-11th/YoonSeoHee/assets/102652293/964ccd30-d64a-4b79-9b5d-23dc86151f19)

- RestController : API만 작성하기 위함
    - `@Autowired PostService` 를 통해 PostService를 사용할 것을 명시
    - `@RequestMapping("Post")` 에 @ResponseBody 의미를 가정
- Service : CRUD 서비스 기능 작성
    - `@Autowired PostDao` 를 통해 postDao의 method를 이용
        
        → PostDao에서는 Repository의 method를 이용
        
- DTO : 계층간 데이터 교환을 위한 객체
    - `@Getter`와 `@Setter`를 이용해 PostDto의 getter/setter 메소드만 가지고 있음
- Entity Class : 실제 DB의 테이블과 매칭될 클래스
    - PostEntity와 BoardEntity 작성
