# JavaScript 基础

## 1. 开始

### 1.1. 注释

- `//`：单行注释
- `/* */`：多行注释

### 1.2. 赋值

#### 1.2.1. let

`let` 不能更改

```javascript
'use strict';
var camper = 'James';
var camper = 'David';
console.log(camper); // logs 'David'
```

```javascript
let camper = 'James';
let camper = 'David'; // throws an error
```

#### 1.2.2. const

const 不能再次赋值，只能通过索引更新

```javascript
const s = [5, 6, 7];
s = [1, 2, 3]; // throws error
s[2] = 45;
console.log(s); //  [5, 6, 45]
```

## 2. 基本类型

- `undefined`：未定义
- `null`：空值
- `boolean`：布尔值
- `string`：字符串
- `number`：数值

### 2.1. 字符串

| 属性   |     方法      |
| ------ | :-----------: |
| length | toUpperCase() |
|        |               |

```javascript
// 索引可以取值，但不能修改值
var txt = 'Hello world!';
console.log(txt.length); // 12
console.log(txt.toUpperCase()); // HELLO WORLD!
```

```javascript
// 格式化字符串
const result = {
  success: ['max-length', 'no-amd', 'prefer-arrow-functions'],
  failure: ['no-var', 'var-on-top', 'linebreak'],
  skipped: ['no-extra-semi', 'no-dup-keys'],
};

function makeList(arr) {
  const failureItems = [];
  for (let i = 0; i < arr.length; i++) {
    failureItems.push(`<li class="text-warning">${arr[i]}</li>`);
  }
  return failureItems;
}

const failuresList = makeList(result.failure);
console.log(failuresList);
```

### 2.2. 数字

```javascript
// number，均为 64 位
var pi = 3.14;
var x = 34;
var y = 123e5;

// math
console.log(Math.round(4.7)); //5
console.log(Math.random()); //0.9370
```

### 2.3. 日期

```javascript
// date
var myDate = new Date();
myDate.setFullYear(2008, 8, 9);
var today = new Date();

if (myDate > today) {
  console.log('Today is before 9th August 2008');
} else {
  console.log('Today is after 9th August 2008');
}
```

### 2.4. 变换

```javascript
console.log(typeof 3);
console.log(typeof '3');
```

|       Column A       | Column B | Column C |
| :------------------: | :------: | :------: |
| `parseInt(str, num)` |    B1    |    C1    |
|          A2          |    B2    |    C2    |
|          A3          |    B3    |    C3    |

## 3. 容器类型

### 3.1. 数组

|    方法     |             功能             |
| :---------: | :--------------------------: |
|  `push()`   |      添加，默认最后一个      |
|   `pop()`   | 删除，无返回值，默认最后一个 |
|  `shift()`  |  删除，有返回值，默认第一个  |
| `unshift()` |       添加，默认第一个       |
|  `sort()`   |             排序             |
| `reverse()` |             反转             |
| `indexOf()` |  返回元素索引，不存在返回-1  |
|  `slice()`  |      索引切片，返回结果      |
| `concat()`  |         数组横向拼接         |
|  `join()`   |           元素拼接           |
| `splice()`  |     索引删除，返回删除项     |
| `filter()`  |        删除 False 值         |

```javascript
var myArray = [
  ['the universe', 42],
  ['everything', 101010],
];

// 索引可取值，也可修改值
myArray.push(['dog', 3]);
console.log(myArray);
var my_cars = new Array();
my_cars[0] = 'Saab';
console.log(my_cars);
```

```javascript
const numbers = [10, 11, 12, 12, 15];
const startIndex = 3;
const amountToDelete = 1;

numbers.splice(startIndex, amountToDelete, 13, 14);
console.log(numbers);
// [ 10, 11, 12, 13, 14, 15 ]
```

ES6 新的 spread 操作符允许我们轻松地将一个数组的所有元素，按顺序复制，语法简单，可读性强。

```javascript
let arr = [true, true, undefined, false, null];
let newArr = [];
newArr.push([...arr]);
// newArr equals [true, true, undefined, false, null]

let thisArray = ['sage', 'rosemary', 'parsley', 'thyme'];
let thatArray = ['basil', 'cilantro', ...thisArray, 'coriander'];
// thatArray now equals ['basil', 'cilantro', 'sage', 'rosemary', 'parsley', 'thyme', 'coriander']
```

### 3.2. Map

Map，类似于 Python 的字典

```javascript
var m = new Map([
  ['Michael', 95],
  ['Bob', 75],
  ['Tracy', 85],
]);
console.log(m.get('Michael')); // 95
console.log(m.set('Adam'), 67); // 添加新的 key-value
console.log(m.has('Adam')); // 是否存在 key 'Adam': true
console.log(m.get('Adam')); // 67
console.log(m.delete('Adam')); // 删除 key 'Adam'
console.log(m.get('Adam')); // undefined
```

### 3.3. Set

```javascript
var s = new Set([1, 2, 3]);
s.add(4);
console.log(s); // Set {1, 2, 3, 4}
s.delete(3);
console.log(s); // Set {1, 2, 4}
```

