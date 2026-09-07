class Solution {
    public Node cloneGraph(Node node) {
        if (node == null)
            return null;

        Stack<Node> stack = new Stack<>();
        HashMap<Node, Node> clones = new HashMap<>();

        stack.push(node);
        clones.put(node, new Node(node.val));

        while (!stack.empty()) {
            Node curr = stack.pop();

            for (Node neighbor : curr.neighbors) {

                // Haven't visited/cloned this node yet
                if (!clones.containsKey(neighbor)) {
                    clones.put(neighbor, new Node(neighbor.val));
                    stack.push(neighbor);
                }

                // Connect clone(curr) -> clone(neighbor)
                clones.get(curr).neighbors.add(clones.get(neighbor));
            }
        }

        return clones.get(node);
    }
}