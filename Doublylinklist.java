class Node {
    public int data;
    public Node next;
    public Node prev;

    public void displayNodeData() {
        System.out.println("{ " + data + " } ");
    }
}

public class MyDoublyLinkedList {

    private Node head;
    private Node tail;
    int size;

    public boolean isEmpty() {
        return (head == null);
    }

    // Method to insert a node at the start of linked list
    public void insertFirst(int data) {
        Node newNode = new Node();
        newNode.data = data;
        newNode.next = head;
        newNode.prev=null;
        if(head!=null)
            head.prev=newNode;
        head = newNode;
        if(tail==null)
            tail=newNode;
        size++;
    }

    // Method to insert a node at the start of linked list
    public void insertLast(int data) {
        Node newNode = new Node();
        newNode.data = data;
        newNode.next = null;
        newNode.prev=tail;
        if(tail!=null)
            tail.next=newNode;
        tail = newNode;
        if(head==null)
            head=newNode;
        size++;
    }
    // used to delete node from start of Doubly linked list
    public Node deleteFirst() {

        if (size == 0)
            throw new RuntimeException("Doubly linked list is already empty");
        Node temp = head;
        head = head.next;
        head.prev = null;
        size--;
        return temp;
    }

    // Method to delete node from last of Doubly linked list
    public Node deleteLast() {

        Node temp = tail;
        tail = tail.prev;
        tail.next=null;
        size--;
        return temp;
    }

    // Method to delete node after particular node
    public void deleteAfter(Node after) {
        Node temp = head;
        while (temp.next != null && temp.data != after.data) {
            temp = temp.next;
        }
        if (temp.next != null)
            temp.next.next.prev=temp;
        temp.next = temp.next.next;

    }

    // Method to print Doubly Linked List forward
    public void printLinkedListForward() {
        System.out.println("Printing Doubly LinkedList (head --> tail) ");
        Node current = head;
        while (current != null) {
            current.displayNodeData();
            current = current.next;
        }
        System.out.println();
    }

    // Method to print Doubly Linked List forward
    public void printLinkedListBackward() {
        System.out.println("Printing Doubly LinkedList (tail --> head) ");
        Node current = tail;
        while (current != null) {
            current.displayNodeData();
            current = current.prev;
        }
        System.out.println();
    }

    public static void main(String args[])
    {
        MyDoublyLinkedList mdll = new MyDoublyLinkedList();
        mdll.insertFirst(50);
        mdll.insertFirst(60);
        mdll.insertFirst(70);
        mdll.insertFirst(10);
        mdll.insertLast(20);
        mdll.printLinkedListForward();
        mdll.printLinkedListBackward();

        System.out.println("================");
        // Doubly Linked list will be
        // 10 ->  70 -> 60 -> 50 -> 20

        Node node=new Node();
        node.data=10;
        mdll.deleteAfter(node);
        mdll.printLinkedListForward();
        mdll.printLinkedListBackward();
        // After deleting node after 1,doubly Linked list will be
        // 20 -> 10 -> 60-> 50
        System.out.println("================");
        mdll.deleteFirst();
        mdll.deleteLast();

        // After performing above operation, doubly Linked list will be
        //  60 -> 50
        mdll.printLinkedListForward();
        mdll.printLinkedListBackward();
    }
}
