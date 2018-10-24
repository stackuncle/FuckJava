# int和Integer

## int与Integer的基本使用对比
1. Integer是int的包装类；int是基本数据类型
1. Integer变量必须实例化后才能使用；int变量不需要
1. Integer实际是对象的引用，指向此new的Integer对象；int是直接存储数据值
1. Integer的默认值是null；int的默认值是0
1. 泛型定义时也不支持int: 如：`List<Integer> list = new ArrayList<Integer>();`可以，而`List<int> list = new ArrayList<int>();`则不行