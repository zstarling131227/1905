#   ***git笔记整理*** 

## 1. git 安装
        sudo apt-get install git
    在终端输入git 检测git是否安装好
    ```
    tarena@tarena:~$ git
    ```
----------------------------------------------------------------------------------------------
## 2. git 使用

###  初始配置
>   配置命令: git config

    1.  配置所有用户： git config --system [选项]
            配置文件位置: /etc/gitconfig
         ```
        tarena@tarena:~$ sudo git config --system user.name Tedu
        [sudo] tarena 的密码： 
        tarena@tarena:~$ cat /etc/gitconfig
        [user]
        name = Tedu
        ```
    2.  配置当前用户： git config --global [选项]
            配置文件位置: ~/.gitconfig
        ```
        tarena@tarena:~$ git config --global user.email 1239269939@qq.com
        tarena@tarena:~$ cat .gitconfig
        [user]
            email = 1239269939@qq.com
        ```
    3.  配置当前项目： git config [选项]
            配置文件位置: project/.git/config
        >> 创建项目（在配置邮箱之前首先要创建项目）
            ```
            tarena@tarena:~$ mkdir gitproject
            tarena@tarena:~$ cd gitproject
            tarena@tarena:~/gitproject$ ls
            tarena@tarena:~/gitproject$ git init
            已初始化空的 Git 仓库于 /home/tarena/gitproject/.git/
            tarena@tarena:~/gitproject$ 
            ```
        >>配置编译器为pycharm
            ```
            tarena@tarena:~/gitproject$ git config core.editor pycharm
            ```
        >>查看配置信息
            ```
            tarena@tarena:~/gitproject$ ls -a
            .  ..  .git
            tarena@tarena:~/gitproject$ cat .git/config
            [core]
                repositoryformatversion = 0
                filemode = true
                bare = false
                logallrefupdates = true
                editor = pycharm
            >> 查看配置信息
            tarena@tarena:~/gitproject$ git config --list
            user.name=Tedu
            user.email=1239269939@qq.com
            core.repositoryformatversion=0
            core.filemode=true
            core.bare=false
            core.logallrefupdates=true
            core.editor=pycharm
            tarena@tarena:~/gitproject$ 
            ```
