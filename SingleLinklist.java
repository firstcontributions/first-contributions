class Node {
    public int data;
    public Node next;

    public void displayNodeData() {
        System.out.println("{ " + data + " } ");
    }
}

public class MyLinkedList {
    private Node head;

    public boolean isEmpty() {
        return (head == null);
    }

    // Method for inserting node at the start of linked list
    public void insertFirst(int data) {
        Node newHead = new Node();
        newHead.data = data;
        newHead.next = head;
        head = newHead;
    }

    // Method for deleting node from start of linked list
    public Node deleteFirst() {
        Node temp = head;
        head = head.next;
        return temp;
    }

    // Method used to delete node after provided node
    public void deleteAfter(Node after) {
        Node temp = head;
        while (temp.next != null && temp.data != after.data) {
            temp = temp.next;
        }
        if (temp.next != null)
            temp.next = temp.next.next;
    }

    // Method used to insert at end of LinkedList
    public void insertLast(int data) {
        Node current = head;
        while (current.next != null) {
            current = current.next; // we'll loop until current.next is null
        }
        Node newNode = new Node();
        newNode.data = data;
        current.next = newNode;
    }

    // Method for printing Linked List
    public void printLinkedList() {
        System.out.println("Printing LinkedList (head --> last) ");
        Node current = head;
        while (current != null) {
            current.displayNodeData();
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String args[])
    {
        MyLinkedList myLinkedlist = new MyLinkedList();
        myLinkedlist.insertFirst(50);
        myLinkedlist.insertFirst(60);
        myLinkedlist.insertFirst(70);
        myLinkedlist.insertFirst(10);
        myLinkedlist.insertLast(20);
        myLinkedlist.printLinkedList();
        // Linked list will be
        // 10 -> 70 ->  60 -> 50 -> 20

        System.out.println("=========================");
        System.out.println("Delete node after Node 60");
        Node node=new Node();
        node.data=60;
        myLinkedlist.deleteAfter(node);
        // After deleting node after 1,Linked list will be
        // 10 -> 70 -> 60 -> 20

        System.out.println("=========================");
        myLinkedlist.printLinkedList();
    }
}
