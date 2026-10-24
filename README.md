# git_learning
```bash

git init  #在当前文件夹里创建一个 Git 仓库,每个仓库只执行一次
git remote add origin <repository_url> #给本地仓库登记一个远程地址,<>为占位符，需要替换为仓库地址.git
git branch -M main #把当前分支重命名为 main
git add . #将改动加入暂存区 .为当前目录下的全部内容，单个文件替换为文件名，如READMME.md
git commit -m 'Your commit message here!'#把暂存区的内容打包成一条提交记录，存进本地历史 ‘’为说明文字
git status #查看状态
git push -u origin main #把本地提交上传到 GitHub


