class DynamicArray {

    private int capacity;
    private int size;
    private int[] contents; 

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.contents = new int[capacity];
    }

    public int get(int i) {
        return this.contents[i];
    }

    public void set(int i, int n) {
        this.contents[i] = n;

    }

    public void pushback(int n) {
        size++;
        if (size > capacity) {
            resize();
        }
        this.contents[size-1] = n;
    }

    public int popback() {
        return this.contents[--size];
    }

    private void resize() {
        int[] copy = this.contents;
        int oldCapacity = capacity;
        capacity *= 2;
        this.contents = new int[capacity];
        for (int i = 0; i < oldCapacity; i++) {
            this.contents[i] = copy[i];
        }
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
