// 1 find the missing element in array
var arr = [5, 7, 9, 11, 15, 17];

const missArrElm = (arr) => {
  const result = [];
  const lastElm = arr.slice(-1);

  for (let item = arr[0]; item < lastElm; item++) {
    if (item % 2 !== 0) {
      !arr.includes(item) && result.push(item);
    }
  }
  return result;
};
console.log(missArrElm(arr));
// -----------------------------------------
// 2 find how many repeated element in array
var array = [1, 2, 1, 1, 1];

const howMnyTime = array.reduce((acc, item) => {
  acc[item] = ++acc[item] || 1;
  return acc;
}, {});

console.log(howMnyTime);

// ----------------------------------------------
// 4 find  the unique value in array
const array = ["a", "b", "c", "b", "c", "a"];

const newElment = [];

array.forEach((element) => {
  if (!newElment.includes(element)) {
    newElment.push(element);
  }
});
console.log(newElm);

// -------------------------------------
function getValue() {
  const input = document.getElementsByClassName("Input")[0];
  const show = document.getElementById("showInput");
  show.innerText = input.value;
  console.log(input.value);
}

const btn_action = document.querySelector(".action button");
const getList = document.querySelector(".feature");

btn_action.addEventListener("click", function () {
  const getList = document.querySelector(".feature");
  const newList = document.createElement("li");
  newList.innerHTML = "tution";
  getList.appendChild(newList);
});

getList.addEventListener("dblclick", function (event) {
  event.target.remove();
});

// ----------------------------------------------
for (let index = 0; index < 3; index++) {
  const log = () => {
    console.log(i);
  };
  setTimeout(log, 100);
}
// -----------------------------------
console.log("one");

setTimeout(() => {
  console.log("two");
}, 0);

Promise.resolve().then(() => {
  console.log("three");
});

console.log("four");

// ------------------------------------------

function abc() {
  if (1) {
    var a = 5;
    let b = 8;
    const c = 9;
  }
  console.log(a);
  console.log(b);
  console.log(c);
}

abc();

// --------------------------------------------

var a = "42";
var b = 42;

console.log(a == b);

console.log(a === b);
// ------------------------------------
// 7 Shuffling array

const list = [5, 2, 3, 6, 1, 8];
console.log(
  list.sort(() => {
    const random = Math.random();
    return random - 0.5;
  })
);

const arr = [1, 2, 3, 5, 4, 6];
var num = Math.trunc(Math.random() * 6);
console.log(arr[num]);
// ------------------------------------------------
// 8 sort array in object

let employee = [
  { id: 1, emp: "malik", dep: "it" },
  { id: 2, emp: "zain", dep: "cs" },
  { id: 3, emp: "bilal", dep: "se" },
  { id: 4, emp: "haris", dep: "art" },
];

let employe = employee.sort((a, b) => {
  if (a.emp < b.emp) {
    return -1;
  } else {
    return 1;
  }
});

for (const name of employe) {
  console.log(name.emp);
}
// -------------------------------------------
// 9 find the second largest num in array...
const input = [1, 3, -2, 7, 5, 1];
const newsort = [...new Set(input)].sort((a, b) => a - b);
const seclargest = newsort[newsort.length - 2];
console.log(seclargest);

// ----------------------------------------
// 10 find the array length without length method..
let arr = [1, 4, 7, 3, 4, 2];

