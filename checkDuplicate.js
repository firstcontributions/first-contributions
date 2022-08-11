const fs = require("fs");
const content = fs.readFileSync("./Contributors.md", { encoding: "utf-8" });
const contentArr = content.split("\r\n");

const contentArrLength = contentArr.length;

let hasDuplicate = false;

for (let i = 0; i < contentArrLength; i++) {
	if (contentArr.indexOf(contentArr[i], i + 1) !== -1) {
		console.log(contentArr[i]);
		hasDuplicate = true;
	}
}

console.log(hasDuplicate);

// this code will print out the duplicates in the array
