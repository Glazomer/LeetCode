export default class MinHeap {
  #heap;

  #parent = (i) => Math.floor((i - 2) / 2);
  #left = (i) => i * 2 + 1;
  #right = (i) => i * 2 + 2;

  constructor(heap = []) {
    this.#heap = heap;
    heap.reduceRight((_, __, i) => this.#heapifyBottom(i));
  }

  pop() {
    const heap = this.#heap,
      result = heap[0],
      last = heap.pop();
    if (heap.length) {
      heap[0] = last;
      this.#heapifyBottom(0);
    }
    return result;
  }

  push(num) {
    this.#heap.push(num);
    this.#heapifyTop(this.#heap.length - 1);
  }

  #heapifyBottom = (i) => {
    const heap = this.#heap;

    while (1) {
      const l = this.#left(i),
        r = this.#right(i);
      if (heap[r] < heap[i] && !(heap[r] > heap[l])) {
        [heap[i], heap[r]] = [heap[r], heap[i]];
        i = r;
      } else if (heap[l] < heap[i] && !(heap[l] > heap[r])) {
        [heap[i], heap[l]] = [heap[l], heap[i]];
        i = l;
      } else {
        break;
      }
    }
  };

  #heapifyTop = (i) => {
    const heap = this.#heap;

    while (0 < i) {
      const p = this.#parent(i);
      if (0 <= p && heap[i] < heap[p]) {
        [heap[p], heap[i]] = [heap[i], heap[p]];
      }
      i = p;
    }
  };

  get [Symbol.toStringTag]() {
    return 'Heap';
  }
  get [Symbol.iterator]() {
    return this.#heap[Symbol.iterator].bind(this.#heap);
  }
  get heap() {
    return [...this.#heap];
  }
}
