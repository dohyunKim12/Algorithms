package org.example;

import java.util.*;

class 공원 {
    String[][] parkGraph;
    int maxVal = 0;
    public int solution(int[] mats, String[][] park) {
        parkGraph = new String[park.length][park[0].length];
        for(int i = 0;i<park.length;i++) {
            parkGraph[i] = park[i].clone();
        }
        Arrays.sort(mats);

        maxVal = Arrays.stream(mats).max().getAsInt();
        int maximumSize = 0;

        for(int i = 0; i<park.length;i++) {
            for(int j = 0; j< park[0].length; j++) {
                if(park[i][j].equals("-1")) {
                    int size = 1;
                    int scale = checkScalability(i, j);
                    if(scale != 0) {
                        size += scale;
                    }
                    maximumSize = Math.max(maximumSize, size);
                }
            }
        }

        System.out.println(maximumSize);
        int answer = 0;

        for(int i = 0;i<mats.length;i++) {
            if (i ==0 && mats[i] > maximumSize) return -1;
            if(mats[i] > maximumSize) break;
            answer = Math.min(maximumSize, mats[i]);
        }
        return answer;
    }
    private int checkScalability(int i, int j) {
        int scale = 0;
        for(int x = 1;x<maxVal;x++) {
            for(int y = 0;y<=x;y++) {
                if(i+x >= parkGraph.length || j + x >= parkGraph[0].length) return scale;
                if(!(parkGraph[i+x][j+y].equals("-1") && parkGraph[i+y][j+x].equals("-1"))) {
                    return scale;
                }
            }
            scale = x;
        }
        return scale;
    }

}