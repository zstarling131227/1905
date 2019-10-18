## pandas基础

### pandas介绍

1. pandas.cut用来把一组数据分割成离散的区间。比如有一组年龄数据，可以使用pandas.cut将年龄数据分割成不同的年龄段并打上标签。

原型
pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise') #0.23.4
参数含义
x：被切分的类数组（array-like）数据，必须是1维的（不能用DataFrame）；
bins：bins是被切割后的区间（或者叫“桶”、“箱”、“面元”），有3中形式：一个int型的标量、标量序列（数组）或者pandas.IntervalIndex 。

一个int型的标量
当bins为一个int型的标量时，代表将x平分成bins份。x的范围在每侧扩展0.1%，以包括x的最大值和最小值。
标量序列
标量序列定义了被分割后每一个bin的区间边缘，此时x没有扩展。
pandas.IntervalIndex
定义要使用的精确区间。
right：bool型参数，默认为True，表示是否包含区间右部。比如如果bins=[1,2,3]，right=True，则区间为(1,2]，(2,3]；right=False，则区间为(1,2),(2,3)。
labels：给分割后的bins打标签，比如把年龄x分割成年龄段bins后，可以给年龄段打上诸如青年、中年的标签。labels的长度必须和划分后的区间长度相等，比如bins=[1,2,3]，划分后有2个区间(1,2]，(2,3]，则labels的长度必须为2。如果指定labels=False，则返回x中的数据在第几个bin中（从0开始）。
retbins：bool型的参数，表示是否将分割后的bins返回，当bins为一个int型的标量时比较有用，这样可以得到划分后的区间，默认为False。
precision：保留区间小数点的位数，默认为3.
include_lowest：bool型的参数，表示区间的左边是开还是闭的，默认为false，也就是不包含区间左部（闭）。
duplicates：是否允许重复区间。有两种选择：raise：不允许，drop：允许。

返回值
out：一个pandas.Categorical, Series或者ndarray类型的值，代表分区后x中的每个值在哪个bin（区间）中，如果指定了labels，则返回对应的label。
bins：分隔后的区间，当指定retbins为True时返回。




2. 

