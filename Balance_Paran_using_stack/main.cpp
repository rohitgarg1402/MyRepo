//
//  main.cpp
//  BalaParanusingStack
//
//  Created by Rohit Garg on 10/13/16.
//  Copyright © 2016 Rohit Garg. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <stack>
using namespace std;

bool arepair(char left,char right)
{
    if(left == '(' && right == ')')
    {
        return true;
    }
    else if(left == '{' && right == '}')
    {
        return true;
    }
    else if(left == '[' && right == ']')
    {
        return true;
    }
    else
    {
        return false;
    }
    
}
bool checkbalpara(string c,int n)
{
    int i;
    stack<char> s;
    for(i=0;i<n;i++)
    {
        if(c[i] == '{' || c[i] == '[' || c[i] == '(')
        {
            s.push(c[i]);
        }
        else if(c[i] == '}' || c[i] == ']' || c[i] == ')')
        {
            if(s.empty() || !arepair(s.top(),c[i]))
            {
                return false;
            }
            else
            {
                s.pop();
            }
        }
    }
    if(s.empty())
    {
        return true;
    }
    return false;
}

int main()
{
    string c;
    bool result;
    cout<< "Please Enter a string:";
    cin>>c;
    result = checkbalpara(c,c.length());
    if (result == true)
    {
        cout<<"Paranthesis are balanced\n";
    }
    else
    {
        cout<<"Paranthesis are not balanced\n";
    }
    
}
