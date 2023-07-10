class SLLNode { 
    constructor(val) {
        this.value = val; 
        this.next = null; 
    }
}

class SLL { 
    constructor() { 
        this.head = null; 
    }

    
    addFront(value) {
        var newNode = new SLLNode(value); 
        newNode.next = this.head; 
        this.head = newNode; 
        return this.head; 
    }

    
    removeFront() {
        if (this.head == null) { 
            return this.head;
        }
        var removedNode = this.head; 
        this.head = removedNode.next; 
        removedNode.next = null;
        return this.head;
    }

    
    front() {
        if (this.head == null) {
            return null;
        } 
        else { 
            return this.head.value;
        }
    }
}