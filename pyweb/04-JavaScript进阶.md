# JavaScript 进阶

## 1. 对象的属性

多属性数据类型：可用于代替 switch

### 1.1. 属性访问

```javascript
// 访问属性
var testObj = {
  hat: 'ballcap',
  shirt: 'jersey',
  shoes: 'cleats',
};
var hatValue = testObj.hat;
var shirtValue = testObj.shirt;
```

```javascript
// 访问含有空格对属性
var testObj = {
  'an entree': 'hamburger',
  'my side': 'veggies',
  'the drink': 'water',
};
var entreeValue = testObj['an entree'];
var drinkValue = testObj['the drink'];
```

```javascript
// 复合变量
var myPlants = [
  {
    type: 'flowers',
    list: ['rose', 'tulip', 'dandelion'],
  },
  {
    type: 'trees',
    list: ['fir', 'pine', 'birch'],
  },
];

var secondTree = myPlants[1].list[1];
```

### 1.2. 属性更改

```javascript
var testObj = {
  12: 'Namath',
  16: 'Montana',
  19: 'Unitas',
};

var playerNumber = 16;
var player = testObj[playerNumber];

// 删除
delete testObj.playerNumber;
```

```javascript
// 冻结
let obj = {
  name: 'FreeCodeCamp',
  review: 'Awesome',
};
Object.freeze(obj);
obj.review = 'bad'; // will be ignored. Mutation not allowed
obj.newProp = 'Test'; // will be ignored. Mutation not allowed
```

### 1.3. 方法、查询

```javascript
let duck = {
  name: 'Aflac',
  numLegs: 2,
  sayName: function () {
    return 'The name of this duck is ' + this.name + '.';
  },
};
duck.sayName();

// 属性查询
obj.hasOwnProperty(checkProp);

// 键查询
Object.keys(obj);
```

## 2. 对象的构造

### 2.1. 访问器

```javascript
// 属性
class Thermostat {
  constructor(fahrenheit) {
    // _表示私有变量
    this._fahrenheit = fahrenheit;
  }
  // getter
  get temperature() {
    return (5 / 9) * (this._fahrenheit - 32);
  }
  // setter
  set temperature(celsius) {
    this._fahrenheit = (celsius * 9.0) / 5 + 32;
  }
}

const thermos = new Thermostat(76);
let temp = thermos.temperature; // 24.44 in Celsius
thermos.temperature = 26;
temp = thermos.temperature; // 26 in Celsius
```

### 2.2. 构造器

```javascript
// 函数构造器
function Dog(name, color) {
  this.name = name;
  this.color = color;
  this.numLegs = 4;
}

let terrier = new Dog('a', 'red');

// 遍历属性
let ownProps = [];
let prototypeProps = [];

for (let property in terrier) {
  if (terrier.hasOwnProperty(property)) {
    ownProps.push(terrier);
  } else {
    prototypeProps.push(property);
  }
}

// 检查对象
function joinDogFraternity(candidate) {
  if (candidate.constructor === Dog) {
    return true;
  } else {
    return false;
  }
}

// 类构造器
class SpaceShuttle {
  constructor(targetPlanet) {
    this.targetPlanet = targetPlanet;
  }
}
const zeus = new SpaceShuttle('Jupiter');
```

### 2.3. 原型继承

```javascript
// 实例、原型
terrier instanceof Dog;
Dog.prototype.isPrototypeOf(terrier);
Object.prototype.isPrototypeOf(Dog.prototype);

// 原始属性
Dog.prototype.numLegs = 2;

// 继承
Dog.prototype = {
  constructor: Dog, // Solution
  numLegs: 4,
  eat: function () {
    console.log('nom nom nom');
  },
  describe: function () {
    console.log('My name is ' + this.name);
  },
};

// 继承 2
function Animal() {}

Animal.prototype = {
  constructor: Animal,
  eat: function () {
    console.log('nom nom nom');
  },
};

function Dog() {}

Dog.prototype = Object.create(Animal.prototype);

let beagle = new Dog();
beagle.eat(); // Should print "nom nom nom"

// 重置
Dog.prototype.constructor = Dog;
// 添加方法
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;
Dog.prototype.bark = function () {
  console.log('Woof!');
};
```

### 2.4. 共享、闭包

对于不相关的对象，最好使用 `mixins` 。 `mixin` 允许其他对象使用功能集合。

```javascript
let bird = {
  name: 'Donald',
  numLegs: 2,
};

let boat = {
  name: 'Warrior',
  type: 'race-boat',
};

let glideMixin = function (obj) {
  obj.glide = function () {
    console.log('Gliding!');
  };
};

glideMixin(bird);
glideMixin(boat);

// 闭包：免于外部修改
function Bird() {
  let weight = 15;

  this.getWeight = function () {
    return weight;
  };
}
```

### 2.5. IIFE

若函数没有名称，也没有存储在变量中。函数表达式末尾的两个括号 `()` 使其立即被执行或调用。这种模式被称为立即执行函数表达式（Immediately Invoked Function Expression，IIFE）。

```javascript
(function () {
  console.log('Chirp, chirp!');
})();

// 模块
let funModule = (function () {
  return {
    isCuteMixin: function (obj) {
      obj.isCute = function () {
        return true;
      };
    },
    singMixin: function (obj) {
      obj.sing = function () {
        console.log('Singing to an awesome tune');
      };
    },
  };
})();
```

### 2.6. Promise

```javascript
const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer is set to true to represent a successful response from a server
  let responseFromServer = true;

  if (responseFromServer) {
    resolve('We got the data');
  } else {
    reject('Data not received');
  }
});

makeServerRequest.then((result) => {
  console.log(result);
});

const makeServerRequest = new Promise((resolve, reject) => {
  // responseFromServer is set to false to represent an unsuccessful response from a server
  let responseFromServer = false;

  if (responseFromServer) {
    resolve('We got the data');
  } else {
    reject('Data not received');
  }
});

makeServerRequest.then((result) => {
  console.log(result);
});

makeServerRequest.catch((error) => {
  console.log(error);
});
```

## 3. 函数式编程

函数式程序设计是一种程序设计风格，其解决方案是简单的、孤立的函数，在函数范围之外没有任何副作用。

- 孤立的函数，对程序的状态没有依赖性，其中包括全局变量的变化；
- 纯函数，同样的输入总是有同样的输出；
- 函数副作用有限，对函数之外的程序状态的任何改变或突变都会被仔细控制；

### 3.1. 命令式、声明式

```javascript
// 命令式
var array = [1, 2, 3];
for (let i = 0; o < array.length; i++) {
  console.log(array[i]);
}
// 声明式
var array = [1, 2, 3];
array.forEach((elememt) => console.log(elememt));
```

### 3.2. curry

柯里化：把一个多参数函数变换为一个嵌套的一元函数的过程。

```javascript
// 常见多参数函数
const add = (x, y) => x + y;
// 柯里化
const addCurried = (x) => (y) => x + y;
addCurried(2)(3);
// 调用
const add = (x, y) => x + y;
let autoCurried = curry(add);
autoCurried(2)(3); //5
```

### 3.3. 原型

```javascript
var s = [23, 65, 98, 5];

Array.prototype.myMap = function (callback) {
  var newArray = [];
  this.forEach((a) => newArray.push(callback(a)));
  return newArray;
};

var new_s = s.myMap(function (item) {
  return item * 2;
});
```
