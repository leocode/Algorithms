public class Tree {
    public Node root;

    public Tree(Object x) {
        root = new Node(x);
    }

    public Node insert(Node node, Integer x) {
        if (node == null) {
            return node = new Node(x);
        }
        if (x < (Integer) node.element) {
            node.leftChild = insert(node.leftChild, x);
        } else {
            node.rightChild = insert(node.rightChild, x);
        }
        return node;
    }

    public void inOrder(Node node) {
        if (node != null) {
            inOrder(node.leftChild);
            System.out.print(((Integer) node.element).intValue() + ",");
            inOrder(node.rightChild);
        }
    }

    public void descOrder(Node node) {
        if (node != null) {
            descOrder(node.rightChild);
            System.out.print(((Integer) node.element).intValue() + ",");
            descOrder(node.leftChild);
        }
    }
}

