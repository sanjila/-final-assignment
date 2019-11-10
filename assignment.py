from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Information System")
        self.root.geometry('1000x700')
        # connection to database
        try:
            self.con = mysql.connector.connect(host='localhost', user='root', passwd='root', database="student")
            self.mycursor = self.con.cursor()
            self.mycursor.execute('create table if not exists student'
                                  '(student_id int not null,first_name varchar(50),last_name varchar(50),degree '
                                  'varchar(50), address varchar(13), contact_number varchar(40), '
                                  'constraint pk_id primary key(student_id))')
            print("connect")
        except mysql.connector.Error as e:
            messagebox.showinfo('Connection Error', 'There is problem in connection!!')
            sys.exit()


        # Adding widget in the form
        # #title frame

        self.title_frame = Frame(self.root, bd=4, relief=RIDGE, bg='grey')
        self.title_frame.place(x=20, y=20, width=800, height=50)


        self.lbltitle = Label(self.title_frame, text='STUDENT INFORMATION SYSTEM', font='bold', bg='grey', padx=15, pady=15).pack()

        # label frame
        self.label_frame = Frame(self.root, bd=4, relief=RIDGE, bg='grey')
        self.label_frame.place(x=20, y=100, width=450, height=500)

        # labels of the form
        self.lblsid = Label(self.label_frame, text="Student id:", bg='grey').grid(row=1, column=0, padx=15, pady=15)
        self.lblfname = Label(self.label_frame, text="First name:", bg='grey').grid(row=2, column=0, padx=15, pady=15)
        self.lblLname = Label(self.label_frame, text="Last name:", bg='grey').grid(row=3, column=0, padx=15, pady=15)
        self.lbladdress = Label(self.label_frame, text="Address:", bg='grey').grid(row=5, column=0, padx=15, pady=15)
        self.lblcno = Label(self.label_frame, text="Contact number:", bg='grey').grid(row=6, column=0, padx=15, pady=15)

        # choose degree
        self.lbldegree = Label(self.label_frame, text="Degree:", bg='grey')
        self.lbldegree.grid(row=4, column=0, padx=15, pady=15)
        self.entry_degree = ttk.Combobox(self.label_frame, state='readonly')
        self.entry_degree['values'] = ['BSc(Hons)Computing', 'BSc(Hons)Ethical Hacking', 'Msc.It', 'Msc.software engineering']
        self.entry_degree.grid(column=1, row=4)

        # ===Entry of the form
        self.entrystudent_id = Entry(self.label_frame)
        self.entrystudent_id.grid(row=1, column=1, padx=15, pady=15)
        self.entryfirst_name = Entry(self.label_frame)
        self.entryfirst_name.grid(row=2, column=1, padx=15, pady=15)
        self.entrylast_name = Entry(self.label_frame)
        self.entrylast_name.grid(row=3, column=1, padx=15, pady=15)
        self.entry_address = Entry(self.label_frame)
        self.entry_address.grid(row=5, column=1, padx=15, pady=15)
        self.entrycontact_number = Entry(self.label_frame)
        self.entrycontact_number.grid(row=6, column=1, padx=15, pady=15)

        # ==Frame for buttons
        self.button_frame = Frame(self.label_frame, bd=4, relief=RIDGE, bg='white')
        self.button_frame.place(x=20, y=300, width=400, height=50)

        # ==buttons
        self.addButton = Button(self.button_frame, text="Add", bg='grey', command=self.add_info)
        self.addButton.grid(row=0, column=2, padx=10, pady=10)
        self.updateButton = Button(self.button_frame, text="Update", bg='grey', command=self.update_info)
        self.updateButton.grid(row=0, column=4, padx=10, pady=10)
        self.deleteButton = Button(self.button_frame, text="Delete", bg='grey', command=self.delete_info)
        self.deleteButton.grid(row=0, column=6, padx=10, pady=10)
        self.clearButton = Button(self.button_frame, text="Clear", bg='grey', command=self.clear_info)
        self.clearButton.grid(row=0, column=8, padx=10, pady=10)
        self.showButton = Button(self.button_frame, text="Show all", bg='grey', command=self.show_data)
        self.showButton.grid(row=0, column=10, padx=10, pady=10)
        self.exitButton = Button(self.label_frame, text="EXIT", bg='grey', height=1, width=6, command=self.Exit)
        self.exitButton.grid(row=10, column=1, padx=80, pady=80)
       #--table_frame
        self.table_frame = Frame(self.root, bd=4, relief=RIDGE, bg='grey')
        self.table_frame.place(x=480, y=100, width=500, height=500)

      # --search-frame
        self.search_frame = Frame(self.table_frame, bd=4, relief=RIDGE, bg='grey')
        self.search_frame.place(x=5, y=20, width=480, height=100)

       # --search combobox
      # combo=ttk.combobox(root)
        self.entry = ['Student id', 'First name', 'Last name', 'Degree','Address']
        self.l1 = Label(self.search_frame, width=10, text='Search by:', bg='grey').grid(column=1, row=0)
        self.combo_search = ttk.Combobox(self.search_frame, values=self.entry,state='readonly')
        self.combo_search.grid(column=3, row=0)

        self.l2 = Label(self.search_frame, width=10, text='Search:', bg='grey').grid(column=1, row=3)
        self.entry_search = Entry(self.search_frame)
        self.entry_search.grid(column=3, row=3)

        self.searchButton=Button(self.search_frame,text='Search',command=self.info_search)
        self.searchButton.grid(row=4,column=3)

        # sort
        self.sort_label = Label(self.search_frame, width=10, text='Sort by:', bg='grey').grid(column=5, row=0)
        self.combo_sort = ttk.Combobox(self.search_frame, values=['Student id', 'First name', 'Last name', 'Degree','Address'],state='readonly')
        self.combo_sort.grid(column=7, row=0)

        self.sortButton = Button(self.search_frame, text='Sort',command=self.sorting_info)
        self.sortButton.grid(row=3, column=7, padx=5, pady=5)

