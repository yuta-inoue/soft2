#include <iostream>
#include <list>

using namespace std;

class Cell {
  public:
    string name;
    string addr;
    Cell(string name,string addr);
};

list<Cell> db;
Cell::Cell(string name,string addr){
  this->name = name;
  this->addr = addr;
}
void addList(){
  string name,addr;
  cout << "type the name and address you want to add : ";
  cin >> name >> addr;
  Cell* cell = new Cell(name,addr);
  db.push_back(*cell);
}

void searchList(){
  string name;
  cout << "type the name you want to search : ";
  cin >> name;
  list<Cell>::iterator it;
  it = db.begin();
  while(it!=db.end()){
    Cell cell = *it;
    if(cell.name==name){
      cout << "name: " << name << " addr: " << cell.addr << endl;
      db.push_front(*(new Cell(name,cell.addr)));
      db.erase(it);
      return;
    }
    it++;
  }
  cout << "not found" << endl;
}

void print(){
  list<Cell>::iterator it;
  it = db.begin();
  cout << "print the content of database below" << endl;
  while(it!=db.end()){
    Cell cell = *it;
    cout << "name: " << cell.name << " addr: " << cell.addr << endl;
    it++;
  }
}
int main(){
  char command;
  string name,addr;
  list<Cell> db;
  while(cin >> command){
    switch(command){
      case 'a':
        addList();
        break;
      case 'p':
        print();
        break;
      case 's':
        searchList();
        break;
      case 'q':
        return -1;
        break;
      default:
        cout << "error" << endl;
        break;
    }
  }
}
