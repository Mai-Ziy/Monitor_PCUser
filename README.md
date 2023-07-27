# Monitor_PCUser
This sowfware in order to Monitor PC about using process,Through the Email send Statement for Monitor (PC owner)

#Version 0.1
#English
This project provides the following functions
1: Collect all current process information of the host (process name, process PID)
2: Special processes (requiring self addition) monitor their process access paths (such as file information being accessed by VScode)
3. Use a local TXT path to store this information
4. Send the TXT file as an attachment via email
5. In theory, the collection frequency or content can be customized by the user
6. Provide more assistance, including how to package the software as an executable file, how to set startup and self start, etc., to help users better

#中文
该项目提供以下功能
1.收集主机当前全部进程信息（进程名称、进程PID）
2.特殊进程（需要自行添加）监控其进程访问路径（比如VS正在访问的文件信息）
3.采用本地TXT路径存放这些信息
4.采用邮件的方式对该TXT文件采用附件的方式发送
5.理论上采集频率或采集内容可以由用户自定义
6.提供更多帮助：包括如何打包软件为可执行文件、如何设置开机自启动等，帮助用户更好地监控主机使用者的情况。

如需打包，请在编译和验证成功后使用pyinstaller -F -w -i icon.ico xxxxx.py打包程序（后台运行）
如果仍在验证阶段需要查看输出信息，请使用pyinstaller -F -i icon.ico xxxxx.py打包程序（前台运行）
