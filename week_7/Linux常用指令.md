# Linux命令：
## @形式
**- 指令 名1 名2**
**- 指令 -r 名1 名2**

### 1. ls：查看/访问当前目录的文件和内容
例：ls Code Desktop
### 2. cd :进入目录

~~~
cd Code
cd .. :回到上一级目录
cd -：回到上次的目录
cd ~：回到终端首页
cd /：进入根目录
~~~
### 3. tree：列出一文件夹中的所有子文件夹和文件
~~~
tree Code：列出Code文件夹中的文件和目录
~~~
### 4. 路径
绝对路径：E：\program\application  
相对路径：.\application

### 5. mkdir:新建目录
~~~
mkdir Code:新建名为Code的目录
mkdir -p one/two/three：一次性创建多个目录 
~~~
### 6. touch:新建文件
### 7. cp : 复制文件
~~~
cp hello one/two/:　复制文件到one/two 的目录下
cp -r：复制目录到指定目录
 ~~~
### 8. rm：删除文件
~~~
rm -r ：删除目录
~~~
### 9. mv：移动位置
~~~
 mv 名1 名2：将  名1  移到  名2 中
 (名1：文件；名2：文件夹或目录)
 重命名
mv test1 test2：将test1更名为test2
(名1：文件；  名2：文件)
~~~
### 10.  cat命令：
~~~
cat 文件路径：显示文件内容
cat -n 文件路径 ：有序的显示文件内容
~~~
### 11.  pwd
~~~
查看当前所处目录
获取当前目录的绝对路径
~~~