class Solution {
    public boolean isValid(String S) {
        Stack<Character> st=new Stack<>();
        for(char ch:S.toCharArray()){
            if(ch=='('){
                st.push(')');
            }
            else if(ch=='{'){
                st.push('}');
            }
            else if(ch=='['){
                st.push(']');
            }
            else if(st.isEmpty() || st.pop()!=ch){
                return false;
            }
        }
        return st.isEmpty();
    }
}