let myfunc = (arr) => {
  let length = 0;
  while (arr[length] !== undefined) {
    length++;
    //arr[length] !== 'undefined' // 1
  }
  return length;
};
console.log(myfunc(arr));
//  --------------------------------------------
// 11 find the avgerage in array..
//with reduce
const arr = [4, 7, 12, 4, 2];
const sum = arr.reduce((acc, value) => {
  return acc + value;
});
console.log(sum / arr.length);
//------- without reduce
let sumval = 0;
for (let index = 0; index < arr.length; index++) {
  sumval += arr[index];
}
console.log(sumval);
// ----------------------------------------
// 12 find the even/odd number in array..
const arr = [1, 2, 3, 4, 5, 6];
let evenArr = [];
let oddArr = [];
const even_odd = arr.map((element) => {
  if (element % 2 == 0) {
    evenArr.push(element);
  } else {
    oddArr.push(element);
  }
});
console.log(`${evenArr} this is even`);
console.log(`${oddArr} this is odd`);
// -----------------------------------------------
// 12 reverse array without method..
const arr = [1, 2, 3, 4, 5];
let reverseArr = [];
for (let i = arr.length; i > 0; i--) {
  reverseArr.push(i);
}
console.log(reverseArr);
// ----------------
// 13 reverse string without method
var string = "greeting";
let reverse = "";

for (let i = string.length - 1; i >= 0; i--) {
  reverse += string[i];
}
console.log(reverse);
//  -----------------------------------------
const arr = [1, 4, 7, 8, 9, 10];
let newArr = [4, 8];
let newone = arr.filter((element) => !newArr.includes(element));
console.log(newone);
// -----------------------------------------------

console.log(2 + 9 + "1" + " 4");

//------------------------------------------
const string = prompt("enter your string");
let vowels = ["a", "e", "i", "o", "u"];
var count = 0;
for (let i = 0; i < string.length; i++) {
  if (vowels.includes(string[i])) {
    count++;
  }
}
console.log(count);
// ---------------------------------------------------
// 14  find factorial number-----
var user = prompt("enter any number for foctoial");
let fact = 1;
if (user < 0) {
  console.log(`${user} is not foctorial number`);
} else {
  for (let i = 1; i <= user; i++) {
    fact = fact * i;
  }
  console.log(`${user} is  foctorial ${fact}`);
}
// ----------------------------------------------------
var num1 = 2;
var num2 = 1;
[num1, num2] = [num2, num1];
console.log(`${num1} ,  ${num2}`);
// ----------------------------------------------------
// star--------

for (let i = 0; i < 5; i++) {
  var str = "";
  for (let j = 5; j > i; j--) {
    str += "-";
  }
  for (let k = 0; k <= i; k++) {
    str += "*";
  }
  for (let n = 1; n <= i; n++) {
    str += "*";
  }
  console.log(str);
}
// Sidha Loop..
for (let i = 0; i <= 5; i++) {
  for (let j = 1; j <= i; j++) {
    document.write("* ");
  }
  document.write("<br/>");
}
// Ulta Loop
for (let i = 5; i >= 0; i--) {
  for (let j = 1; j <= i; j++) {
    document.write("*");
  }
  document.write("<br/>");
}

// -------------------------------------
// 15 find intersection.......
var arr1 = [1, 2, 4, 5, 7, 4, 5, 3, 4];
var arr2 = [2, 4, 6, 5, 3];

const intersection = arr1.filter((element) => {
  return arr2.includes(element);
});

console.log(intersection);

// -------------------------------------------
function sum() {
  let count = 0;
  for (let i = 0; i < arguments.length; i++) {
    count += arguments[i];
  }
  console.log(count);
}
sum(5, 7, 8, 9, 4, 2);
// ---------------------------------------------

const car = {
  Name: "HondaCity",
  colour: "black",
  fuel: -1,
  drive: function () {
    if (this.colour === "black") {
      console.log("Your Car");
    } else {
      console.log("Not Your Car");
    }
  },
};

car.drive();
console.log(car.Name);
// --------------------------------------------------
const arr = ["pizza", "overloaded", "burger"];

