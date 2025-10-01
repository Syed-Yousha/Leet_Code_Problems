class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size = digits.size();
        
        // agar last digit 9 nahi hai
        if(digits[size-1] != 9)
        {
            digits[size-1] += 1;
            return digits;
        }

        //agar last digit 9 hai
        int carry = 1;
        for(int i=size-1; i>=0; i--)
        {
            //first for digit like 9999
            if(i==0 && digits[i] == 9 && carry == 1)
            {
                digits[i] = 0;
                digits.insert(digits.begin(), 1);
                return digits;
            }

            //digits like 1299
            if(digits[i] == 9)
            {
                digits[i] = 0;
            }

            //digits like 1239
            if(digits[i] != 9)
            {
                digits[i] += 1;
                carry = 0;
                return digits;
            }
        
        }
        return digits;

    }
};