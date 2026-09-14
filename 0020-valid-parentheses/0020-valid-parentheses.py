class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if (i == '('):
                st.append('(')
            elif(i == '{'):
                st.append('{')
            elif(i == '['):
                st.append('[')
            elif(i == ')'):
                if(not st or st[-1] != '('):
                    return False
                else:
                    st.pop()    
            elif(i == '}'):
                if(not st or st[-1] != '{'):
                    return False
                else:
                    st.pop()    
            elif(i == ']'):
                if(not st or st[-1] != '['):
                    return False
                else:
                    st.pop()    


        if not st:
            return True
        else:
            return False