const num = Math.trunc(Math.random() * 3);
console.log(arr[num]);
// ---------------------------------------------------
function createStudent(firstName, lastName) {
  let student1 = {
    firstName: firstName,
    lastName: lastName,
  };
  return student1;
}
console.log(createStudent("hassan", "qadir"));
//  ------------------------------------------------
function myFunction(firstName, lastName) {
  console.log(this);
}
myFunction("hassan", "qadir");
// ------------------------------------------
let sum = () => {
  console.log("my name is hassan");
};
setTimeout(sum(), 2000);
//-------
let myFun = (a, b) => {
  let sum = a + b;
  return sum;
};
// ----
let fun1 = (a, b) => {
  return a + b;
};
console.log(setTimeout(fun1(5, 4), 2000));
// ----------------------------------
// Rest Operator.....
function sum(...a) {
  let count = 0;
  for (let i = 0; i < a.length; i++) {
    count += a[i];
  }
  return count;
}
console.log(sum(4, 5, 6, 7));
// --------------------------------------
var obj = [
  { Id: 1, fName: "Hassan", lName: "Qadir", age: 25, field: "ComputerScience" },
  { Id: 2, fName: "Hassan", lName: "Qadir", age: 27, field: "ComputerScience" },
  { Id: 2, fName: "Hassan", lName: "Qadir", age: 20, field: "ComputerScience" },
  { Id: 2, fName: "Hassan", lName: "Qadir", age: 30, field: "ComputerScience" },
];
var obj2 = [];
for (let i = 0; i < obj.length; i++) {
  if (obj[i].age > 23) {
    obj2.push(obj[i]);
  }
}
//  console.log(obj2);
// -------------------------------
// 16 higher order function and clouser..
function outerFun(x) {
  let innerFun = (y) => {
    return x + y;
  };
  return innerFun;
}
let innerFun = outerFun(5);
console.log(innerFun(6));
// --------------------------------------------
// Not reuseability Normal Fuction thats why call and apply introduce..
// when we use call method object with function attachment then any type of parameters pass..
// when we use apply method object with function attachment then only array  parameters pass..
// The call, bind and apply methods can be used to set the this keyword independent of how a function is called.The bind method creates a copy of the function and sets the this keyword, while the call and apply methods sets the this keyword and calls the function immediately.

let obj1 = {
  fname: "hassan",
  lname: "qadir",
  age: 25,
};
let obj2 = {
  fname: "zain",
  lname: "qadir",
  age: 24,
};
function nameFun() {
  return `${this.fname}${this.lname}`;
}
console.log(obj2);
console.log(obj2.nameFun.call(obj1));
// -------------------------------------------------------------------------------------
var data = Promise.race([
  new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("hassan");
    }, 4000);
  }),
  new Promise((resolve, reject) => {
    setTimeout(() => {
      reject("hassan + zain");
    }, 2000);
  }),
  new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("hassan");
    }, 3000);
  }),
]);

data
  .then((item) => {
    console.log(item);
  })
  .catch((err) => {
    console.log(`this is ${err}`);
  });

// ------------------------------------

let user = {
  getName: function () {
    return `${this.fname},${this.lname}`;
  },
  getBirth: function () {
    let age = new Date().getFullYear() - this.birth;
    return age;
  },
};
let user1 = {
  fname: "hassan",
  lname: "qadir",
  birth: 2000,
  getBirth: user.getBirth,
};
user1.__proto__ = user;
console.log(user1.getBirth());
console.log(user1);

// my own prototype..
Object.prototype.myApp = function getAge() {
  let age = new Date().getFullYear() - this.birth;
  return age;
};
let user3 = {
  nameFun: function () {
    return `${this.fname},${this.lname}`;
  },
};
let user1 = {
  fname: "Zain",
  lname: "qadir",
  birth: 1998,
};

var user2 = {
  fname: "hassan",
  lname: "qadir",
  birth: 1997,
};

user1.__proto__ = user3;
console.log(user1.nameFun());
//  ----------------------------------------
// Deep Copy and shallow copy..
let user1 = {
  fname: "hassan",
  lname: "qadir",
};