---------------------------------------------------------------------------------------------
###基本命令
>   
    1.     初始化仓库
        git init
        意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理
        >> 在配置文件时已经初始化过
            ```
            tarena@tarena:~/gitproject$ git init
            >>>
                重新初始化已存在的 Git 仓库于 /home/tarena/gitproject/.git/
            ```
    2.     查看本地仓库状态
        git status
        说明: 初始化仓库后默认工作在master分支，当工作区与仓库区不一致时会有提示。
        >> 无文件时的状态输出
            ```
            tarena@tarena:~/gitproject$ git status
            >>>
                位于分支 master
                尚无提交
                无文件要提交（创建/拷贝文件并使用 "git add" 建立跟踪）
            ```
        >> 有文件时的状态输出
            ```
            tarena@tarena:~/gitproject$ ls
            >>>
                bitree.py     'httpserver (1).py'   img2.jpg   mythread.py   test
                day02_am.rar   img1.jpg             img3.jpg   README.md
            tarena@tarena:~/gitproject$ git status
             >>>   
                位于分支 master

                尚无提交

                未跟踪的文件:
                （使用 "git add <文件>..." 以包含要提交的内容）

                README.md
                bitree.py
                day02_am.rar
                httpserver (1).py
                img1.jpg
                img2.jpg
                img3.jpg
                mythread.py
                test/

                 提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
            ```
    3.     将工作内容记录到暂存区
            git add [files..]
        >> 将文件记录到暂存区
            ```
            tarena@tarena:~/gitproject$ git add bitree.py
            tarena@tarena:~/gitproject$ git add img1.jpg mythread.py 
            tarena@tarena:~/gitproject$ git add test
            tarena@tarena:~/gitproject$ git status
            >>>
                位于分支 master

                尚无提交

                要提交的变更：
                （使用 "git rm --cached <文件>..." 以取消暂存）

                    新文件：   bitree.py
                    新文件：   img1.jpg
                    新文件：   mythread.py
                    新文件：   test/exercise.py
                    新文件：   test/test1.py
                    新文件：   test/test2.py

                未跟踪的文件:
                （使用 "git add <文件>..." 以包含要提交的内容）

                    README.md
                    day02_am.rar
                    httpserver (1).py
                    img2.jpg
                    img3.jpg
            ```
        
        >> 将所有文件（不包含隐藏文件）记录到暂存区
            git add  *
            ```
            tarena@tarena:~/gitproject$ git add *
            tarena@tarena:~/gitproject$ git status
            >>> 未在pycahrm中打开时的状态
                位于分支 master

                尚无提交

                要提交的变更：
                （使用 "git rm --cached <文件>..." 以取消暂存）

                    新文件：   README.md
                    新文件：   bitree.py
                    新文件：   day02_am.rar
                    新文件：   httpserver (1).py
                    新文件：   img1.jpg
                    新文件：   img2.jpg
                    新文件：   img3.jpg
                    新文件：   mythread.py
                    新文件：   test/exercise.py
                    新文件：   test/test1.py
                    新文件：   test/test2.py
            ```
    4.     取消文件暂存记录
        git rm --cached [file]
        >>
            tarena@tarena:~/gitproject$ git rm --cached README.md
            rm 'README.md'
            tarena@tarena:~/gitproject$ git status
            >>>
            ……
            未跟踪的文件:
            （使用 "git add <文件>..." 以包含要提交的内容）

                README.md

    5.     将文件同步到本地仓库
        git commit [file] -m [message]
        说明: -m表示添加一些同步信息，表达同步内容
        >>将暂存区所有记录同步到仓库区
             git commit  -m 'add files'
             ```
            tarena@tarena:~/gitproject$ git commit  -m 'add files'
            >>>
                [master （根提交） c47f6be] add files
                11 files changed, 574 insertions(+)
                create mode 100644 .gitignore
                create mode 100644 bitree.py
                create mode 100644 day02_am.rar
                create mode 100644 httpserver (1).py
                create mode 100644 img1.jpg
                create mode 100644 img2.jpg
                create mode 100644 img3.jpg
                create mode 100644 mythread.py
                create mode 100644 test/exercise.py
                create mode 100644 test/test1.py
                create mode 100644 test/test2.py
             ```
        >>
            tarena@tarena:~/gitproject$ git commit readme.md -m 'add readme'
                 >>>
                [master 4c65737] add readme
                1 file changed, 3 insertions(+)
                create mode 100644 readme.md
            tarena@tarena:~/gitproject$ git status
                >>>
                    位于分支 master
                    未跟踪的文件:
                    （使用 "git add <文件>..." 以包含要提交的内容）

                        README1.md

                    提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）

        >>查看commit 日志记录
               >>>显示全部 git log
                ```
                tarena@tarena:~/gitproject$ git log
                >>>
                    commit 4c6573744351370eca85a78f6bbc12175066a41c (HEAD -> master)
                    Author: Tedu <1239269939@qq.com>
                    Date:   Thu Jul 18 11:02:05 2019 +0800

                        add readme

                    commit c47f6be03b0dda5b3c767fc8c4e0ff66c5c77989
                    Author: Tedu <1239269939@qq.com>
                    Date:   Thu Jul 18 10:57:29 2019 +0800

                        add files
                ```
                >>>只显示部分 git log --pretty=oneline
                ```
                tarena@tarena:~/gitproject$ git log --pretty=oneline
                    >>>
                        4c6573744351370eca85a78f6bbc12175066a41c (HEAD -> master) add readme
                        c47f6be03b0dda5b3c767fc8c4e0ff66c5c77989 add files

                ```

    6.     比较工作区文件和仓库文件差异
        git diff [file]
        >>
            tarena@tarena:~/gitproject$ git diff readme.md
            >>>

    7.     将暂存区或者某个commit点文件恢复到工作区
        git checkout [commit] -- [file]
        ***********
        --是为了防止误操作，checkout还有切换分支的作用
        移动或者删除文件
        git mv [file] [path]
        git rm [files]
        注意: 这两个操作会修改工作区内容，同时将操作记录提交到暂存区。
        >>git rm [files]
            ```
            tarena@tarena:~/gitproject$ ls
                bitree.py     'httpserver (1).py'   img2.jpg   mythread.py   readme.md
                day02_am.rar   img1.jpg             img3.jpg   README1.md    test
            tarena@tarena:~/gitproject$ rm img1.jpg
            tarena@tarena:~/gitproject$ ls
                bitree.py     'httpserver (1).py'   img3.jpg      README1.md   test
                day02_am.rar   img2.jpg             mythread.py   readme.md
             tarena@tarena:~/gitproject$ git checkout -- img1.jpg
            tarena@tarena:~/gitproject$ ls
                bitree.py     'httpserver (1).py'   img2.jpg   mythread.py   readme.md
                day02_am.rar   img1.jpg             img3.jpg   README1.md    test
             ```
        >>git mv [file] [path]
             ```
                tarena@tarena:~/gitproject$ ls
                >>>
                    bitree.py            img1.jpg   img3.jpg      README1.md   test
                    'httpserver (1).py'   img2.jpg   mythread.py   readme.md
                tarena@tarena:~/gitproject$ git mv mythread.py test 
                tarena@tarena:~/gitproject$ git status
                 >>>  
                    位于分支 master
                    要提交的变更：
                    （使用 "git reset HEAD <文件>..." 以取消暂存）

                        新文件：   README1.md
                        删除：     day02_am.rar
                        重命名：   mythread.py -> test/mythread.py

                tarena@tarena:~/gitproject$ git commit -m "mv and rm"
                 >>>
                    [master ed9f169] mv and rm
                    3 files changed, 198 insertions(+)
                    create mode 100644 README1.md
                    delete mode 100644 day02_am.rar
                    rename mythread.py => test/mythread.py (100%)
                tarena@tarena:~/gitproject$ git status
                >>>
                    位于分支 master
                    无文件要提交，干净的工作区
             ```

