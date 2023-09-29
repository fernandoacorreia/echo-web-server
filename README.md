# echo-web-server
A sample web server that just echoes requests

## Running as a script

```
PORT=8888 ./files/opt/echo/echo.py
```

## Running in a container

```
docker build -t echo-web-server .

docker run --rm -it -P echo-web-server
```
