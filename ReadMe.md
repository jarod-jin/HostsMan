#Read Me#

>这是一个修改hosts的小脚本，可以自动适配了windows系统和mac系统

##使用步骤##

###确认安装python###
window系统需要安装python2.7，mac系统一般是自带python运行环境，也可以在终端下键入

    python -V
如果这样显示：

![](http://i.imgur.com/ymF5VPR.png)

表示已经安装了python 2.7

###修改hosts文件权限###

####mac系统####
可以使用一下命令

    sudo chmod 777 /private/etc/hosts

然后需要输入您mac系统的密码

####windows系统####
打开文件夹

	C:\Windows\System32\drivers\etc

找到hosts文件，右键点击文件，选择属性

![](http://i.imgur.com/VXtEcXX.png)

![](http://i.imgur.com/YMSYFRS.png)

然后确认



###使用脚本###

在终端下切换到HostsMan的文件夹下使用以下命令

    python ./HostsMan.py

最后根据提示输入

####关于hosts备份####

hostsbak文件夹是每次修改的前一次hosts文件修改






