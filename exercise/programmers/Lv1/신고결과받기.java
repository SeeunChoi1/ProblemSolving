package 프로그래머스;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class 신고결과받기 {
    public static void main(String[] args) throws FileNotFoundException{
        // get input
        // System.setIn(new FileInputStream("/Users/seunchoi/Desktop/Study/코딩테스트/input.txt"));
		// Scanner scan = new Scanner(System.in);

        // scan.nextLine();
        String[] id_list = new String[] {"con", "ryan"};
        String[] report = new String[] {"ryan con", "ryan con", "ryan con", "ryan con"};
        
        int[] answer = solution(id_list, report, 3);
        for(int i = 0; i<answer.length; i++){
            System.out.println(answer[i]);
        }
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};
        
        for(int i = 0; i<id_list.length; i++){
            System.out.println(id_list[i]);
        }
        return answer;
    }
}
