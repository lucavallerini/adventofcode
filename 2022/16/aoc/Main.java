package aoc;

import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String args[]) {
        final Input input = new Input("2022/16/sample");
        ArrayList<String> lines = input.readInput();
        System.out.println(lines);

        Graph<Integer, Integer> graph = new Graph<Integer, Integer>();
        Pattern pattern = Pattern.compile("([0-9]+)");
        for (final String line : lines) {
            System.out.println(line);
            Matcher matcher = pattern.matcher(line);
            System.out.println(matcher.group());
        }
    }
}
