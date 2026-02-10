#zip element

x={"a","b","c","d","e" }
y={1,2,3,4,5}
print("x=",x)
print("y=",y)
result=list(zip(x,y))
print(result)

#part2
subject=["english","math","science","social"]
code=[101,102,103,104]
result=list(zip(subject,code))

print("subject list=",result)
for i,j in zip(subject, code[ ::- 1]):
    print(i,j)

