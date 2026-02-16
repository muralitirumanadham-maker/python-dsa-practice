def floodFill(image, sr, sc, newColor):
    old_colour=image[sr][sc]
    if old_colour==newColor:
        return image
    def dfs(r,c):
        if r<0 or c<0 or r>=len(image) or c>=len(image[0]):
            return
        if image[r][c]!=old_colour:
            return
        image[r][c]=newColor
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    dfs(sr,sc)
    return image

image=[
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
sr=1
sc=1
new_color=2
result=floodFill(image,sr,sc,new_color)
print("output is:")
for row in result:
    print(row)
