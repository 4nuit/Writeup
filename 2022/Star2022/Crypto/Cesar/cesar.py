# According chall name ... We guess that the cipher used is Caesar (on file lol it's a funny way)
# We've JPEG encrypted in input (cadeau.jpeg.enc) so we know magic number of JPEG. We will use that to find how to shift it...
# using xxd, let's see first bytes... we see QNRP instead JFIF: now try to find the shift
    # ord('Q') - ord('J') = 7 
    # ord('N') - ord('F') = 8
    # ord('R') - ord('I') = 9
    # ord('P') - ord('F') = 10
    # it's look like the shift is the byte position(Q is the 7 byte) is the file

#let's write a little script to uncipher that:
with open("cadeau.jpg.enc","rb") as f:
    data = f.read()


with open("flag.jpg","wb") as f:
    for i in range(len(data)):
        b = (data[i]-i-1)%(0xFF+1)
        f.write(b.to_bytes(1, 'big'))

# waw it's working, enjoy the flag