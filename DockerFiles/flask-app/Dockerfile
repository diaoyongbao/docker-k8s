# 使用官方提供的python开发环境作为基础镜像
FROM python:2.7-slim

# 将工作目录切换为/app
WORKDIR /app

# 将当前目录所有内容复制到/app下
ADD . /app

# 使用pip命令安装依赖
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 允许外界访问容器的80端口
EXPOSE 80

# 设置环境变量
ENV NAME World

# 设置容器进程为 python app.py 即：这个python应用的启动命令
CMD ["python","app.py"]