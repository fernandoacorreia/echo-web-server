FROM python:3
ADD files /
EXPOSE 8080
CMD ["python", "/opt/echo/echo.py"]
