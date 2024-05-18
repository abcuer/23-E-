// #include <iostream>
// using namespace std;
// int main(){
//     cout << "Hello World! "<< endl;
//     system("pause");
//     return 0;
// }
// #include <iostream>
// using namespace std;
// int main()
// {
//     int a = 1,b = 2, c = 3;
//     int d=0;
//     cin >> d;
//     switch(d)
//     {
//         case 1: cout << "d小于1" <<endl; break;
//         case 2: cout << "d等于1" <<endl; break;
//         case 3: cout << "d大于1" <<endl; break;
//     }
//     cout << "d = " << d << endl;
//     system("pause");
//     return 0;
// }

#include <iostream>
using namespace std;
int main()
{
    int i,n;
    int sum=0;
    cin >> n;
    for(i=1;i<=n;i++)
    {
        if(i%2==0){
            sum+=1;
            cout<<i<<endl;
        }
    }
    cout<<sum<<endl;
    system("pause");
    return 0;
}