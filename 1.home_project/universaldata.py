class Universal:

   def bookdata(self,a,b,c,d,e) -> None:
      
        with open('books.txt','r') as self.f:
           trs= self.f.read()
    
           self.a=a;self.b=b;self.c=c;self.d=d;self.e=e 
           if len(trs)==0:
              st= str(a+' '+b+' '+c+' '+d+' '+e)
           else:
              st= str('\n'+a+' '+b+' '+c+' '+d+' '+e) 
        with open('books.txt','a') as self.f:        
           self.f.write(st)
           print('\n'+'Malumot mufaqiyatli qoyildi')

   def computerdata(self,a,b,c,d,e):
        #computer=====================================
        with open('computer.txt','r') as self.f:
           trs= self.f.read()
    
           self.a=a;self.b=b;self.c=c;self.d=d;self.e=e 
           if len(trs)==0:
              st= str(a+' '+b+' '+c+' '+d+' '+e)
           else:
              st= str('\n'+a+' '+b+' '+c+' '+d+' '+e) 
        with open('computer.txt','a') as self.f:        
           self.f.write(st)
           print('\n'+'Malumot mufaqiyatli qoyildi')
   def televisiondata(self,a,b,c,d,e):       
        #television====================================
        with open('teletvdata.txt','r') as self.f:
           trs= self.f.read()
    
           self.a=a;self.b=b;self.c=c;self.d=d;self.e=e 
           if len(trs)==0:
              st= str(a+' '+b+' '+c+' '+d+' '+e)
           else:
              st= str('\n'+a+' '+b+' '+c+' '+d+' '+e) 
        with open('teletvdata.txt','a') as self.f:        
           self.f.write(st)
           print('\n'+'Malumot mufaqiyatli qoyildi')
   def homedata(self,a,b,c,d,e):         
        #home=========================================
        with open('homedata.txt','r') as self.f:
           trs= self.f.read()
    
           self.a=a;self.b=b;self.c=c;self.d=d;self.e=e 
           if len(trs)==0:
              st= str(a+' '+b+' '+c+' '+d+' '+e)
           else:
              st= str('\n'+a+' '+b+' '+c+' '+d+' '+e) 
        with open('homedata.txt','a') as self.f:        
           self.f.write(st)
           print('\n'+'Malumot mufaqiyatli qoyildi') 
   def bankdata(self,a,b,c,d,e):         
        #bank========================================
        with open('bankdata.txt','r') as self.f:
           trs= self.f.read()
    
           self.a=a;self.b=b;self.c=c;self.d=d;self.e=e 
           if len(trs)==0:
              st= str(a+' '+b+' '+c+' '+d+' '+e)
           else:
              st= str('\n'+a+' '+b+' '+c+' '+d+' '+e) 
        with open('bankdata.txt','a') as self.f:        
           self.f.write(st)
           print('\n'+'Malumot mufaqiyatli qoyildi')         
                      
           
class Getone(Universal):
        
         def showbooks(self,textdata):
           with open(f'{textdata}.txt','r') as self.f:
               st = self.f.read()
               print(st)
         def deletedatalist(self,textdata):
            with open(f'{textdata}.txt','r') as self.f:
               sr = self.f.readlines()
               print(type(sr))
               son = int(input('Son >>> '))
               sr.pop(son)
               for el in sr:
                 if el=="\n":
                   sr.remove(el)
    
            with open(f'{textdata}.txt','w') as self.f:  
                newd=''
                for el in sr:
                  newd+=el
                self.f.write(newd) 
                print('\n'+'Data ochirildi. ')      

         def updatedata(self,textdata): 
           with open(f'{textdata}.txt','rt') as  self.f:
               data=self.f.read() 
  
               tef = input('Enter the old word. ')
               fet = input('Enter the new word. ')
  
               data=data.replace(tef, fet)
           with open(f'{textdata}.txt','wt') as  self.f: 

               self.f.write(data) 
               print('Update changed successifully.')
             
              
                            