## 4. 控制流

### 4.1. if...else

| 运算符 |      功能      | 运算符 |       功能       |
| ------ | :------------: | ------ | :--------------: |
| `==`   | 相等，不要求类 | `!=`   | 不相等，不要求类 |
| `===`  | 相等，要求类型 | `!==`  |  不相等，要求类  |
| `&&`   |     逻辑与     | `\|`   |      逻辑或      |

> JS 中的 False 值有 `false` , `null` , `0` , `""` , `undefined` , 和 `NaN` 。

```javascript
// if
var x;
var time = 50;
if (time < 10) {
  x = 'Good morning';
} else if (time < 20) {
  x = 'Good day';
} else {
  x = 'Good evening';
}
console.log(x);
```

```javascript
// 条件操作符
// condition ? statement-if-true : statement-if-false;
function checkSign(num) {
  return num > 0 ? 'positive' : num < 0 ? 'negative' : 'zero';
}
```

### 4.2. switch

```javascript
function caseInSwitch(val) {
  var answer = '';
  switch (val) {
    case 1:
      return 'alpha';
      break;
    case 2:
      return 'beta';
      break;
    case 3:
      return 'gamma';
      break;
    case 4:
      return 'delta';
      break;
    default:
      // 相当于 `if` 语句中的最后一个 `else`
      return 'letter';
      break;
  }
  return answer;
}

console.log(caseInSwitch(1));
```

```javascript
// switch 合并式
function sequentialSizes(val) {
  var answer = '';
  switch (val) {
    case 1:
    case 2:
    case 3:
      return 'Low';
      break;
    case 4:
    case 5:
    case 6:
      return 'Mid';
      break;
  }
  return answer;
}

console.log(sequentialSizes(1));
```

### 4.3. for

```javascript
// for
for (var i = 0; i < 5; i++) {
  x = x + 'The number is ' + i + '<br>';
}

// for...in...
var person = { f_name: 'John', l_name: 'Doe', age: 25 };
for (x in person) {
  txt = txt + person[x];
}
```

### 4.4. while

```javascript
// while
while (i < 5) {
  x = x + 'The number is ' + i + '<br>';
  i++;
}

// do while
do {
  x = x + 'The number is ' + i + '<br>';
  i++;
} while (i < 5);
```

### 4.5. iterable

由于历史遗留问题 `for ... in` 循环遍历的实际上是对象的属性名称。一个数组实际上也是一个对象，它的每个元素的索引被视为一个属性。 `for ... of` 循环则完全修复了这些问题，它只循环集合本身的元素。

```javascript
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([
  [1, 'x'],
  [2, 'y'],
  [3, 'z'],
]);
for (var x of a) {
  // 遍历 Array
  console.log(x);
}
for (var x of s) {
  // 遍历 Set
  console.log(x);
}
for (var x of m) {
  // 遍历 Map
  console.log(x[0] + '=' + x[1]);
}
```

### 4.6. 内置循环

```javascript
// forEach
const forEach = (array, fn) => {
  for (let i = 0; i < array.length; i++) {
    fn(array[i]);
  }
};
```

```javascript
// forEachObject
const forEachObject = (obj, fn)=>{
    for(var property in obj){
        if(obj.hasOwnProperty(properity){
            fn(property, obj[property])
       })
   }
```

## 5. 函数

### 5.1. 定义

```javascript
// 定义
function displayDate() {
  console.log('time').innerHTML = Date();
  console.log('Get time');
}

// 参数
function testFun(param1, param2) {
  console.log(param1, param2);
}
```

```javascript
// 未定义
function abTest(a, b) {
  if (a < 0 || b < 0) {
    return undefined;
  }

  return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}

abTest(2, 2);
```

### 5.2. 异常

```javascript
function myFunction() {
  // try catch
  try {
    var x = console.log('demo').value;
    // throw
    if (x == '') throw 'empty';
    if (isNaN(x)) throw 'not a number';
    if (x > 10) throw 'too high';
    if (x < 5) throw 'too low';
  } catch (err) {
    var y = console.log('mess');
    y.innerHTML = 'Error: ' + err + '.';
  }
}
```

### 5.3. 箭头函数

```javascript
var myConcat = function (arr1, arr2) {
  'use strict';
  return arr1.concat(arr2);
};

// 等价于
const myConcat = (arr1, arr2) => arr1.concat(arr2);
```

### 5.4. 解构

#### 5.4.1. let

```javascript
'use strict';
let [x, [y, z]] = ['hello', ['JavaScript', 'ES6']];
console.log(x);
console.log(y);
console.log(z);
```

```javascript
'use strict';
let [, , z] = ['hello', 'JavaScript', 'ES6'];
console.log(z);
```

#### 5.4.2. const

```javascript
const HIGH_TEMPERATURES = {
  yesterday: 75,
  today: 77,
  tomorrow: 80,
};

const { today: highToday, tomorrow: highTomorrow } = HIGH_TEMPERATURES;
console.log(highToday);
console.log(highTomorrow);
```

