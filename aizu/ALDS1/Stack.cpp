/**
 * デバッグ
 * https://qiita.com/2019Shun/items/5ab290a4117a00e373b6
 * */
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

struct Stack *tmp_stack;

struct Stack * getStack(void)
{
    return tmp_stack;
}

void setStack(struct Stack *stack)
{
    tmp_stack = stack;
}

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

struct Stack * createStack(void)
{
    struct Stack *result = (Stack *)malloc(1 * sizeof(Stack));
    return result;
}

struct Stack * initialize(void)
{
    struct Stack *result = createStack();
    result->var = "0";
    result->prev = nullptr;
    result->next = nullptr;

    return result;
}

struct Stack * push(struct Stack *stack, std::string var)
{
    struct Stack *new_stack = initialize();

    if (stack != nullptr) {
        stack = head(stack);
        new_stack->next = stack;
        stack->prev = new_stack;
    }
    
    if(var.size() > 0) {
        new_stack->var = var;
    }
    
    return new_stack;
}

std::string pop(struct Stack *stack)
{
    struct Stack *remove_stack;
    std::string result;

    stack = head(stack);

    if (!stack->var.empty()) {
        result = stack->var;
    } else {
        result = "0";
    }

    if(stack->next != nullptr) {
        remove_stack = stack;
        stack = stack->next;
        stack->prev = nullptr;
        remove_stack = nullptr;
    } else {
        stack = nullptr;
    }
    
    if (stack != nullptr) stack = head(stack);

    setStack(stack);

    return result;
}

int main(void)
{
    std::string a;
    std::string b;
    std::string s;
    int tmp = 0;

    struct Stack *stack = nullptr;

    while (!(cin >> s).eof()) 
    {
        if (s == std::string("+")) {
            /* code */
            a = pop(stack);
            stack = getStack();
            b = pop(stack);
            stack = getStack();
            stack = push(stack, to_string(std::stoi(a) + std::stoi(b)));
        } else if(s == std::string("-")) {
            /* code */
            b = pop(stack);
            stack = getStack();
            a = pop(stack);
            stack = getStack();
            stack = push(stack, to_string(std::stoi(a) - std::stoi(b)));
        } else if(s == std::string("*")) {
            /* code */
            a = pop(stack);
            stack = getStack();
            b = pop(stack);
            stack = getStack();
            stack = push(stack, to_string(std::stoi(a) * std::stoi(b)));
        } else {
            stack = push(stack, s);
        }

        stack = head(stack);

        if (cin.eof() || cin.fail() || s.empty()) {
            break;
        }
    }

    cout << stack->var << endl;

    return 0;
}