---------------------------------------------------------------------------------------------
### 扩展功能
> 隐藏文件
    >> 
    ```
    tarena@tarena:~/gitproject$ ls .git/
    branches  config  description  HEAD  hooks  index  info  objects  refs
    ```
    >>在pycharm中打开项目gitproject，然后在终端查看状态，
        未跟踪的文件下会显示.idea/。
        ```
        tarena@tarena:~/gitproject$ git status
        >>>
            位于分支 master

            尚无提交

            要提交的变更：
            （使用 "git rm --cached <文件>..." 以取消暂存）

                新文件：   README.md
                新文件：   bitree.py
                新文件：   day02_am.rar
                新文件：   httpserver (1).py
                新文件：   img1.jpg
                新文件：   img2.jpg
                新文件：   img3.jpg
                新文件：   mythread.py
                新文件：   test/exercise.py
                新文件：   test/test1.py
                新文件：   test/test2.py

            未跟踪的文件:
            （使用 "git add <文件>..." 以包含要提交的内容）

                .idea/
        ```
    >> 在pycahrm中新建一个隐藏文件.gitignore（new--file--输入 .gitignore回车），在 .gitignore中输入.idea.
        此时查看状态不显示.idea/，而显示  .gitignore。
        ```
        tarena@tarena:~/gitproject$ git status
        >>>
            ……
            尚未暂存以备提交的变更：
            （使用 "git add <文件>..." 更新要提交的内容）
            （使用 "git checkout -- <文件>..." 丢弃工作区的改动）

                修改：     .gitignore
    ```
    >> 添加隐藏文件 .gitignore。git add .gitignore或者 git add *均可以
         ```
        tarena@tarena:~/gitproject$ git add .gitignore
        tarena@tarena:~/gitproject$ git add *
        tarena@tarena:~/gitproject$ git status
        >>>
            位于分支 master

            尚无提交

            要提交的变更：
            （使用 "git rm --cached <文件>..." 以取消暂存）

                新文件：   .gitignore
                新文件：   README.md
                新文件：   bitree.py
                新文件：   day02_am.rar
                新文件：   httpserver (1).py
                新文件：   img1.jpg
                新文件：   img2.jpg
                新文件：   img3.jpg
                新文件：   mythread.py
                新文件：   test/exercise.py
                新文件：   test/test1.py
                新文件：   test/test2.py
         ```

