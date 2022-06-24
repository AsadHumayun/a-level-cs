export = Queue;

declare class Queue extends Array<any> {
  constructor(data?: any[] | null);
    items: unknown[];
    enqueue(data: any | any[]): void;
    dequeue(loop?: number | null): void;
    removeDuplicates(): any[];
    get(index?: number | null): any | null;
    clear(): void;
    frontMost(): any | null;
    isEmpty(): boolean;
    getSize(): number;
    getAll(): any[];
}