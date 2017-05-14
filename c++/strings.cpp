#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b ;
   
    cin >> a >> b ;
    
    cout << a.length() << ' ' << b.length() << endl ;
   
    cout << a << b << endl ;
    
    string c = a ;  c[0] = b[0] ;
    
    string d = b ; d[0] = a[0] ;
    
    cout << c << ' ' << d << endl ;
  
    return 0;
}
