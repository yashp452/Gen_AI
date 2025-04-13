def build_vocab():
    vocab={}
    j=1
    for i in "ABCDEFGHIJHLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        vocab[i]=j
        j+=1
    for i in range(ord('अ'), ord('ह') + 1):  
        vocab[chr(i)] = j
        j += 1
    for i in range(ord('क'), ord('ह') + 1):
        vocab[chr(i)] = j
        j += 1
    matras = ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ', 'ं', 'ः', '्']
    for m in matras:
        vocab[m] = j
        j += 1
    return vocab

def tokenizer(subtext):
    ans=0
    length=len(subtext)
    for i,c in enumerate(subtext):
        power=length-i-1
        ans+=(vocab.get(c,0)*(10**(power)))
    return ans

text="The Cat बैठा Mat क खा ग घ"
vocab=build_vocab()
y=text.split(" ")
print(y)
z=[tokenizer(c) for c in y]
print(z)
