const readline = require("readline");
const fs = require("fs");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

/**
 * Splits one source array into multiple derivative sub arrays.
 * @param {Array<any>} list The source array of which elements are derivative.
 * @param {Number} elementsPerSubArray Number of elements to be present in each subArray.
 * @returns {Array<Array>} Divided array derivative of original array
 * @private @static
*/
function mtx(list, elementsPerSubArray) {
    let matrix = [], i, k;
    for (i = 0, k = -1; i < list.length; i++) {
        if (i % elementsPerSubArray === 0) {
            k++;
            matrix[k] = [];
        };
        matrix[k].push(list[i]);
    };
    return matrix;
};

/**
 * Appends supplied data to a file.
 * Data will be taken via an RL stream through stdin.
 * Must be in form `name;score;name0;score0` etc
 * @alias <> acts as the append function too because it does this by default.
 */
function saveToFile() {
    let data;
    rl.question("Please enter the student data - in format name;score;name;score;name;score etc: ", (ans) => {
        if (ans.split(";").length <= 0 || (ans.split(";").length % 2 != 0)) throw TypeError("Invalid data inputted");
        s = Date.now();
        stream = fs.createWriteStream("data.txt", { flags: "a" });
        cntnt = fs.readFileSync("./data.txt", { encoding: "utf-8" });
        cntnt = cntnt.split(";");
        stream.write(`${cntnt.length >= 1 ? ";" + ans : ans}`);
        stream.end();
        console.log(`Successfully appended data "${cntnt.length >= 1 ? ";" + ans : ans}" to file ${process.cwd() + "/data.txt"} in ${Date.now() - s} ms.`)
        console.log("Terminating  programme...")
        rl.close(); //terminates rl stream and kills the programme
    });
};

/**
 * Calculates the average score from the scores found from the text file.
 * @returns {Number} `avg` - Average score
 */
function calculateAverage() {
    let data = fs.readFileSync("./data.txt", { encoding: "utf-8" });
    console.log(data);
    data = mtx(data.split(";"), 2);
    total = (data.map((f) => Number(f[1]))).reduce((a, b) => a + b, 0);
	numRecs = data.length;
	average = total / numRecs;
	console.log(`(${data.map((d) => d[1]).join("+")})/${numRecs}: ${average}`);
    rl.close();
};

/**
 * Displays every single score of a student from the text file. For an average please use the other functions in this document.
 * No parameters are required for this function; just the existence of the file is required.
 */
function displayData() {
    data = fs.readFileSync("./data.txt", { encoding: "utf-8" });
    if (!data) {
        console.log("<No entries found>.");
        rl.close();
    };
    data = mtx(data.split(";"), 2);
    console.log("ALL ENTRIES:");
    console.log(data.map((f) => `${f[0]}: ${f[1]} marks`).join(";\n"));
    rl.close();
};

console.log("1. Input data and save to new file\n2. Input data and append to existing file\n3. Calculate and display average mark\n4. Display data\n5. Quit");
rl.question("Please enter your choice: ", (ans) => {
    console.log(`Input captured: ${ans}`);
    opts = [[1, saveToFile], [2, saveToFile], [3, calculateAverage], [4, displayData], [5, rl.close]];    
    opts[opts.findIndex((f) => f[0] == Number(ans))][1](); //find and execute correct function
});