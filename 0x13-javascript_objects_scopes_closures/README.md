# 0x13. JavaScript - Objects, Scopes and Closures

![Make file gif](./t/giphy-2.gif)

> This project was on ...
`JavaScript`

## Background Context

### Object Destructuring

[The Cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet?tab=readme-ov-file#destructuring-objects-and-arrays)

```javascript
const person = {
  firstName: "Nick",
  lastName: "Anderson",
  age: 35,
  sex: "M"
}
```

```javascript
const { firstName: first, age, city = "Paris" } = person; // That's it !

console.log(age) // 35 -- A new variable age is created and is equal to person.age
console.log(first) // "Nick" -- A new variable first is created and is equal to person.firstName
console.log(firstName) // ReferenceError -- person.firstName exists BUT the new variable created is named first
console.log(city) // "Paris" -- A new variable city is created and since person.city is undefined, city is equal to the default value provided "Paris".
```

```javascript
const joinFirstLastName = ({ firstName, lastName }) => firstName + '-' + lastName;

joinFirstLastName(person); // "Nick-Anderson"
```

### Array Destructuring

```javascript
const myArray = ["a", "b", "c"];

const [x, y] = myArray; // That's it !

console.log(x) // "a"
console.log(y) // "b"
```

### I learnt about

- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What `this` means
- What `undefined` means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Requirements

### General

- Allowed editors: `v`i, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`

## MORE INFO

### Install Node 14

```terminal
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semi-standard

[StandardJS Documentation](https://standardjs.com/rules.html)

[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

[![js-semistandard-style](https://raw.githubusercontent.com/standard/semistandard/master/badge.svg)](https://github.com/standard/semistandard)

```terminal
 sudo npm install semistandard --global
```

## Environment

- Language: JavaScript, NodeJS
- OS: Ubuntu 20.04 LTS
- Interpreter: Node 14.x
- Style guidelines: [semistandard 16.x.x](https://github.com/standard/semistandard) and [AirBnB style](https://github.com/airbnb/javascript)

## Files

- 0-rectangle.js
- 1-rectangle.js
- 2-rectangle.js
- 3-rectangle.js
- 4-rectangle.js
- 5-square.js
- 6-square.js
- 7-occurrences.js
- 8-esrever.js
- 9-logme.js
- 10-converter.js

> Each file contains the solution to a task in the project.

<!-- markdownlint-disable-next-line -->
#### Credits

Work is owned and maintained by [Michael C. Iyke](https://github.com/michaeliyke).

## Acknowledgement

All work contained in this project was completed as part of the curriculum for Alx. ALX is a leading technology training provider, built to accelerate the careers of young Africans through the technology and professional skills that enable them to thrive in the digital economy. The program prepares students for careers in the tech industry using project-based peer learning. For more information, [visit](https://www.alxafrica.com/).