```javascript
// 解构嵌套变量
const LOCAL_FORECAST = {
  yesterday: { low: 61, high: 75 },
  today: { low: 64, high: 77 },
  tomorrow: { low: 68, high: 80 },
};

const {
  today: { low: lowToday, high: highToday },
} = LOCAL_FORECAST;
console.log(lowToday);
console.log(highToday);
```

```javascript
// 解构对象
const stats = {
  max: 56.78,
  standard_deviation: 4.34,
  median: 34.54,
  mode: 23.87,
  min: -0.75,
  average: 35.85,
};

const half = ({ max, min }) => (max + min) / 2.0;
console.log(half(stats));
```

### 5.5. 参数

```javascript
// 可变参数
const sum = (...args) => {
  return args.reduce((a, b) => a + b, 0);
};
```

```javascript
// 拷贝
const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;
arr2 = [...arr1];
console.log(arr2);
```

```javascript
// 交换
const source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
function removeFirstTwo(list) {
  const [a, b, ...arr] = list;
  return arr;
}
```

## 6. 正则表达式

### 6.1. 测试、匹配

```javascript
// 方式 1
let testStr = 'freeCodeCamp';
let testRegex = /Code/;
let result = testRegex.test(testStr);
```

```javascript
// 方式 2
var patt1 = new RegExp('e');
var result = patt1.test('The best things in life are free'); //true
```

```javascript
// 匹配
let ourStr = 'Regular expressions';
let ourRegex = /expressions/;
ourStr.match(ourRegex); // ["expressions"]
```

### 6.2. 范围

```javascript
// 或
let petString = 'James has a pet cat.';
let petRegex = /dog|cat|bird|fish/;
let result = petRegex.test(petString);
```

```javascript
// 忽略大小写
let myString = 'freeCodeCamp';
let fccRegex = /freeCodeCamp/i;
let result = fccRegex.test(myString);
```

```javascript
// 全局匹配
let testStr = 'Repeat, Repeat, Repeat';
let repeatRegex = /Repeat/g;
testStr.match(repeatRegex); // ["Repeat", "Repeat", "Repeat"]
```

```javascript
// 分组匹配 1
let bigStr = 'big';
let bagStr = 'bag';
let bogStr = 'bog';
let bgRegex = /b[ai]g/;
bigStr.match(bgRegex); // ["big"]
bagStr.match(bgRegex); // ["bag"]
bogStr.match(bgRegex); // null
```

```javascript
// 分组匹配 2
let catStr = 'cat';
let batStr = 'bat';
let matStr = 'mat';
let bgRegex = /[a-e]at/;
catStr.match(bgRegex); // ["cat"]
batStr.match(bgRegex); // ["bat"]
matStr.match(bgRegex); // null
```

```javascript
// 非
let quoteSample = '3 blind mice.';
let myRegex = /[^aeiou0-9]/gi;
let result = quoteSample.match(myRegex);
```

### 6.3. 范围符号

| 符号 |       意义       | 符号 |    意义    |
| ---- | :--------------: | ---- | :--------: |
| \w   | 数字或字母或 `_` | \W   | \w 但反义  |
| \d   |       数字       | \D   | \d 但反义  |
| \s   |       空格       | \S   | \s 但反义  |
| +    |    一次或多次    | \*   | 零次或多次 |

```javascript
// 通配符
let humStr = "I'll hum a song";
let hugStr = 'Bear hug';
let huRegex = /hu./;
huRegex.test(humStr); // true
huRegex.test(hugStr); // true
```

```javascript
// 一次或多次出现
let difficultSpelling = 'Mississippi';
let myRegex = /s+/g;
let result = difficultSpelling.match(myRegex);
```

```javascript
// 起始
let rickyAndCal = 'Cal and Ricky both like racing.';
let calRegex = /^Cal/;
let result = calRegex.test(rickyAndCal);
```

```javascript
// 终止
let caboose = 'The last car on a train is the caboose';
let lastRegex = /caboose$/;
let result = lastRegex.test(caboose);
```

```javascript
// 限定次数
let ohStr = 'Ohhh no';
let ohRegex = /Oh{3, 6} no/;
let result = ohRegex.test(ohStr);
```

```javascript
// 符号限定次数
let sampleWord = 'astronaut';
let pwRegex = /^\D(?= \w{5})(?= \w*\d{2})/;
let result = pwRegex.test(sampleWord);
```

```javascript
// 复用
let repeatNum = '42 42 42';
let reRegex = /(\d+)\s\1\s\1/;
let result = reRegex.test(repeatNum);
```

```javascript
// 交换
let str = 'one two three';
let fixRegex = /(\w+)\s(\w+)\s(\w+)/;
let replaceText = '$3 $2 $1';
let result = str.replace(fixRegex, replaceText);
```

```javascript
// 删除
let hello = '   Hello, World!  ';
let wsRegex = /^\s+|\s+$/g;
let result = hello.replace(wsRegex, '');
```