---------------------------------------------------------------------------------------------
###版本控制
> 
    1.退回到上一个commit节点
        git reset --hard HEAD^
        注意 ： 一个^表示回退1个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致
        >>
        ```
            tarena@tarena:~/gitproject$ git reset --hard HEAD^
            >>>HEAD 现在位于 4c65737 add readme
            tarena@tarena:~/gitproject$ ls
            >>>
                bitree.py     'httpserver (1).py'   img2.jpg   mythread.py   test
                day02_am.rar   img1.jpg             img3.jpg   readme.md
            tarena@tarena:~/gitproject$ git status
            >>>   
                位于分支 master
                无文件要提交，干净的工作区
        ```
    2.退回到指定的commit_id节点
        git reset --hard [commit_id]
        >>
            ```
                tarena@tarena:~/gitproject$ git reset --hard 4c65737
                >>>
                    HEAD 现在位于 4c65737 add readme
                tarena@tarena:~/gitproject$ ls
                >>>
                    bitree.py     'httpserver (1).py'   img2.jpg   mythread.py   test
                    day02_am.rar   img1.jpg             img3.jpg   readme.md
                tarena@tarena:~/gitproject$ git log
                >>>
                    commit 4c6573744351370eca85a78f6bbc12175066a41c (HEAD -> master)
                    Author: Tedu <1239269939@qq.com>
                    Date:   Thu Jul 18 11:02:05 2019 +0800

                        add readme

                    commit c47f6be03b0dda5b3c767fc8c4e0ff66c5c77989
                    Author: Tedu <1239269939@qq.com>
                    Date:   Thu Jul 18 10:57:29 2019 +0800

                        add files
            ```
    3.查看所有操作记录
        git reflog
        注意:最上面的为最新记录，可以利用commit_id去往任何操作位置
        >>
            ```
            tarena@tarena:~/gitproject$ git reflog
            >>>
                4c65737 (HEAD -> master) HEAD@{0}: reset: moving to 4c65737
                4c65737 (HEAD -> master) HEAD@{1}: reset: moving to HEAD^
                ed9f169 HEAD@{2}: commit: mv and rm
                4c65737 (HEAD -> master) HEAD@{3}: commit: add readme
                c47f6be HEAD@{4}: commit (initial): add files
            ```
    4.创建标签
        标签: 在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。
        git tag [tag_name] [commit_id] -m [message]
        说明: commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。
        >>在最新的commit处添加标签v1.0  --------git tag v1.0 -m '版本1'
            ```
            tarena@tarena:~/gitproject$  git tag v1.0 -m '版本1'
            tarena@tarena:~/gitproject$ git tag
            v1.0

            ```
    5.查看标签
        git tag 查看标签列表
        git show [tag_name] 查看标签详细信息
        >>
            ```
            tarena@tarena:~/gitproject$ git show v1.0
                >>>    
                        tag v1.0
                        Tagger: Tedu <1239269939@qq.com>
                        Date:   Thu Jul 18 11:41:21 2019 +0800

                        版本1
                        ……
            ```
    6.去往某个标签节点
        git reset --hard [tag]
        >>
            ```
            tarena@tarena:~/gitproject$ git reset --hard v0.9
            >>>
                HEAD 现在位于 c47f6be add files
            tarena@tarena:~/gitproject$ git reset --hard v1.0
            >>>
                HEAD 现在位于 4c65737 add readme

            ```
    7.删除标签
        git tag -d [tag]
        >>
                ```
                tarena@tarena:~/gitproject$ git tag -d v0.9
                已删除标签 'v0.9'（曾为 aad9e17）
                tarena@tarena:~/gitproject$ git tag
                v1.0
                ```
