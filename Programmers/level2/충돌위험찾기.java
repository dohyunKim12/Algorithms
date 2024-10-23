package org.example;

import java.util.*;

class Solution {
    List<int[][]> robots = new ArrayList<>();

    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        for(int i = 0;i<routes.length;i++) {
            int[] route = routes[i];

            int[][] robot = new int[2][2];
            robot[0] = points[route[0] - 1].clone();
            robot[1] = points[route[1] - 1].clone();
            robots.add(robot);
        }
        answer += detectCollide();
        while(!robots.isEmpty()) {
            move();
            answer += detectCollide();
            flushRobot();
        }
        return answer;
    }
    private void move() {
        for(int[][] robot : robots){
            int[] start = robot[0];
            int[] end = robot[1];

            if (start[0] != end[0]) {
                start[0] += (end[0] > start[0]) ? 1 : -1;
            }
            else if (start[1] != end[1]) {
                start[1] += (end[1] > start[1]) ? 1 : -1;
            }
        }
    }
    private int detectCollide() {
        Set<String> pointSet = new HashSet<>();
        Set<String> realPoint = new HashSet<>();
        for(int[][] robot : robots){
            String point = Arrays.toString(robot[0]);
            if(!pointSet.add(point)) realPoint.add(point);
        }

        return realPoint.size();
    }
    private void flushRobot() {
        robots.removeIf(robot -> Arrays.equals(robot[0], robot[1]));
    }
}