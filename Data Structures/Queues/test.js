const Queue = require('./Queue.js');
const queue = new Queue(["1", "2", "3", "4"]);

console.log(queue.getAll()); // E: ["1", "2", "3", "4"], PASSED TEST

queue.clear();
console.log(queue.getAll()); // E: [], PASSTED TEST

queue.enqueue("Enqueued item"); // TEST PASSED
queue.enqueue("2nd Enqueued item"); // TEST PASSED
console.log(queue.getAll()); // E: ["Enqueued item", "2nd Enqueued item"], TEST PASSED

console.log(queue.get(0)) // E: "Enqueued item", TEST PASSED

queue.every(console.log); // TEST PASSED

console.log(queue.map((e) => `\`${e}\``)); // E: [ '`Enqueued item`', '`2nd Enqueued item`' ] TEST PASSED

console.log(queue.getSize()); // E: 2, TEST PASSED

console.log(queue.isEmpty()) // E: false, TEST PASSED

console.log(queue.frontMost()); // E: "Enqueued item", TEST PASSED
console.log(queue.getAll())
queue.dequeue() // E:

console.log(queue.getAll()) // E: [], TEST PASSED