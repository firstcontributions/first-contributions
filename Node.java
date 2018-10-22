package com.company;
public class Node<T>{
        private T data;
        private Node<T> next;
        public Node(T data){
            this.data = data;
            this.next = null;
        }
        public Node(T data, Node<T> next){
            this.data = data;
            this.next = next;
        }
        public Node getNext(){
            return this.next;
        }

        public T getData() {
            return this.data;
        }

        public void setNext(Node<T> next) {
            this.next = next;
        }
        public void setData(T data){
            this.data = data;
        }
    }