---------------------------------------------------------------------------------------------
###保存工作区
> 
    1.  保存工作区内容
        git stash save [message]
        说明: 将工作区未提交的修改封存，让工作区回到修改前的状态
        >>
        ```
        tarena@tarena:~/gitproject$ git stash save "数据结构"
        保存工作目录和索引状态 On master: 数据结构
        tarena@tarena:~/gitproject$ git status
        位于分支 master
        无文件要提交，干净的工作区
        tarena@tarena:~/gitproject$ git stash save "IO网络"
        保存工作目录和索引状态 On master: IO网络
        tarena@tarena:~/gitproject$ git stash save "IO网络"
        没有要保存的本地修改
        tarena@tarena:~/gitproject$ git stash save "线程进程"
        保存工作目录和索引状态 On master: 线程进程
        ```
    2.   查看工作区列表
        git stash list
        说明:最新保存的工作区在最上面
        >>
            ```
                tarena@tarena:~/gitproject$ git stash list
                    >>>   
                    stash@{0}: On master: 数据结构
                    tarena@tarena:~/gitproject$ git stash list
                    stash@{0}: On master: 线程进程
                    stash@{1}: On master: IO网络
                    stash@{2}: On master: 数据结构
                tarena@tarena:~/gitproject$ git status
                    >>>
                    位于分支 master
                    无文件要提交，干净的工作区
            ```
    3.  应用某个工作区
        git stash apply [stash@{n}]
        >>
            ```
            tarena@tarena:~/gitproject$ git stash apply stash@{1}
                >>>
                位于分支 master
                尚未暂存以备提交的变更：
                （使用 "git add <文件>..." 更新要提交的内容）
                （使用 "git checkout -- <文件>..." 丢弃工作区的改动）

                    修改：     readme.md

                修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
            tarena@tarena:~/gitproject$ git add *
            tarena@tarena:~/gitproject$ git commit -m 'charge readme'
            >>>
                [master 5243e02] charge readme
                1 file changed, 2 insertions(+)
            ```
    4.  删除工作区
            git stash drop [stash@{n}] 删除某一个工作区
            git stash clear 删除所有保存的工作区
            >>drop
                ```
                tarena@tarena:~/gitproject$ git stash list
                    >>>
                    stash@{0}: On master: 线程进程
                    stash@{1}: On master: IO网络
                    stash@{2}: On master: 数据结构
                tarena@tarena:~/gitproject$ git stash drop stash@{0}
                    >>>
                    丢弃了 stash@{0} (6eb0952f372f9698a8d1516d66754bfa70edb1aa)
                tarena@tarena:~/gitproject$ git stash list
                    >>>
                    stash@{0}: On master: IO网络
                    stash@{1}: On master: 数据结构
                ```
            >>clear
                ```
                tarena@tarena:~/gitproject$ git stash clear
                tarena@tarena:~/gitproject$ git stash list
                ```
---------------------------------------------------------------------------------------------
###分支管理
>   定义: 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，单独开发，互不干扰。完成开发工作后再进行分支统一合并。

    1.  查看分支情况
        git branch
        说明: 前面带 * 的分支表示当前工作分支
        >>
            ```
                tarena@tarena:~/gitproject$ git branch
                * master
                tarena@tarena:~/gitproject$ git status
                位于分支 master
                无文件要提交，干净的工作区
            ```
    2.  创建分支
        git branch [branch_name]
        说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支"干净"状态。
        >>
        ```
            tarena@tarena:~/gitproject$ git branch joy_dev
            tarena@tarena:~/gitproject$ git branch
            joy_dev
            * master
        ```

    3.  切换工作分支
        git checkout [branch]
        说明: 2,3可以同时操作，即创建并切换分支

        git checkout -b [branch_name]
        >>
        ```
            tarena@tarena:~/gitproject$ git  checkout joy_dev
                切换到分支 'joy_dev'
            tarena@tarena:~/gitproject$ git branch
                * joy_dev
                master
            tarena@tarena:~/gitproject$ ls
                bitree.py            img1.jpg   mythread.py
                day02_am.rar         img2.jpg   readme.md
                'httpserver (1).py'   img3.jpg   test
            tarena@tarena:~/gitproject$ git  checkout master
                切换到分支 'master'
                arena@tarena:~/gitproject$ git branch
                joy_dev
                * master
            >>创建并切换到新建分支
            tarena@tarena:~/gitproject$ git  checkout -b ALex_dev
                切换到一个新分支 'ALex_dev'
            tarena@tarena:~/gitproject$ git branch
                * ALex_dev
                joy_dev
                master
        ```
        ```
        tarena@tarena:~/gitproject$ git checkout ALex_dev
            切换到分支 'ALex_dev'
            ***修改完成后要重新添加
        tarena@tarena:~/gitproject$ git add *
        tarena@tarena:~/gitproject$ git commit -m 'changed readme'
            [ALex_dev 58bfd7a] changed readme
            1 file changed, 4 insertions(+), 1 deletion(-)
            ```
    4.  合并分支
        git merge [branch]

        冲突问题是合并分支过程中最为棘手的问题

        当分支合并时，原分支和以前发生了变化就会产生冲突
        当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需自己决定commit操作即可。
        当合并分支时两个分支修改了同一个文件，则需要手动解决冲突。
        >>
            ```
                tarena@tarena:~/gitproject$ git merge ALex_dev
                    >>>
                    更新 5243e02..3339537
                    Fast-forward
                    readme.md | 4 +++-
                    1 file changed, 3 insertions(+), 1 deletion(-)
                 tarena@tarena:~/gitproject$ git status
                    >>>
                    位于分支 master
                    无文件要提交，干净的工作区
            ```
    5.  删除分支
        git branch -d [branch] 删除分支
        git branch -D [branch] 删除没有被合并的分支
        >>
            ```
            tarena@tarena:~/gitproject$ git branch -d joy_dev
            已删除分支 joy_dev（曾为 5243e02）。
            ```
