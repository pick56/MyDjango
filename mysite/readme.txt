1,启动一个完整的django项目的命令是
python manage.py runserver
或
python manage.py runserver 8889
python manage.py runserver 0.8889
python manage.py runserver 0.0.0.0:8889

2，创建应用
python manage.py startapp polls
应用和mysite有区别

3，改变模型需要这三步：

编辑 models.py 文件，改变模型。
运行 python manage.py makemigrations 为模型的改变生成迁移文件。
运行 python manage.py migrate 来应用数据库迁移。

4，Django 管理页面

Username: admin
Email address: admin@example.com
Password: 123456
Password (again): 123456
Superuser created successfully.