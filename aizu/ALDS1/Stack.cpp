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


struct Stack * bottom(struct Stack *stack)
{
    if(stack->next == nullptr || stack == nullptr) {
        return stack;
    }

    while(1) {
        if(stack->next != nullptr){
            stack = stack->next;
        } else {
            break;
        }
    }

    return stack;
}

struct Stack * head(struct Stack *stack)
{
    if(stack->prev == nullptr || stack == nullptr){
        return stack;
    }

    while(1) {
        if(stack->prev != nullptr){
            stack = stack->prev;
        } else {
            break;
        }
    }

    return stack;
}

struct Stack * initialize(void)
{
    struct Stack *result = (Stack *)malloc(1 * sizeof(Stack));
    result->prev = nullptr;
    result->next = nullptr;

    struct Stack *stack = (Stack *)malloc(1 * sizeof(Stack));
    stack->prev = result;
    stack->next = nullptr;
    result->next = stack;

    return head(result);
}

struct Stack * push(struct Stack *stack, std::string var)
{
    std::string tmp;
    stack = head(stack);
    tmp = stack->var;
    
    if (!var.empty()) {
        stack->var = var;
    }

    stack = stack->next;
    
    if (!tmp.empty()) {
        stack->var = tmp;
    }

    stack = head(stack);
    

    return stack;
}

std::string pop(struct Stack *stack)
{
    std::string result;
    std::string tmp;

    stack = head(stack);
    if (!stack->var.empty()) {
        result = stack->var;
    }
    stack = bottom(stack);
    if (!stack->var.empty()) {
        tmp = stack->var;
    }
    stack->var = "0";
    stack = head(stack);
    if (!tmp.empty()) {
        stack->var = tmp;
    }
    

    return result;
}

int main(void)
{
    std::string a;
    std::string b;
    std::string s;

    struct Stack *stack = initialize();

    while (cin >> s) 
    {
        
        if (s == std::string("+")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            cout<< to_string(std::stoi(a) + std::stoi(b)) <<endl;
            stack = push(stack, to_string(std::stoi(a) + std::stoi(b)));
        } else if(s == std::string("-")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            stack = push(stack, to_string(std::stoi(a) - std::stoi(b)));
        } else if(s == std::string("*")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            stack = push(stack, to_string(std::stoi(a) * std::stoi(b)));
        } else if(s == std::string("/")) {
            /* code */
            a = pop(stack);
            b = pop(stack);
            stack = push(stack, to_string(std::stoi(a) / std::stoi(b)));
        } else {
            stack = push(stack, s);
        }

        stack = head(stack);
        if(!stack->var.empty()) cout << stack->var << endl;
    }

    stack = bottom(stack);
    free(stack->next);
    free(stack);
}