let user2 = { ...user1 }; //Shallow copy..
user2.fname = "zain";
let user2 = JSON.parse(JSON.stringify(user1)); //Deep copy..
user2.fname = "zain";
console.log(user1);
console.log(user2);
// ------------------------
// Clousure....
function mostOuter() {
  let b = 20;
  return function outerFun() {
    let a = 100;
    return function nameFun() {
      return a + b;
    };
  };
}

let outerFun = mostOuter();
let nameFun = outerFun();
console.log(nameFun());
// --------------------------------
let obj = [
  {
    fname: "hassan",
    lname: "qadir",
  },
];
for (let item of obj) {
  console.log(item);
}

let data = new Map([["name", "hassan"]]);

console.log(data);
// -----------------------------------------------------

let arr = [3, 6, 8, 19, 36, 75, 36, 91, 76, 10, 94, 97];
let min = arr[0];
let max = arr[0];

for (let i = 1; i < arr.length; i++) {
  if (arr[i] < min) {
    min = arr[i];
  }
  if (arr[i] > max) {
    max = arr[i];
  }
}
console.log(min);
console.log(max);
// ----------------------------------------
let child = document.getElementById("child");
let parent = document.getElementById("parent1");

child.addEventListener("click", shape1);
parent.addEventListener("click", shape2);
document.body.addEventListener("click", shape3);

function shape1(e) {
  e.stopPropagation();
  console.log("btn");
}

function shape2() {
  console.log("div");
}

function shape3() {
  console.log("body");
}
// ----------------------------------------
// 17 Merging without subread Operator
let arr1 = [2, 4, 6, 8, 9, 15, 45, 76, 32];
let arr2 = [6, 7, 3, 9, 10, 15];
let arr3 = [];

for (let i = 0; i < arr1.length; i++) {
  arr3[i] = arr1[i];
}

for (let i = 0; i < arr2.length; i++) {
  arr3[arr1.length + i] = arr2[i];
}
console.log(arr3);
// -----------------------------------------
// 18 Remove amy element in array
let arr = [1, 3, 4, 5, 6, 7, 8, 9];
var postion = 4;
for (let i = postion; i < arr.length - 1; i++) {
  arr[i] = arr[i + 1];
}
arr.length = arr.length - 1;
console.log(arr);
//   -------------------------------
// 19 insert array without subred operator
let arr = [1, 3, 5, 7, 8, 9];
var postion = 2;
let newElm = 6;

for (let i = arr.length - 1; i >= postion; i--) {
  arr[i + 1] = arr[i];
  arr[i] = newElm;
}
console.log(arr);

// -------------------------------------
let textBox = document.getElementById("search");
let div = document.getElementById("result");
fetch("https://jsonplaceholder.typicode.com/users")
  .then((res) => res.json())
  .then((users) => showUser(users));
function showUser(users) {
  let ul = document.createElement("ul");
  for (const user of users) {
    let li = document.createElement("li");
    li.innerText = user.name;
    ul.appendChild(li);
    div.appendChild(ul);
  }
}
textBox.oninput = filter;

function filter() {
  let getli = document.querySelectorAll("li");
  for (const li of getli) {
    let current = li.innerText.toLowerCase();
    let searchText = this.value.toLowerCase();
    if (!current.includes(searchText)) {
      li.setAttribute("hidden", true);
    } else {
      li.removeAttribute("hidden");
    }
  }
}
// ----------------------------------------
let arr = [1, 2, 4, 6, 1, 6, 3, 1, 9, 8];
let count = [];

for (let i = 0; i < arr.length; i++) {
  let num = arr[i];
  if (count[num]) {
    count[num] += 1;
  } else {
    count[num] = 1;
  }
}
console.log(count);
// -------------------------------------------
// 20 how to convert two arrays to an array of object
const keys = ["name", "born"];
const value = ["hassan", "1997"];

const print = value.map((value, i) => ({ [keys[i]]: value }));
console.log(print);