#         # ==scrollback
        self.scroll_frame = Frame(self.table_frame, bd=4, relief=RIDGE, bg='white')
        self.scroll_frame.place(x=5, y=130, width=480, height=350)

        self.scroll_x = Scrollbar(self.scroll_frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.scroll_frame, orient=VERTICAL)

        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        self.student_table = ttk.Treeview(self.scroll_frame, columns=('self.student_id', 'self.first_name', 'self.last_name', 'self.degree', 'self.address', 'self.contact_number')
                                          , xscrollcommand=self.scroll_x.set,
                                 yscrollcommand=self.scroll_y.set)

        self.student_table.heading('self.student_id', text="Student id")
        self.student_table.heading('self.first_name', text='First name')
        self.student_table.heading('self.last_name', text='Last name')
        self.student_table.heading('self.degree', text='Degree')
        self.student_table.heading('self.address', text='Address')
        self.student_table.heading('self.contact_number', text='Contact Number')
        self.student_table['show'] = 'headings'

        self.student_table.column('self.student_id', width=30)
        self.student_table.column('self.first_name', width=30)
        self.student_table.column('self.last_name', width=30)
        self.student_table.column('self.degree', width=55)
        self.student_table.column('self.address', width=30)
        self.student_table.column('self.contact_number', width=60)

        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=True)
        self.show_data()
        self.student_table.bind('<ButtonRelease-1>', self.pointer)



