package aoc;

import java.util.HashSet;
import java.util.Set;

public class Graph<F, C> {

    private Set<Node> nodesSet;
    private Set<Edge<F, C>> edgesSet;

    public Graph() {
        nodesSet = new HashSet<>();
        edgesSet = new HashSet<>();
    }

    public void addNode(final Node node) {
        nodesSet.add(node);
    }

    public void addNodes(final Set<Node> nodes) {
        nodesSet.addAll(nodes);
    }

    public void addEdge(final Edge<F, C> edge) {
        edgesSet.add(edge);

    }

    public void addEdges(final Set<Edge<F, C>> edge) {
        edgesSet.addAll(edge);

    }

    public class Node {
        final String name;

        public Node(final String name) {
            this.name = name;
        }
    }

    public class Edge<F, C> {
        private Node from;
        private Node to;
        private F flow;
        private C cost;

        public Edge(final Node from, final Node to, final F flow, final C cost) {
            this.from = from;
            this.to = to;
            this.flow = flow;
            this.cost = cost;
        }

        public Node getFrom() {
            return from;
        }

        public Node getTo() {
            return to;
        }

        public F getFlow() {
            return flow;
        }

        public C getCost() {
            return cost;
        }
    }
}
