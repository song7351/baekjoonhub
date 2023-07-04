class Solution {
    public int solution(int n) {
        int answer = 0;
        for(; 0<n; n--) {
            if(n%2 == 0){
                answer += n;
            }
        }
        return answer;
    }
}