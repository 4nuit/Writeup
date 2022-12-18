#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

//gcc -o shop shop.c

unsigned int money; //Money is positive right ?

int getUserInput(){
 int res;
 char buffer[20];
 fgets(buffer, sizeof(buffer), stdin);
 res = strtol(buffer, NULL, 10);
 return res;
}

void win(){
 char buffer[50];
 FILE *fp = fopen("/home/pwn3r/flag", "r");
 if(fp){
  fgets(buffer,sizeof(buffer),fp);
  printf("%s\n",buffer);
 }
 else{
  puts("Error, contact the admins please.");
 }
}

void init(){
 puts("Welcome to the gorfou pet store!");
 puts("As you are new here, i give you a $200 coupon.");
 puts("Have fun!");
 money = 200;
}

void menu(){
 puts("====================");
 printf("You have $%u on your account\n",money);
 puts("1)Buy");
 puts("2)Quit");
}

void buy(){
 puts("====================");
 puts("1)Food: 10$");
 puts("2)Shampoo: 12$");
 puts("3)Flag: 10000$");
 puts("4)Cancel");
 int choice = getUserInput();
 int cost;
 int item = choice;
 switch (choice){
  case 1:
   cost = 10;
   break;
  case 2:
   cost = 12;
   break;
  case 3:
   cost = 10000;
   break;
  case 4:
   return;
   break;
  default:
   puts("We do not sell that here ...");
   return;
   break;
 }
 if(cost > money){
  puts("Sorry but you have not the money for that...");
 }
 else{
  money -= cost;
  if(item == 3){
   win();
  }
  puts("How much do you want to donate to the International Gorfou Foundation?");
  int choice = getUserInput();
  if(choice > money){
   puts("A man cannot give what he hasn't got!");
   return;
  }
  else if(choice == 0){
   puts("You are stingy, give them at least 10$!");
   money -= 10;
  }
  else{
   money -= choice;
   puts("Thank you for your donation!");
  }
 }
 return;
}

void main(){
 init();
 int choice;
 while (1){
  menu();
  choice = getUserInput();
  switch(choice){
   case 1:
    buy();
    break;
   case 2:
    puts("Bye");
    exit(0);
    break;
   default:
    puts("I didn't understand, could you repeat?");
    break;
  };
 };
}
