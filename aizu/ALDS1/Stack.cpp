/*#include<stdio.h>
#include<stdlib.h>
#include<string.h>*/
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

struct Stack
{
    std::string var;
    struct Stack *prev;
    struct Stack *next;
};


struct Stack * bottom(struct Stack *array)
{
    while(array->prev == nullptr) {
        array = array->prev;
    }
    return array;
}


struct Stack * initialize(void)
{
    struct Stack *result = (Stack *)malloc(1 * sizeof(Stack));
    result->var = nullptr;
    result->prev = nullptr;
    result->next = nullptr;
    struct Stack *tmp = result;

    for (int i = 0; i < 2; i++)
    {
        struct Stack *array = (Stack *)malloc(1 * sizeof(Stack));
        array->var = nullptr;
        array->prev = tmp;
        array->next = nullptr;
        tmp->next = array;
        tmp = array;
    }
    
    return result;
}

int isEmpty(struct Stack *array)
{
    bool result = false;

    array = bottom(array);

    while(array->next != nullptr)
    { 
        if(array->var.empty()) {
            result = true;
        }
    }

    return result;
}

int isFull(struct Stack *array)
{
    return 1;
}

bool push(struct Stack *stack, int num)
{
    return true;
}

int pop(struct Stack *stack)
{
    return 0;
}

int main(void)
{
    int a;
    int b;
    std::string s;

    struct Stack *stack = initialize();


    while (cin >> s) 
    {
        if (s == std::string("+")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            push(stack, a + b);
            break;
        } else if(s == std::string("-")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            push(stack, a - b);
            break;
        } else if(s == std::string("*")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            push(stack, a * b);
            break;
        } else if(s == std::string("/")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            push(stack, a / b);
            break;
        } else {
            push(stack, stoi(s));
            break;
        }
    }
}