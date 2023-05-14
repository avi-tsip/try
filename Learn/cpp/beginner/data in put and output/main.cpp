#include <iostream>
#include <string>

int main()
{
    int age;
    std::string name;
    /*
    std::cout << "Type your age: " << std::endl;
    std::cin >> age;
    /* this is how we get a user in put that is without spaced
    std::cout << "Type your name: " << std::endl;
    std::cin >> name;
    

    //This is how we capture user input with spaces
    std::cout << "Type your name: " << std::endl;
    std::cin.ignore();
    std::getline(std::cin, name, '\n');
    */

    
    // We can also get the both age and name in the same line like this:
    std::cout << "Type your name and age seperated by a space: " << std::endl;
    std::cin >> name >> age;
    

    std::cout << "My name is " << name  << " and my age is " << age << std::endl;
    return 0;
}