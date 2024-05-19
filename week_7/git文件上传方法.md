# Github上传文件
1. 初始化
~~~
git init
~~~
3. 上传全部文件
~~~
git add *
~~~
2.创建分支
~~~
git branch 分支名
~~~ 
3.转到该分支
~~~
git checkout 分支名
~~~
4. 配置账号密码（已配置则跳过）
5. 添加备注
~~~
git commit -m "备注"
~~~
6.文件上传的位置
~~~
git remote add origin 远程分支链接
~~~
7. 开始推送
~~~
git push -u origin 分支名
~~~