---------------------------------------------------------------------------------------------
###远程仓库
> 
    1.    添加远程仓库
        git remote  add origin https://github.com/xxxxxxxxx
        >>
                tarena@tarena:~/gitproject$ git remote add origin https://github.com/zstarling131227/https-github.com-new.git
    2.    删除远程主机
        git remote rm [origin]
        >>
            tarena@tarena:~/gitproject$ git remote rm origin
            tarena@tarena:~/gitproject$ git remote###删除后查看为空

    3.    查看连接的主机
        git remote
        注意: 一个git项目连接的远程主机名不会重复
        >>
            tarena@tarena:~/gitproject$ git remote
            origin
    4.    将本地分支推送给远程仓库
        将master分支推送给origin主机远程仓库，第一次推送分支使用-u表示与远程对应分支建立自动关联
        git push -u origin  master
        >>首次上传master
            ```
                tarena@tarena:~/gitproject$  git push -u origin  master
                >>> 
                    Username for 'https://github.com': zstarling131227  
                    Password for 'https://zstarling131227@github.com': 
                    对象计数中: 39, 完成.
                    Delta compression using up to 4 threads.
                    压缩对象中: 100% (35/35), 完成.
                    写入对象中: 100% (39/39), 310.08 KiB | 18.24 MiB/s, 完成.
                    Total 39 (delta 13), reused 0 (delta 0)
                    remote: Resolving deltas: 100% (13/13), done.
                    To https://github.com/zstarling131227/https-github.com-new.git
                    * [new branch]      master -> master
                    分支 'master' 设置为跟踪来自 'origin' 的远程分支 'master'。
                ```
        >>修改后重新上传
            ***注意：
                tarena@tedu:~/test/1905/test/gtihub_project$ git push
                    warning: push.default 尚未设置，它的默认值在 Git 2.0 已从 'matching'
                    变更为 'simple'。若要不再显示本信息并保持传统习惯，进行如下设置：
                    git config --global push.default matching
                    若要不再显示本信息并从现在开始采用新的使用习惯，设置：
                    git config --global push.default simple
                    当 push.default 设置为 'matching' 后，git 将推送和远程同名的所有
                    本地分支。
                    从 Git 2.0 开始，Git 默认采用更为保守的 'simple' 模式，只推送当前
                    分支到远程关联的同名分支，即 'git push' 推送当前分支。
                    参见 'git help config' 并查找 'push.default' 以获取更多信息。
                    （'simple' 模式由 Git 1.7.11 版本引入。如果您有时要使用老版本的 Git，
                    为保持兼容，请用 'current' 代替 'simple'）
                    fatal: unable to access 'http://github.com/zstarling131227/wangbadan.git/': Recv failure: 
                    连接被对方重设***

            ```
            tarena@tarena:~/gitproject$ git add *
            tarena@tarena:~/gitproject$ git commit -m 'change2'
                >>>
                [master b1d6f0d] change2
                1 file changed, 2 insertions(+)
            tarena@tarena:~/gitproject$ git push
                >>>
                Username for 'https://github.com': zstarling131227
                Password for 'https://zstarling131227@github.com': 
                对象计数中: 3, 完成.
                Delta compression using up to 4 threads.
                压缩对象中: 100% (3/3), 完成.
                写入对象中: 100% (3/3), 340 bytes | 340.00 KiB/s, 完成.
                Total 3 (delta 2), reused 0 (delta 0)
                remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
                To https://github.com/zstarling131227/https-github.com-new.git
                37359eb..b1d6f0d  master -> master
        >>将分支ALex_dev上传
            tarena@tarena:~/gitproject$ git push -u origin ALex_dev
        >>将标签v1.0上传
            tarena@tarena:~/gitproject$ git push origin v1.0

    5.    删除远程分支
        git branch -a 查看所有分支
        git push origin [:branch] 删除远程分支
        >>
            tarena@tarena:~/gitproject$ git push origin :ALex_dev
                >>> 
                    Username for 'https://github.com': zstarling131227
                    Password for 'https://zstarling131227@github.com': 
                    To https://github.com/zstarling131227/https-github.com-new.git
                    - [deleted]         ALex_dev
            tarena@tarena:~/gitproject$ git push origin --delete tag v1.0
                >>>
                    Username for 'https://github.com': zstarling131227
                    Password for 'https://zstarling131227@github.com': 
                    To https://github.com/zstarling131227/https-github.com-new.git
                    - [deleted]         v1.0

    6.    其他推送方法
        git push --force origin 用于本地版本比远程版本旧时强行推送本地版本
        git push origin [tag] 推送本地标签到远程
        git push origin --tags 推送本地所有标签到远程
        git push origin --delete tag [tagname] 删除远程仓库标签
        >>
            tarena@tarena:~/gitproject$ git reset --hard HEAD^
                >>>HEAD 现在位于 37359eb changed readme
            tarena@tarena:~/gitproject$ git status
                >>>
                    位于分支 master
                    您的分支落后 'origin/master' 共 1 个提交，并且可以快进。
                    （使用 "git pull" 来更新您的本地分支）

                    无文件要提交，干净的工作区
            tarena@tarena:~/gitproject$ git push --force origin
                >>>
                    Username for 'https://github.com': zstarling131227
                    Password for 'https://zstarling131227@github.com': 
                    Total 0 (delta 0), reused 0 (delta 0)
                    To https://github.com/zstarling131227/https-github.com-new.git
                    + b1d6f0d...37359eb master -> master (forced update)

    7.    从远程获取代码
        git pull
        将远程分支master拉取到本地，作为tmp分支
        git fetch origin master:tmp

        ***区别***
        pull将远程内容直接拉取到本地，并和对应分支内容进行合并
        fetch将远程分支内容拉取到本地，但是不会和本地对应分支合并，可以自己判断后再使用merge合并。
        >> git pull
            ```
            tarena@tarena:~/gitproject$ git pull origin
            ###或者tarena@tarena:~/gitproject$ git pull 都可以
                >>> 
                    remote: Enumerating objects: 5, done.
                    remote: Counting objects: 100% (5/5), done.
                    remote: Compressing objects: 100% (3/3), done.
                    remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
                    展开对象中: 100% (3/3), 完成.
                    来自 https://github.com/zstarling131227/https-github.com-new
                    37359eb..c1e71bc  master     -> origin/master
                    更新 37359eb..c1e71bc
                    Fast-forward
                    mythread.py | 4 +++-
                    1 file changed, 3 insertions(+), 1 deletion(-)
            ```
        >> git fetch
            ```
                tarena@tarena:~/gitproject$ git fetch origin master:tmp
                    >>> 
                        remote: Enumerating objects: 5, done.
                        remote: Counting objects: 100% (5/5), done.
                        remote: Compressing objects: 100% (3/3), done.
                        remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
                        展开对象中: 100% (3/3), 完成.
                        来自 https://github.com/zstarling131227/https-github.com-new
                        * [新分支]          master     -> tmp
                        c1e71bc..f960a7e  master     -> origin/master
                tarena@tarena:~/gitproject$ git branch
                    >>>
                        ALex_dev
                        * master
                        tmp
                tarena@tarena:~/gitproject$ git merge tmp
                    >>>
                        更新 c1e71bc..f960a7e
                        Fast-forward
                        github.py | 4 +++-
                        1 file changed, 3 insertions(+), 1 deletion(-)
                        tarena@tarena:~/gitproject$ 
            ```
