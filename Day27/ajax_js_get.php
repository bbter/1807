<?php
header('content-type:text/html;charset="utf-8"');
header('Access-Control-Allow-Origin:*');  
error_reporting(0);
//就是系统或应用程序出错时弹出的 错误报告，编程人员根据这个报告的内容可以判断是哪一段程序代码出问题了。
$username = $_GET['username'];
$age = $_GET['age'];
$password = $_GET["password"];

/*获取?后面对应健的值*/

echo "你的名字：{$username}，年龄：{$age}，密码：{$password}";?>
