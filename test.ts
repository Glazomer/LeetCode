// @ts-ignore
import Heap from './heap.ts';
const h = new Heap([14, 12, 6, 23, 11, 19, 17, 3, 4]);
console.log(h.heap);
console.log(h.pop());
console.log(h.pop());
console.log(h.pop());
h.push(7);
console.log(h.pop());
console.log(h.pop());
