// constructing vectors
#include <iostream>
#include <vector>
#include <new>


extern "C" std::vector<int>* divide_p(int total, int part);
extern "C" int* get_global_array(int total, int part);

std::vector<int>* divide_p(int total, int part)
{
    std::vector<int> *v = new std::vector<int>();

    while (part) {
        v->insert(v->end(), total / part);
        total -= total / part;
        part--;
    }

    return v;
}

int global_v[4] = {1, 2, 3, 4};

int* get_global_array(int total, int part)
{
    int *v = global_v;
    return v;
}


int main() {
    std::vector<int> *vp;
    vp = divide_p(10, 3);
    for (std::vector<int>::iterator it = vp->begin(); it != vp->end(); ++it)
        std::cout << ' ' << *it;
    std::cout << '\n';
}
