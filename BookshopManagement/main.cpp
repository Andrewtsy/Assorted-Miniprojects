#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

class bookshop {
public:
  void control_panel();
  void add_book();
  void show_book();
  void check_book();
  void update_book();
  void del_book();
};

void bookshop::control_panel()
{
  system("clear");
  cout << "\n\n\t\t\t\tControl Panel";
  cout << "\n1. Add Books";
  cout << "\n2. Display books";
  cout << "\n3. Check Particular Book";
  cout << "\n4. Update Book";
  cout << "\n5. Delete Book";
  cout << "\n6. Exit";
}

void bookshop::add_book()
{
  system("clear");
  fstream file;
  int no_copy;
  string b_name, a_name, b_id;

  cout << "\n\n\t\t\t\tAdd Books";
  cout << "\n\nBook Id: ";
  cin >> b_id;
  cout << "\nBook Name: ";
  cin >> b_name;
  cout << "\nAuthor Name: ";
  cin >> a_name;
  cout << "\nNo. of Books: ";
  cin >> no_copy;

  file.open("book.txt", ios::out | ios::app);
  file << " " << b_id << " " << b_name << " " << a_name << " " << no_copy << "\n";
  file.close();
}

void bookshop::show_book()
{
  system("clear");
  fstream file;
  int no_copy;
  string b_name, b_id, a_name, wait;
  cout << "\n\n\t\t\t\t\tAll Books";

  file.open("book.txt", ios::in);
  if (!file)
    cout << "\n\nFile Opening Error!";
  else {
    cout << "\n\n\nBook ID\t\tBook"
         << "\t\tAuthor\t\tNo. of "
            "Books\n\n";
    file >> b_id >> b_name;
    file >> a_name >> no_copy;

    while (!file.eof()) {
      cout << " " << b_id
           << "\t\t" << b_name
           << "\t\t" << a_name
           << "\t\t" << no_copy
           << "\n\n";
      file >> b_id >> b_name;
      file >> a_name >> no_copy;
    }

    cout << "Enter any char to continue: ";
    cin >> wait;
    file.close();
  }
}

void bookshop::check_book()
{
  system("clear");
  fstream file;
  int no_copy, count = 0;
  string b_id, b_name, a_name, b_idd;

  cout << "\n\n\t\t\t\tCheck "
       << "Particular Book";

   file.open("book.txt", ios::in);
   if (!file)
      cout << "\n\nFile Opening Error!";
    else {
      cout << "\n\nBook ID : ";
      cin >> b_idd;
      file >> b_id >> b_name;
      file >> a_name >> no_copy;

      while (!file.eof()) {
        if (b_idd == b_id) {
          system("clear");
          cout << "\n\n\t\t\t\t"
               << "Check Particular Book";
          cout << "\n\nBook ID : "
               << b_id;
          cout << "\nName : "
               << b_name;
          cout << "\nAuthor : "
               << a_name;
          cout << "\nNo. of Books : "
               << no_copy;
          cout << endl
               << endl;
          count++;
          break;
        }
        file >> b_id >> b_name;
        file >> a_name >> no_copy;
      }
      file.close();
      if (count == 0)
        cout << "\n\nBook ID Not Found...";
    }
}

void bookshop::update_book()
{
  system("clear");
  fstream file, file1;
  int no_copy, no_co, count = 0;
  string b_name, b_na, a_name;
  string a_na, b_idd, b_id;

  cout << "\n\n\t\t\t\tUpdate Book Record";
  file1.open("book1.txt", ios::app | ios::out);
  file.open("book.txt", ios::in);

  if (!file)
    cout << "\n\nFile Opening Error";
  else {
    cout << "\n\nBook ID: ";
    cin >> b_id;
    file >> b_idd >> b_name;
    file >> a_name >> no_copy;

    while (!file.eof()) {
      if (b_id == b_idd) {
        system("clear");
        cout << "\t\t\t\t"
             << "Update Book Record";
        cout << "\n\nNew Book Name : ";
        cin >> b_na;
        cout << "\nAuthor Name : ";
        cin >> a_na;
        cout << "\nNo. of Books : ";
        cin >> no_co;
        file1 << " " << b_id << " "
              << b_na << " "
              << a_na << " " << no_co
              << "\n\n";
        count++;
        cout << "Yes Marker\n";
      }
      else
        file1 << " " << b_idd
             << " " << b_name
             << " " << a_name
             << " " << no_copy
             << "\n\n";
      file >> b_idd >> b_name;
      file >> a_name >> no_copy;
      cout << "No Marker\n";
    }
    if (count == 0)
      cout << "\n\nBook ID"
           << " Not Found...";
  }
  cout << endl;
  file.close();
  file1.close();
  remove("book.txt");
  rename("book1.txt", "book.txt");
}

void bookshop::del_book()
{
  system("clear");
  fstream file, file1;
  int no_copy, count = 0;
  string b_id, b_idd, b_name, a_name;
  cout << "\n\n\t\t\t\tDelete a Book";

  file1.open("book1.txt", ios::app | ios::out);
  file.open("book.txt", ios::in);

  if (!file)
    cout << "\n\nFile Opening Error";
  else {
    cout << "\n\nBook ID: ";
    cin >> b_id;
    file >> b_idd >> b_name;
    file >> a_name >> no_copy;
    while (!file.eof()) {
      if (b_id == b_idd) {
        system("clear");
        cout << "\n\n\t\t\t\t"
             << "Delete a Book";
        cout << "\n\nBook is Deleted Successfully...\n\n";
        count++;
      }
      else
        file1 << " " << b_idd
              << " " << b_name
              << " " << a_name
              << " " << no_copy
              << "\n\n";
      file >> b_idd >> b_name;
      file >> a_name >> no_copy;
    }
    if (count == 0)
      cout << "\n\nBook ID Not Found";
  }
  file.close();
  file1.close();
  remove("book.txt");
  rename("book1.txt", "book.txt");
}

void bookShopRecord()
{
  int choice;
  char x;
  bookshop b;

  while (1) {
    b.control_panel();
    cout << "\n\nEnter your choice: ";
    cin >> choice;
    switch (choice) {
      case 1:
        do {
          b.add_book();
          cout << "\n\nWant to add another book? (y/n): ";
          cin >> x;
        } while (x == 'y');
        break;

      case 2:
        b.show_book();
        break;

      case 3:
        b.check_book();
        break;

      case 4:
        b.update_book();
        break;

      case 5:
        b.del_book();
        break;

      case 6:
        exit(0);
        break;

      default:
        cout << "\n\nInvalid Choice\n";
    }
  }
}

int main()
{
  bookShopRecord();
  return 0;
}
