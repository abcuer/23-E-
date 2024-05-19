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
8. 第一次配置
git config --global user.name "DBinK"
git config --global user.email "DBinKv1@Gmail.com"

# 设置代理
git config --global http.proxy http://192.168.100.49:7897
git config --global https.proxy https://192.168.100.49:7897

git config --global --unset http.proxy
git config --global --unset https.proxy

# 基础操作
git init    # 初始化项目， 有了GitHub几乎不用
git status  # 查看整个仓库的状态
git add .   # 把新增文件添加到暂存区，以备提交
git commit -m "本次提交的备注" # 命令生成一个新的提交
git push    # 提交推送到 GitHub 远程仓库
git push -f # 将本地分支强制推送到远程仓库

# 分支操作


git fetch origin              # 获取远程分支的最新更新
git reset --hard origin/main  # 将本地分支重置到远程分支的最新提交