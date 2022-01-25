
## python 之禅
命令行输入`import this`可以看到

* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

## 我的
使用变量太长，可以使用临时变量存储，再使用这个临时变量，即一个语句太长，影响阅读，可以拆分之后再组建。

## 函数编写指南
应给函数指定描述性名称，且只在其中使用小写字母和下划线，给模块命名时也应遵循上述约定。

每个函数都应包含简要地阐述其功能的注释。该注释应紧跟在函数定义后面，并采用文档字符串格式

给形参指定默认值时，等号两边不要有空格，对于函数调用中的关键字实参，也应遵循这种约定

所有import 语句都应放在文件开头。唯一例外的情形是，在文件开头使用了注释来描述整个程序

## 类编码风格
类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。

对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能

每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述

在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类

需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import 语句