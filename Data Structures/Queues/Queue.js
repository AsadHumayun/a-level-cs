/**
 * Queue data structure
 * @extends {Array}
 */
class Queue extends Array {
  /**
   * Creates the queue.
   * @param {?any[]} data Pre-parsed data that the Queue will be populated with.
   * @constructor
   */
  constructor(data = []) {
    if (!Array.isArray(data)) throw new TypeError(`QueueConstructor: Parameter 'data' must be of type Array. Received ${typeof data}`);
    super(data);
    /**
     * All the items held within the queue.
     * @type {any[]}
     */
    this.items = data;
  }
  /**
   * This function will enqueue a value to the queue's `items` property.
   * Adds `data` to the end of the queue.
   * @param {any | any[]} data Data to be enqueued (added to the end of the array).
   * @param data can be any[], if any[] then all values will be enqueued, starting from item as position 0.
   * @returns {void}
   */
  enqueue(data) {
    if (!data) return;
    if (Array.isArray(data)) {
      data.forEach(d => this.enqueue(d));
      return;
    }
    this.items.push(data);
  }
  /**
   * Dequeues the current Queue.
   * @param {?number} loop Amout of times to dequeue the Queue. Default is 1.
   * @returns {void}
   */
  dequeue(loop = 1) {
    if (loop > this.items.length) {
      this.items = [];
    }
    else {
      let i = 0;
      while (i !== loop) {
        this.items.shift();
        i++;
       }
    }
  }
  /**
   * Removes all duplicates from the Queue and returns it.
   * @returns {any[]}
   */
  removeDuplicates() {
    return [...new Set(this.items)];
  }
  /**
   * Gets a value at a specified `index` in the current Queue.
   * @param {?number} index Index of the element in the queue. This parameter defaults to 0 if not specified.
   * @returns {?any}
   */
  get(index = 0) {
    return this.items[index];
  }
  /**
   * Clears the Queue.
   * @returns {void}
   */
  clear() {
    this.items = [];
  }
  /**
   * Returns the frontmost element of the Queue.
   * @returns {?any}
   */
  frontMost() {
    return this.items[0];
  }
  /**
   * Checks whether the current queue is empty.
   * @returns {boolean}
   */
  isEmpty() {
    return this.items.length === 0;
  }
  /**
   * Returns the size of the current Queue.
   * @returns {number}
   */
  getSize() {
    return this.items.length;
  }
  /**
   * Returns the items in this Queue.
   * @returns {any[]}
   */
  getAll() {
    return this.items;
  }
}

module.exports = Queue;