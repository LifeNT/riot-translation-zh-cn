# riot-web-trans
riot web client translation python script

riot web 客户端的界面汉化脚本（python），部分完成

说明：这个脚本程序(riot-trans.py)可以读取riot的界面字符串，替换为中文字符

最新版本riot下载地址：https://github.com/vector-im/riot-web

请将该文件复制到riot根目录，运行，输入bundle.*.js文件名称，执行替换即可汉化。


测试最新0.95,以及0.94均通过，未来的riot版本只要界面字符没有太大变动理论上都适用，如果riot有完整的国际化支持出来了，这个脚本就没用了。


android手机客户端翻译，全部完成

在\vector\src\main\res 下新建 values-zh-rCN 目录，将array.xml以及strings.xml放入该文件夹中，编译打包即可。
目前更新到0.6.6
