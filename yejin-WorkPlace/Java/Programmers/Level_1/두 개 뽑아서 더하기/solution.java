import java.util.HashSet;
import java.util.Comparator;
import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] numbers) {
        HashSet<Integer> answer = new HashSet<Integer>();
		
		
		for (int i = 0; i < numbers.length; i++) {
			for (int j = i + 1; j < numbers.length; j++) {
				answer.add(numbers[i] + numbers[j]);
			}
		}
		
		ArrayList<Integer> list = new ArrayList<Integer>(answer);
		
		list.sort(Comparator.naturalOrder());
        return list;
    }
}