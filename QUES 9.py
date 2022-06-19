n=int(input("Number of words: "))
li=[]
for i in range(n):
    word=input("Enter the word: ")
    li.append(word)
times={}
for i in li :
    if i not in times :
        times[i]=1
    else :
        times[i]+=1
print("Number of occurences: ",times)
