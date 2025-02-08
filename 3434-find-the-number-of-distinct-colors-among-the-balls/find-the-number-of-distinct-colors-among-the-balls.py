class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_ball={}
        ball_color={}

        ans=[]

        for i in range(len(queries)):
            ball=queries[i][0]
            color=queries[i][1]
            if ball in ball_color.keys():
                color_ball[ball_color[ball]]-=1
                if color_ball[ball_color[ball]]==0:
                    del color_ball[ball_color[ball]]

            
            ball_color[ball]=color
            if color in color_ball.keys():
                color_ball[color]+=1
            else:
                color_ball[color]=1
            ans.append(len(color_ball))
        return ans
            