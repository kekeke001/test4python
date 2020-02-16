## Git Bash Here全局配置
1. git config --glogal user.name “–”;
2. git config --glogal user.email “—@–.com”;

## 将代码拷贝到本地
1. fork--fork到自己的github上
2. 将代码拷贝到本地
    a、clone or download---复制地址
    b、创建文件夹，右击打开Git Bash here :git clone 地址（eg：git clone https://github.com/kekeke001/test4python.git）

## 更新的文件上传到Github
1. 打开Git Bash Here
2. git add . :添加所有文件到暂存区 （注：不会有任何提示消息）eg:git add xlsx_utils.py
3. git commit -m ‘注释内容’ :提交所有文件到远程，注释内容一定要写详细，为了以后可以更加清楚自己改动的具体内容  eg:git commit -m 'First try of git'
③ git push 第一次push会有提示，根据提示命令进行  eg:push   git push origin master
