
## if
if 语句的核心都是一个值为True 或False 的表达式，这种表达式称为条件测试(别名**条件表达式或布尔表达式**），根据条件测试的值为True 还是False 来决定是否执行if 语句中的代码

格式`if if_expression:`（注意冒号），在if 语句中，缩进的作用与在for 循环中相同。如果测试通过了，将执行if 语句后面所有缩进的代码行，否则将忽略它们。
Python提供的if-else 语句。if-else 语句块类似于简单的if 语句，但其中的else 语句让你能够指定条件测试未通过时要执行的操作
检查超过两个的情形，为此可使用Python提供的if-elif-else 结构

```python
if if_expression:
    # if_block

if if_expression:
    # if_block
else
    # else_if_block

if if_expression:
    # if_block
elif elif_expression:
    # else_if_block
# 可以使用多个代码块
else
    # else_block

```
* Python并不要求if-elif 结构后面必须有else 代码块。在有些情况下，else 代码块很有用；而在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰。else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的代码就会执行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif 代码块来代替else 代码块


* 在Python中检查是否相等时区分大小写
* `== !=`
* 数值比较 `> >= < <=`
* 一个等号是陈述，两个等号是判断是否相等


* 检查多个条件 `and or`

* PEP 8提供的唯一建议是，在诸如== 、>= 和<= 等比较运算符两边各添加一个空格。空格不会影响Python对代码的解读，而只是让代码阅读起来更容易。

* 检查特定值是否包含在列表中 使用关键字in `item_value/item_varable in list`
* 检查特定值是否不包含在列表中 使用关键字 not in `item_value/item_varable  not in list`