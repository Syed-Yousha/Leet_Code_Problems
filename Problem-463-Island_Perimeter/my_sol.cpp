class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        
        int rows = grid.size();
        int cols = grid[0].size();
        int p = 0; 

        for(int i=0; i<rows; i++)
        {
            for(int j=0; j<cols; j++)
            {
                if(grid[i][j] == 1)
                {
                    //top
                    if( i==0 || grid[i-1][j]==0)
                    {
                        p++;
                    }
                    //buttom
                    if( i==rows-1 || grid[i+1][j] == 0)
                    {
                        p++;
                    }
                    //left
                    if( j==0 ||grid[i][j-1] == 0)
                    {
                        p++;
                    }
                    //right
                    if( j == cols-1 || grid[i][j+1] == 0)
                    {
                        p++;
                    }
                }

            }
        }
        return p;
    }
};

//time complexity: O(rows*cols)
//space complexity: O(1)


//This time my solution is the optimimal one .Yoo.