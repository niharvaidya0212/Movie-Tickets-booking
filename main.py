class BookTicket:

    def __init__(self):
        print("Enter the number of rows:")
        self.rows=int(input())
        print("Enter the number of seats in each row:")
        self.seats=int(input())
        self.l=[]
        self.userlist=[]
        self.currentincome=0
        self.noticketpurchased=0
        for i in range(self.rows):
            l1=['S']*self.seats
            l2=[{}]*self.seats
            self.l.append(l1)
            self.userlist.append(l2)
        self.menu()
        

    def show_seats(self):
        count=1
        print("\n\t\t\tSEATS\n")
        for n in range(1,self.seats+1):
            if n==1:
                print('\t%d'%(n),end='\t')
            else:
                print(n,end='\t')
        print('\n')
        for i in self.l:
            print(count,end='\t')
            count+=1
            for j in i:
                print(j,end='\t')
            print('\n')
    
    def user(self):
        self.name=input('\nEnter your name:')
        self.gender=input('Enter your gender:')
        self.age=int(input('Enter your age:'))
        self.phone=int(input('Enter your phone number:'))

    def available(self,a,b):
    	if a<=self.rows and b<=self.seats:
    		return True
    
    def buy(self):
        self.user_row=int(input('\nEnter the row of your seat:'))
        self.user_seat=int(input('Enter the seat number:'))
        if self.available(self.user_row,self.user_seat):
        	print('\nRow',self.user_row,' seat number:',self.user_seat)
        	#self.priceofticket(self.user_row)
        	print("Cost of the seat is $",self.priceofticket(self.user_row))
        	answer=input('\nChoose \'Yes\' or \'No\' to proceed :')
        
        	if self.l[self.user_row-1][self.user_seat-1]=='S':
        	    if (answer=='Yes' or answer=='yes'):
        	        self.user()
        	        self.l[self.user_row-1][self.user_seat-1]='B'
        	        self.userlist[self.user_row-1][self.user_seat-1]={'name':self.name,'gender':self.gender,'age':self.age,'phone':self.phone}
        	        print("Your Ticket is booked")
        	        self.currentincome+=self.priceofticket(self.user_row)
        	        self.noticketpurchased+=1
        	else:
        	    print("The seat is already booked")
        else:
        	print("\n!!!!!!Seat doesn't exist!!!!!!")
  
    
    def priceofticket(self,a):
        if self.rows*self.seats<=60:
            self.price=10
        else:
            if a<=(self.rows//2):
                self.price=10
            else:
                self.price=8
        return self.price

    def seat_info(self):
    	a=int(input("\nEnter the row no.:"))
    	b=int(input("Enter the seat no.:"))
    	if self.available(a,b):
    		if self.l[a-1][b-1]=='B':
    			c=self.userlist[a-1][b-1]
    			print('Name:',c['name'])
    			print('Gender:',c['gender'])
    			print('Age:',c['age'])
    			print('Phone no.:',c['phone'])
    		else:
    			print("The seat is empty/available")
    	else:
    		print("\n!!!!!!Seat doesn't exist!!!!!!")

    def statistics(self):
    	self.totalincome=0
    	for i in range(1,self.rows+1):
    		self.totalincome+=self.priceofticket(i)*self.seats
    	percentage=(self.currentincome/self.totalincome)*100

    	print("\nNo. of tickets purchased",self.noticketpurchased)
    	print("percentage",percentage)
    	print("current income: $",self.currentincome)
    	print('Total income: $',self.totalincome)

    
    def menu(self):
        print('\n1.Show the seats\n2.Buy a ticket\n3.Statistics\n4.Show booked ticket user info\n0.Exit')
        choice=int(input("Enter the choice:"))
        if choice==1:
            self.show_seats()
            self.menu()
        elif choice==2:
            self.buy()
            self.menu()
        elif choice==3:
        	self.statistics()
        	self.menu()
        elif choice==4:
        	self.seat_info()
        	self.menu()
        elif choice==0:
        	return None

movie1=BookTicket()