llist=Getone()

print('***************************************************************')
print('*  Write   ***   Write    ***   Write  ***  Write  ***  Write *')
print('*  book.   ***  computer. ***  teleTv. ***  home.  ***  bank. *')
print('***************************************************************')


temo =input('Variantni tanlang: ')
textdata=input('Enter the name of filename. ')

match temo:

  case 'book': 
    
      print('******************************************************')
      print('* Add_data ***  Show_data *** Delete_d  *** Update_d *')
      print('* click_1. ***  click_2.  *** click_3   *** click_4  *')
      print('******************************************************')
      
      
      son1 = int (input('Enter: '))
      match son1:
        case 1:
          print('Enter the data regarding books')
    
          a=input('Name: ')
          b=input('Year: ')
          c=input('Auther: ')
          d=input('Now_cost: ')
          e=input('Summer: ')
          llist.bookdata(a,b,c,d,e)
        case 2:
           llist.showbooks(textdata)
        case 3:
           llist.deletedatalist(textdata)   
        case 4:
           llist.updatedata(textdata)   
  case 'computer':
      print('******************************************************')
      print('* Add_data ***  Show_data *** Delete_d  *** Update_d *')
      print('* click_1. ***  click_2.  *** click_3   *** click_4  *')
      print('******************************************************')
      
      
      son1 = int (input('Enter: '))
      match son1:
        case 1:
          print('Enter the data regarding computer ')
    
          a=input('Name: ')
          b=input('Year: ')
          c=input('Auther: ')
          d=input('Now_cost: ')
          e=input('Summer: ')
          llist.computerdata(a,b,c,d,e)
        case 2:
           llist.showbooks(textdata)
        case 3:
           llist.deletedatalist(textdata)   
        case 4:
           llist.updatedata(textdata)
  case 'teleTv':   
      print('******************************************************')
      print('* Add_data ***  Show_data *** Delete_d  *** Update_d *')
      print('* click_1. ***  click_2.  *** click_3   *** click_4  *')
      print('******************************************************')
      
      
      son1 = int (input('Enter: '))
      match son1:
        case 1:
          print('Enter the data regarding books')
    
          a=input('Name: ')
          b=input('Year: ')
          c=input('Auther: ')
          d=input('Now_cost: ')
          e=input('Summer: ')
          llist.televisiondata(a,b,c,d,e)
        case 2:
           llist.showbooks(textdata)
        case 3:
           llist.deletedatalist(textdata)   
        case 4:
           llist.updatedata(textdata) 
  case 'home':  

      print('******************************************************')
      print('* Add_data ***  Show_data *** Delete_d  *** Update_d *')
      print('* click_1. ***  click_2.  *** click_3   *** click_4  *')
      print('******************************************************')
      
      
      son1 = int (input('Enter: '))
      match son1:
        case 1:
          print('Enter the data regarding books')
    
          a=input('Name: ')
          b=input('Year: ')
          c=input('Auther: ')
          d=input('Now_cost: ')
          e=input('Summer: ')
          llist.homedata(a,b,c,d,e)
        case 2:
           llist.showbooks(textdata)
        case 3:
           llist.deletedatalist(textdata)   
        case 4:
           llist.updatedata(textdata)
  case 'bank':
      print('******************************************************')
      print('* Add_data ***  Show_data *** Delete_d  *** Update_d *')
      print('* click_1. ***  click_2.  *** click_3   *** click_4  *')
      print('******************************************************')
      
      
      son1 = int (input('Enter: '))
      match son1:
        case 1:
          print('Enter the data regarding books')
    
          a=input('Name: ')
          b=input('Year: ')
          c=input('Auther: ')
          d=input('Now_cost: ')
          e=input('Summer: ')
          llist.bankdata(a,b,c,d,e)
        case 2:
           llist.showbooks(textdata)
        case 3:
           llist.deletedatalist(textdata)   
        case 4:
           llist.updatedata(textdata)               

          


      

