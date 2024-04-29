# github
### 1. 全球最大的同性交友(代码托管)平台
### 2.目前最先进的<font color=orange >版本控制工具、开源社区</font>
## 使用方法
1. 打开VSCode终端，配置git的用户名，邮箱和密码
2. 编辑代码完成后，Ctrl + S 
3. 点击第3个图标将文件，确认无误后，点击“√”即可进行传输

# 上传文件到Github
1. 初始化仓库 git init
- 查看本地库状态 git status 
2. 创建分支 
- git branch 查看分支数和名
- git branch 分支名 创建分支
- git checkout -b 分支名 
创建并切换分支
3. 关联远程库 git remote add 远程库 ssh链接
4. 添加文件
  1. git status 查看本地库状态，当有新文件时，会以红色字体进行显示
  2. 添加
  - git add 文件：添加特定文件
  - git add .:添加所有文件
5. 将文件提交至版本库
git commit -m "备注"
6. 上传文件：git push 远程库名 分支名