# # #add information to the database
    def add_info(self):
        try:
            self.student_id = self.entrystudent_id.get()
            self.first_name = self.entryfirst_name.get()
            self.last_name = self.entrylast_name.get()
            self.degree = self.entry_degree.get()
            self.address = self.entry_address.get()
            self.contact_number = self.entrycontact_number.get()

            if self.student_id == '' or self.first_name == '' or self.last_name == '' or self.degree == '' or self.address == '' or self.contact_number == '':
                messagebox.showerror('Error', 'Please fill all input')
                return

            while self.student_id[0] == '0':
                 self.student_id = self.student_id[1:]

            if not self.first_name.isalpha():
                messagebox.showinfo("NOTICE!!", "Invalid First Name")
                return
            if len(self.first_name)>10:
                messagebox.showinfo("NOTICE!!", "First Name too long")
                return

            if not self.last_name.isalpha():
                messagebox.showinfo("NOTICE!!", "Invalid Last Name")
                return

            if len(self.last_name)>10:
                messagebox.showinfo("NOTICE!!", "Last Name too long")
                return

            elif self.address.isdigit():
                messagebox.showinfo("NOTICE!!", "Invalid Address")
                return

            elif len(self.address)>20:
                messagebox.showinfo("NOTICE!!", "Address too long")
                return

            elif not self.student_id.isdigit():
                messagebox.showinfo("NOTICE!!", "Invalid Id!!.")
                return

            elif len(self.student_id) > 5:
                messagebox.showinfo("NOTICE!!", "Student ID must be less than 5 digits!")
                return
            elif not self.contact_number.isdigit():
                messagebox.showinfo("NOTICE!!", "Invalid Phone number.!!")
                return
            elif len(self.contact_number)  != 10:
                return messagebox.showerror('Error', 'Contact number must  be 10 digits!!')

            query = "insert into student values(%s,%s,%s,%s,%s,%s)"
            self.mycursor.execute(query, [self.student_id, self.first_name, self.last_name, self.degree,
                                          self.address, self.contact_number])

            messagebox.showinfo('Confirm', 'Data saved successfully')
            self.con.commit()
            self.show_data()

        except mysql.connector.IntegrityError:
            messagebox.showinfo('Duplicate Entry', 'Data already exits!!!')



    def delete_info(self):
       try:
           self.student_id = self.entrystudent_id.get()
           query = 'delete from student where student_id=%s'
           values = (self.student_id,)
           self.mycursor.execute(query, values)
           self.con.commit()
           self.show_data()
           self.clear_info()
           messagebox.showinfo('Deleted', 'Data deleted successfully')
       except ValueError:
           messagebox.showinfo('Notice', 'Nothing to delete')
           return

    def update_info(self):
       # try:
            query='update student set first_name=%s,last_name=%s,degree=%s,address=%s,contact_number=%s where student_id=%s'
            self.first_name = self.entryfirst_name.get()
            self.last_name = self.entrylast_name.get()
            self.degree = self.entry_degree.get()
            self.address=self.entry_address.get()
            self.contact_number = self.entrycontact_number.get()
            self.student_id =self.entrystudent_id.get()
            values=(self.first_name,self.last_name,self.degree,self.address,self.contact_number,self.student_id)
            self.mycursor.execute(query,values)
            self.con.commit()
            self.show_data()

            if self.first_name == '' or self.last_name == '' or self.degree == '' or self.address == '' or self.contact_number == '':
                messagebox.showerror('Error', 'Please fill all details to update')
                return

            if not self.first_name.isalpha():
                messagebox.showinfo("NOTICE!!", "Invalid First Name")
                return
            if len(self.first_name) > 10:
                messagebox.showinfo("NOTICE!!", "First Name too long")
                return

            if not self.last_name.isalpha():
                messagebox.showinfo("NOTICE!!", "Invalid Last Name")
                return

            if len(self.last_name) > 10:
                messagebox.showinfo("NOTICE!!", "Last Name too long")
                return

            elif self.address.isdigit():
                messagebox.showinfo("NOTICE!!", "Invalid Address")
                return

            elif len(self.address) > 20:
                messagebox.showinfo("NOTICE!!", "Address too long")
                return

            elif not self.student_id.isdigit():
                messagebox.showinfo("NOTICE!!", "Invalid Id!!.")
                return

            elif len(self.student_id) > 5:
                messagebox.showinfo("NOTICE!!", "Student ID must be less than 5 digits!")
                return

            elif not self.contact_number.isdigit():
                messagebox.showinfo("NOTICE!!", "Invalid Phone number.!!")
                return

            elif len(self.contact_number) !=10:
                return messagebox.showerror('Error', 'Contact number must  be 10 digits!!')


            else:
                query = 'update student set first_name=%s,last_name=%s,degree=%s,address=%s,contact_number=%s where student_id=%s'
                values = (
                self.first_name, self.last_name, self.degree, self.address, self.contact_number, self.student_id)
                self.mycursor.execute(query, values)
                self.con.commit()
                self.show_data()
                messagebox.showinfo('Updated', 'Data updated successfully')


    def sort_partition(self,all_data,low,high):
        self.entry_for_sort=self.combo_sort.get()
        if self.entry_for_sort=='First name':
            self.show_column_index=1
        elif self.entry_for_sort == "Last name":
            self.show_column_index = 2
        elif self.entry_for_sort == "Degree":
            self.show_column_index = 3
        elif self.entry_for_sort== "Student id":
            self.show_column_index = 0
        elif self.entry_for_sort=="Address":
            self.show_column_index=4
        num = (low - 1)
        pivot = all_data[high][self.show_column_index]
        for value in range(low, high):
            if all_data[value][self.show_column_index] <= pivot:
                num = num + 1
                all_data[num], all_data[value] = all_data[value], all_data[num]

        all_data[num + 1], all_data[high] = all_data[high], all_data[num + 1]
        return (num + 1)

    def Quick_sort(self, all_data, low, high):
        if low < high:
            self.Part_sort=self.sort_partition(all_data,low,high)
            self.Quick_sort(all_data, low, self.Part_sort-1)
            self.Quick_sort(all_data, self.Part_sort+1, high)

    def sorting_info(self):
        self.entry_for_sort =self.combo_sort.get()
        if self.entry_for_sort:
            query="select * from student"
            self.mycursor.execute(query)
            self.fetch_outputs=self.mycursor.fetchall()
            print(self.fetch_outputs)
            self.Quick_sort(self.fetch_outputs, 0, len(self.fetch_outputs)-1)
            self.student_table.delete(*self.student_table.get_children())
            for value in self.fetch_outputs:
                self.student_table.insert("", 'end', values=value)
                self.con.commit()
        else:
            messagebox.showinfo("Notice", "Please enter the data to sort")

    def info_search(self,mylist=None):
        if not mylist:
            query = "select * from student"
            self.mycursor.execute(query)
            self.output_query = self.mycursor.fetchall()
        else:
            self.output_query = mylist

        self.get_search = self.combo_search.get()
        self.search_value = self.entry_search.get()
        if self.get_search == "Student id":
            self.show_column_index = 0
        elif self.get_search == "First name":
            self.show_column_index = 1
        elif self.get_search == "Last name":
            self.show_column_index = 2
        elif self.get_search == "Degree":
            self.show_column_index = 3
        elif self.get_search == "Address":
            self.show_column_index = 4
        else:
            messagebox.showinfo("Notice", "Please enter the data to search")
            return

        self.list_of_output_data = []
        for value in self.output_query:
            print(value)
            if self.search_value == str(value[self.show_column_index]):
                self.list_of_output_data.append(value)

        self.student_table.delete(*self.student_table.get_children())
        for value in self.list_of_output_data:
            self.student_table.insert("", 'end', values=value)
            self.con.commit()

        if not self.list_of_output_data:
            messagebox.showinfo("Notice", "Data not found")

        return self.list_of_output_data

    def clear_info(self):
        self.entrystudent_id.config(state='normal')
        self.entrystudent_id.delete(0,END)
        self.entryfirst_name.delete(0,END)
        self.entrylast_name.delete(0, END)
        self.entry_degree.set('')
        self.entry_address.delete(0,END)
        self.entrycontact_number.delete(0,END)
        self.combo_search.set('')
        self.combo_sort.set('')
        self.entry_search.delete(0,END)

    def pointer(self, event):

        point=self.student_table.focus()
        content=self.student_table.item(point)
        row=content['values']
        self.clear_info()
        self.entrystudent_id.insert(0,row[0])
        self.entryfirst_name.insert(0,row[1])
        self.entrylast_name.insert(0, row[2])
        self.entry_degree.set(row[3])
        self.entry_address.insert(0,row[4])
        self.entrycontact_number.insert(0,row[5])
        self.entrystudent_id.config(state='disabled')

    def show_data(self):
           query='select * from student'
           self.mycursor.execute(query)
           rows=self.mycursor.fetchall()
           self.student_table.delete(*self.student_table.get_children())
           for row in rows:
               self.student_table.insert('',END,values=row)

    def Exit(self):
        self.root.destroy()
        exit()


if __name__ == '__main__':
    gui = Tk()
    root = Student(gui)
    gui.title('Student Information System')
    gui.geometry('1000x700')
    gui.resizable(False, False)
    gui.mainloop()
