#include <iostream>
#include <cmath>
using namespace std;
int numOfPages(int N, int X)
{
    int digits = 0, pages = 0;
    for (; digits <= N; X++)
    {
        if (digits == N)
            return pages;
        else
        {
            digits += log10(X) + 1;
            pages++;
        }
    }
    return -1;
}
int main()
{
    int n, N, X;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> N >> X;
        cout << numOfPages(N, X);
    }
}