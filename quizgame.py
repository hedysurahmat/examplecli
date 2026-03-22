q={"2+2":"4","3+3":"6"}
score=0
for k,v in q.items():
    if input(k+"=")==v: score+=1
print(score)
