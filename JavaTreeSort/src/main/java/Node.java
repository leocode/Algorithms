public class Node {
    public Object element;
    public Node leftChild;
    public Node rightChild;


    public Node(Object theElement) {
        this(theElement, null, null);
    }

    public Node(Object theElement, Node leftConnection, Node rightConnection) {
        element = theElement;
        this.leftChild = leftConnection;
        this.rightChild = rightConnection;
    }
}

