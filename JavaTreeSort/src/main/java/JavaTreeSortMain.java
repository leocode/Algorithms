

public class JavaTreeSortMain {
    public static void main(String[] args) {
        int[] input = {13, 15,12, 2, 29,4, 3, 155,1, 18, 120};
        Tree tree = new Tree(new Integer(input[0]));
        for (int i = 1; i < input.length; i++) {
            tree.insert(tree.root, new Integer(input[i]));
        }
        System.out.print("Elements in tree by increasing Order: ");
        tree.inOrder(tree.root);
        System.out.println();
        System.out.print("Elements in tree by decreasing Order: ");
        tree.descOrder(tree.root);
    }
}
