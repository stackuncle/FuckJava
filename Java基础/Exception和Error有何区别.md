# Error和Exception有何区别

## Error和Exception的联系

- 继承结构：Error和Exception都是继承于Throwable，RuntimeException继承自Exception。
- Error和RuntimeException及其子类称为未检查异常（Unchecked exception），其它异常成为受检查异常（Checked Exception）。

## Error和Exception的区别

- Error类一般是指与虚拟机相关的问题，如系统崩溃，虚拟机错误，内存空间不足，方法调用栈溢出等。如java.lang.StackOverFlowError和Java.lang.OutOfMemoryError。对于这类错误，Java编译器不去检查他们。对于这类错误的导致的应用程序中断，仅靠程序本身无法恢复和预防，遇到这样的错误，建议让程序终止。

- Exception类表示程序可以处理的异常，可以捕获且可能恢复。遇到这类异常，应该尽可能处理异常，使程序恢复运行，而不应该随意终止异常。

## 运行时异常和受检查的异常

- Exception又分为运行时异常（Runtime Exception）和受检查的异常(Checked Exception )。

- RuntimeException：其特点是Java编译器不去检查它，也就是说，当程序中可能出现这类异常时，即使没有用try……catch捕获，也没有用throws抛出，还是会编译通过，如除数为零的ArithmeticException、错误的类型转换、数组越界访问和试图访问空指针等。处理RuntimeException的原则是：如果出现RuntimeException，那么一定是程序员的错误。

- 受检查的异常（IOException等）：这类异常如果没有try……catch也没有throws抛出，编译是通不过的。这类异常一般是外部错误，例如文件找不到、试图从文件尾后读取数据等，这并不是程序本身的错误，而是在应用环境中出现的外部错误。

# throw 和 throws两个关键字有什么不同

throw 是用来抛出任意异常的，你可以抛出任意 Throwable，包括自定义的异常类对象；throws总是出现在一个函数头中，用来标明该成员函数可能抛出的各种异常。如果方法抛出了异常，那么调用这个方法的时候就需要处理这个异常。

try-catch-finally-return执行顺序

1. 不管是否有异常产生，finally块中代码都会执行；
1. 当try和catch中有return语句时，finally块仍然会执行；
1. finally是在return后面的表达式运算后执行的，所以函数返回值是在finally执行前确定的。无论finally中的代码怎么样，返回的值都不会改变，仍然是之前return语句中保存的值；
1. finally中最好不要包含return，否则程序会提前退出，返回值不是try或catch中保存的返回值。

## 参考

- [《Java编程思想》](https://s.click.taobao.com/vFNU6Lw)
