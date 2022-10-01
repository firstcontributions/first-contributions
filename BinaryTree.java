import java.util.Stack;

public class BinaryTree {

    public static class Node
    {
        int data;
        Node left;
        Node right;
        Node(int data)
        {
            this.data=data;
        }
    }

    // Recursive Solution
    public void preorder(Node root) {
        if(root !=  null) {
            //Pre order traversal
            System.out.printf("%d ",root.data);
            preorder(root.left);
            preorder(root.right);
        }
    }

    // Iterative solution
    public void preorderIter(Node root) {

        if(root == null)
            return;

        Stack<Node> s = new Stack<Node>();
        s.push(root);

        while(!s.empty()){

            Node n = s.pop();
            System.out.printf("%s ",n.data);

            if(n.right != null){
                s.push(n.right);
            }
            if(n.left != null){
                s.push(n.left);
            }

        }

    }

    public static void main(String[] args)
    {
        BinaryTree bi=new BinaryTree();
        // Creating a binary tree
        Node rootNode=createBinaryTree();
        System.out.println("Using Recursive solution:");

        bi.preorder(rootNode);

        System.out.println();
        System.out.println("-------------------------");
        System.out.println("Using Iterative solution:");

        bi.preorderIter(rootNode);
    }

    public static Node createBinaryTree()
    {

        Node rootNode =new Node(30);
        Node node20=new Node(50);
        Node node10=new Node(60);
        Node node30=new Node(80);
        Node node60=new Node(90);
        Node node50=new Node(100);
        Node node70=new Node(110);

        rootNode.left=node20;
        rootNode.right=node60;

        node20.left=node10;
        node20.right=node30;

        node60.left=node50;
        node60.right=node70;

        return rootNode;
    }
}
