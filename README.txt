we need to authenticate and obtain the token. which we will get at endpoint is:
using httpie:   http post http://127.0.0.1:8000/api/token/ email=s@gmail.com password=a

copy access token and make a request:
http http://127.0.0.1:8000/api/get/ "Authorization: Bearer access_token" 