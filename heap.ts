export default class Heap {
  #heap: number[];

  // shortcuts
  #parent = (i: number): number => Math.floor((i - 2) / 2);
  #left = (i: number): number => i * 2 + 1;
  #right = (i: number): number => i * 2 + 2;

  constructor(heap: number[] = []) {
    this.#heap = heap;
    for (let i = heap.length - 1; i >= 0; --i) {
      this.#heapifyBottom(i);
    }
  }

  pop(): number {
    const heap = this.#heap,
      result = heap[0],
      last = heap.pop();
    if (last && heap.length) {
      // checking var 'last', so tsling do not swear...
      heap[0] = last;
      this.#heapifyBottom(0);
    }
    return result;
  }

  push(num: number): void {
    this.#heap.push(num);
    this.#heapifyTop(this.#heap.length - 1);
  }

  #heapifyBottom = (i: number): void => {
    const heap = this.#heap;

    while (1) {
      const l = this.#left(i),
        r = this.#right(i);
      if (r < heap.length && heap[r] < heap[i] && heap[r] < heap[l]) {
        [heap[i], heap[r]] = [heap[r], heap[i]];
        i = r;
      } else if (l < heap.length && heap[l] < heap[i] && heap[l] < heap[r]) {
        [heap[i], heap[l]] = [heap[l], heap[i]];
        i = l;
      } else {
        break;
      }
    }
  };

  #heapifyTop = (i: number): void => {
    const heap = this.#heap;

    while (0 < i) {
      const p = this.#parent(i);
      if (0 <= p && heap[i] < heap[p]) {
        [heap[p], heap[i]] = [heap[i], heap[p]];
      }
      i = p;
    }
  };

  get [Symbol.toStringTag](): string {
    return 'Heap';
  }
  get [Symbol.iterator](): () => IterableIterator<number> {
    return this.#heap[Symbol.iterator].bind(this.#heap);
  }
  get heap(): number[] {
    return [...this.#heap];
  }
}
