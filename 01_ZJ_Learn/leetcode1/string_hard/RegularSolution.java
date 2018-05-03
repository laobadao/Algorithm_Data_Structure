/**
 * @author zhaojun (Email:laobadaozjj@gmail.com)
 *         <p>
 *         2017/11/15 13:22
 */

public class RegularSolution {
    enum Result {
        TRUE, FALSE
    }
    //Result 是枚举类型 里面只有 TRUE or FALSE
    //memo 是 Result 类型的 二维数据 ，也就是 所包含的元素 只有 TRUE FALSE  
    Result[][] memo;

    public boolean isMatch(String text, String pattern) {
        memo = new Result[text.length() + 1][pattern.length() + 1];
        // dp () 方法递归调用 i , j 初始化为 0
        return dp(0, 0, text, pattern);
    }

    public boolean dp(int i, int j, String text, String pattern) {

        if (memo[i][j] != null) {
            return memo[i][j] == Result.TRUE;
        }
        boolean ans;
        if (j == pattern.length()) {
            //  ans = ( i == text.length()) 看仔细了 ，== 是判断 判断结果是 Boolean 然后再赋值
            ans = i == text.length();
        } else {
            boolean first_match = (i < text.length() &&
                    (pattern.charAt(j) == text.charAt(i) ||
                            pattern.charAt(j) == '.'));

            if (j + 1 < pattern.length() && pattern.charAt(j + 1) == '*') {

                ans = (dp(i, j + 2, text, pattern) ||
                        first_match && dp(i + 1, j, text, pattern));
            } else {
                ans = first_match && dp(i + 1, j + 1, text, pattern);
            }
        }
        // if (ans) ans == true ，memo[i][j] = Result.TRUE 
        memo[i][j] = ans ? Result.TRUE : Result.FALSE;
        return ans;
    }

    public static void main(String[] args) {
        RegularSolution rs = new RegularSolution();
        boolean result = rs.isMatch("bbbccc", "a*b*c*");
        System.out.print("isMatch(aaabbbccc, a*b*c*)=" + result);
        // isMatch(aaabbbccc, a*b*c*) = true 
        // isMatch(bbbccc, a*b*c*)
    }
}

