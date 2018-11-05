# int和Integer

int 是我们常说的整形数字，是 Java 的 8 个原始数据类型（Primitive Types，boolean、byte 、short、char、int、float、double、long）之一。Java 语言虽然号称一切都是对象，但原始数据类型是例外。

Integer 是 int 对应的包装类，它有一个 int 类型的字段存储数据，并且提供了基本操作，比如数学运算、int 和字符串之间转换等。在 Java 5 中，引入了自动装箱和自动拆箱功能（boxing/unboxing），Java 可以根据上下文，自动进行转换，极大地简化了相关编程。

关于 Integer 的值缓存，这涉及 Java 5 中另一个改进。构建 Integer 对象的传统方式是直接调用构造器，直接 new 一个对象。但是根据实践，我们发现大部分数据操作都是集中在有限的、较小的数值范围，因而，在 Java 5 中新增了静态工厂方法 valueOf，在调用它的时候会利用一个缓存机制，带来了明显的性能改进。按照 Javadoc，这个值默认缓存是 -128 到 127 之间。

## int与Integer的基本使用对比
1. Integer是int的包装类；int是基本数据类型
1. Integer变量必须实例化后才能使用；int变量不需要
1. Integer实际是对象的引用，指向此new的Integer对象；int是直接存储数据值
1. Integer的默认值是null；int的默认值是0
1. 泛型定义时也不支持int: 如：`List<Integer> list = new ArrayList<Integer>();`可以，而`List<int> list = new ArrayList<int>();`则不行