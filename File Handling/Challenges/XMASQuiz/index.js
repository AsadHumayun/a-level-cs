const { writeFile } = require("fs");
const { createInterface } = require("readline");
const delay = require("delay");

const start = Date.now();
const rl = createInterface({
	input: process.stdin,
	output: process.stdout,
});

const config = require("./config.json");
const questions = Object.entries(config.questions);

const sanitize = (input) => input.replace(/[%]|[&]|[{]|[}]|[\\]|[<]|[>]|[*]|[?]|[$]|[!]|[']|["]|[:]|[@]|[+]|[`]|[|]|[|]|[=]/gm, "");

console.log("WELCOME TO THE XMAS QUIZ!\n\nPlease note that questions' answers are, indeed, not case-sensitive.");
var id = "";
const write = [];

write.push(`[${new Date().toISOString()}]: Attempting to get this dude\'s username...`);
rl.question(`Please enter a unique player identification string.\nThis is used as a filename for a log file that'll be created, with all of your questions and answers on them. It will be a normal text file, found in the ${process.cwd()}/logs folder.`, (ans) => {
	ans = sanitize(ans);
	if (config.disallowedUsernames.includes(ans.toLowerCase())) {
		console.log(`That username is invalid. A username may not be one of: [${config.disallowedUsernames.join(", ")}]`);
		process.exit(0);
	}
	else {
		console.clear();
		console.log(`Welcome, ${ans}!`);
		id = ans;
		write.push(`[${new Date().toISOString()}]: Successfully updated String id from null to "${id}"`);
	}
});

// eslint-disable-next-line no-var
var score = 0;
let EOQ = false;
write.push(`[${new Date().toISOString()}]: Starting quiz....`);
// have to use an async wrapper here, due to the functions involved being async.
(async () => {
	for (const q of questions) {
    write.push(`[${new Date().toISOString()}]: rl<ReadlineInterface>.question<String, callback(ans, ?err)>`);
		rl.question(q[0], (ans) => {
		write.push(`[${new Date().toISOString()}]: rl.question<[Q: "${q[0]}"]>`);
			if (questions.indexOf(q) + 1 === questions.length) EOQ = true;
			if (ans.toLowerCase() === q[1].toString()) {
				console.log("You got the answer correct!\nMoving onto the next question in 10 seconds...");
				score++;
        write.push(`[${new Date().toISOString()}]: Question answered correctly; updating scr...`);
        write.push(`[${new Date().toISOString()}]: ${score}`);
				return;
			}
			else {
        write.push(`[${new Date().toISOString()}]: Unexpected response ""; question marked as incorrect.\n${id}.scr<Number<${score}>> was not updated.`);
				console.log(`Sorry, but you got the question wrong...\nThe correct answer was: "${q[1]}". Better luck next time?`);
			}
		});
		if (EOQ) {
		write.push(`[${new Date().toISOString()}]: EOQ\nFinal score: ${score}. Time taken: ${Date.now() - start} ms.`);
			console.clear();
			console.log(`That's all the questions done!\nYour score was... ${score}/${questions.length}!`);
		}
		else {
			await delay(10000);
			console.clear();	
		}
	}
	write.push(`[${new Date().toISOString()}]: (interface (readline)): closing instance...`);
	rl.close();
	write.push(`[${new Date().toISOString()}]: Closed readline instance.`);
	writeFile(`./logs/${id}.txt`, write.join("\n"), (e) => console.error(e));
	process.exit(0);
})();