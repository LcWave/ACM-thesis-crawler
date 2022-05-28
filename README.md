# ACM-thesis-crawler
一个简单的用于批量爬取ACM论文的爬虫
# 环境
```bash
python 3.6
selenium
```
# 使用步骤
## 1.下载浏览器驱动
[下载地址](http://chromedriver.storage.googleapis.com/index.html)

需要下载与Chrome浏览器版本匹配的驱动
## 2.修改项
### 1）修改驱动位置
![image](https://user-images.githubusercontent.com/86061264/170816770-f2bd42a8-bf84-4462-9f53-669933d12738.png)

将驱动的位置修改成你存放的位置
### 2）修改主文件夹位置
![image](https://user-images.githubusercontent.com/86061264/170816835-e8d60cf4-a26b-442b-b443-b878bb0f9566.png)

修改成你想存放的位置
### 3）修改下载地址
在Proceedings中找到要要下载会议的地址
![image](https://user-images.githubusercontent.com/86061264/170817026-29052306-0abf-4068-91bb-ad143b80b002.png)
![image](https://user-images.githubusercontent.com/86061264/170817036-f3099a85-6200-48f2-9d67-b6d76688722c.png)
### 4）看需求决定是否注释子文件夹
如果网页是这种形式，可以不注释
![image](https://user-images.githubusercontent.com/86061264/170817182-b26b154c-fe82-4d00-a90c-0548ac8f478f.png)

如果没有session，或全为展开形式，注释掉下面一段即可

![image](https://user-images.githubusercontent.com/86061264/170817074-ca04db0d-974b-4621-b07c-2bd02777677c.png)
### 5）修改k
注释掉创建子文件夹代码的可以不管
看第一个session中有多少个pdf，有多少个，将下图中的判断条件改成几个。

![image](https://user-images.githubusercontent.com/86061264/170817524-12f810ee-8bee-418f-81c3-b38951b67d2d.png)

### ！！！注意
由于在爬取时没有将pdf链接与论文名字打包在一起（有时间会改），需要根据实际情况修改一下片段

![image](https://user-images.githubusercontent.com/86061264/170817657-7908e6eb-18fe-430e-a8a0-9cd8abfc17ef.png)
