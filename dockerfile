FROM python:3
WORKDIR  /daily_steps
COPY . .
CMD ["python", "daily_steps.py"]