# ia_django
### 인터넷 응용 Django project입니다.
#### 명령어
* 서버 활성화 : python manage.py runserver
* Django 3.0.6 설치 : pip install django==3.0.6
* Django Project : django-admin startproject [PROJECT NAME]
* Django App : django-admin startapp [APP NAME]
* models.py에 변화있을때 : python manage.py makemigrations
* models.py 수정 후 데이터 매핑 : python manage.py migrate
* Admin 생성 : python manage.py createsuperuser
#### Tutorial
* Part 1 ~ Part 7 commit
#### News App
* IPaddress:Portnum/admin/ <br>
: App에 따라 그룹 지어진 모든 모델들을 보여줌
* IPaddress:Portnum/news/articles/[YEAR] <br>
: 해당 [YEAR]에 있는 Article들을 보여줌 <br>
: ex) IPaddress:Portnum/news/articles/2020
* IPaddress:Portnum/news/articles/[YEAR]/[MONTH] <br>
: 해당 [MONTH]에 있는 Article들을 보여줌 <br>
: 여러개의 Article이 있을 경우 모두 보여줌
#### 참조
* Django Tutorial : https://docs.djangoproject.com/en/3.0/
* Django Date Format : https://oddly.tistory.com/64
* Django Example : https://cntechsystems.tistory.com/85?category=817164
