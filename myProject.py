
from tkinter import*
import random
import time
import datetime
from tkinter import messagebox
import time
import datetime
root=Tk()
root.geometry("1350x750+0+0")
root.title("Cash Counter")



Tops = Frame(root, width=1350,height=100,bd=14,relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900,height= 650,bd=8,relief="raise")
f1.pack(side=LEFT)

f2 =Frame(root, width=440,height= 650,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

ft2 =Frame(f2, width=440,height=450,bd=12,relief="raise")
ft2.pack(side=TOP)

fb2 =Frame(f2, width=440,height=250,bd=5,relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a, width=400,height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)

f1ab=Frame(f1a, width=400,height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a, width=440,height=390,bd=16,relief="raise")
f2aa.pack(side=LEFT)

f2ab=Frame(f2a, width=440,height=390,bd=16,relief="raise")
f2ab.pack(side=RIGHT)

l=['violet','indigo','green','blue','orange','magenta','red','black','white']
fil=random.choice(l)

root.configure(background=fil)

Tops.configure(background=fil)
f1.configure(background=fil)
f2.configure(background=fil)
#######################################Receipt#############################33
def Reciept():
    txtReceipt.delete('1.0',END)
    x=random.randint(10908,500876)
    randomRef=str(x)
    Reciept_Ref.set('  BILL'+randomRef)
    txtReceipt.insert(END,'Receipt Ref:'+Reciept_Ref.get()+'  '+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t '+'Cost of Items \n\n')
    txtReceipt.insert(END, 'Aloo Tikki Burger: \t\t\t' + E_Aloo_Tikki_Burger.get()+'\n')
    txtReceipt.insert(END, 'Maha Veggie Burger: \t\t\t' +E_Maha_Veggie_Burger.get()+'\n')
    txtReceipt.insert(END, 'Premium Paneer Burger: \t\t\t' +E_Premium_Paneer_Burger.get()+'\n')
    txtReceipt.insert(END, 'Veggie Delight Footlong: \t\t\t' +E_Veggie_Delight_Footlong.get()+'\n')
    txtReceipt.insert(END, 'Cheese Footlong: \t\t\t' +E_Cheese_Footlong.get()+'\n')
    txtReceipt.insert(END, 'Paneer Tikka FootLong: \t\t\t' +E_Paneer_Tikka_FootLong.get()+'\n')
    txtReceipt.insert(END, 'Aloo Tikki+Fries+Coke: \t\t\t' +E_Combo.get()+'\n')
    txtReceipt.insert(END, 'Veg S.Burg+Coke+Fries: \t\t\t' +E_Veg_Special_Burger.get()+'\n')
    txtReceipt.insert(END, 'Mushroom Pizza: \t\t\t' +E_CoffeeCake.get()+'\n')
    txtReceipt.insert(END, 'Margherita Pizza: \t\t\t' +E_Margherita_Pizza.get()+'\n')
    txtReceipt.insert(END, 'Veggie Delight Pizza: \t\t\t' +E_Veggie_Delight_Pizza.get()+'\n')
    txtReceipt.insert(END, 'Paneer Tikka Pizza: \t\t\t' +E_Paneer_Tikka_Pizza.get()+'\n')
    txtReceipt.insert(END, 'T.Paneer Tikka Pizza: \t\t\t' +E_Teekha_Paneer.get()+'\n')
    txtReceipt.insert(END, 'Deluxe Veggie Pizza: \t\t\t' +E_Deluxe_Veggie_Pizza.get()+'\n')
    txtReceipt.insert(END, 'Mushroom Corn Delight: \t\t\t' +E_Mushroom_Corn_Delight.get()+'\n')
    txtReceipt.insert(END, 'Extravaganza: \t\t\t' +E_CranBerry.get()+'\n')
    txtReceipt.insert(END, 'Cost of Burgers:  \t' +CostofDrinks.get()+'    Tax Paid: '+Tax.get()+ '\n')
    txtReceipt.insert(END, 'Cost of Pizzas:  \t' +CostofCake.get()+'      SubTotal: '+SubTotal.get() + '\n')
    txtReceipt.insert(END, 'Service Charge:  \t' +ServiceCharge.get()+'   Total:  '+Total.get()+ '\n')





################################Heading#########################3

lblINFO= Label(Tops,font=('arial',70,'bold'), text= '               Menu Card                  ',bd=10)

lblINFO.grid(row=0,column=0)
####################Method#################
########################Cost#######################################3333
def CostofItem():
    Item1 = float(E_Aloo_Tikki_Burger.get())
    Item2 = float(E_Maha_Veggie_Burger.get())
    Item3 = float(E_Premium_Paneer_Burger.get())
    Item4 = float(E_Veggie_Delight_Footlong.get())
    Item5 = float(E_Cheese_Footlong.get())
    Item6 = float(E_Paneer_Tikka_FootLong.get())
    Item7 = float(E_Combo.get())
    Item8 = float(E_Veg_Special_Burger.get())

    Item9 = float(E_CoffeeCake.get())
    Item10 = float(E_Margherita_Pizza.get())
    Item11 = float(E_Veggie_Delight_Pizza.get())
    Item12= float(E_Paneer_Tikka_Pizza.get())
    Item13 = float(E_Teekha_Paneer.get())
    Item14 = float(E_Deluxe_Veggie_Pizza.get())
    Item15 = float(E_Mushroom_Corn_Delight.get())
    Item16 = float(E_CranBerry.get())

    PriceofDrinks=round((Item1*29)+(Item2*69)+(Item3*99)\
                        +(Item4*79) +(Item5*119)+(Item6*99)+(Item7*99)+(Item8*115))

    PriceofCakes=round((Item9*89)+(Item10*89)+(Item11*89)+(Item12*119)+(Item13*119)+(Item14*119)+(Item15*119)+(Item16*130))

    DrinksPrice='₹'+str((PriceofDrinks))
    CakesPrice='₹'+str((PriceofCakes))
    CostofCake.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)

    SC='₹ '+str((20))
    ServiceCharge.set(SC)

    SubTotalofItems='₹ '+ str((PriceofDrinks+PriceofCakes+20))
    SubTotal.set(SubTotalofItems)

    PaidTax=round((PriceofDrinks+PriceofCakes+20)*0.17,2)
    Tax.set(PaidTax)
    TT=((PriceofCakes+PriceofDrinks + 20)*0.17)
    Tc=round((PriceofDrinks+PriceofCakes+ 20 +TT),2)
    TC='₹ '+str(Tc)
    Total.set(TC)

def qExit():
   qExit= messagebox.askyesno('Quit System','Do you want to quit? ')
   if qExit>0:
       root.destroy()
       return
def Reset():
    Tax.set('')
    SubTotal.set('')
    Total.set('')
    CostofCake.set('')
    CostofDrinks.set('')
    ServiceCharge.set('')
    txtReceipt.delete('1.0',END)

    E_Aloo_Tikki_Burger.set('0')
    E_Maha_Veggie_Burger.set('0')
    E_Premium_Paneer_Burger.set('0')
    E_Veggie_Delight_Footlong.set('0')
    E_Cheese_Footlong.set('0')
    E_Paneer_Tikka_FootLong.set('0')
    E_Combo.set('0')
    E_Veg_Special_Burger.set('0')

    E_CoffeeCake.set('0')
    E_Margherita_Pizza.set('0')
    E_Veggie_Delight_Pizza.set('0')
    E_Paneer_Tikka_Pizza.set('0')
    E_Teekha_Paneer.set('0')
    E_Deluxe_Veggie_Pizza.set('0')
    E_Mushroom_Corn_Delight.set('0')
    E_CranBerry.set('0')

    var1.set('0')
    var2.set('0')
    var3.set('0')
    var4.set('0')
    var5.set('0')
    var6.set('0')
    var7.set('0')
    var8.set('0')
    var9.set('0')
    var10.set('0')
    var11.set('0')
    var12.set('0')
    var13.set('0')
    var14.set('0')
    var15.set('0')
    var16.set('0')

    txtAloo_Tikki_Burger.configure(state=DISABLED)
    txtMaha_Veggie_Burger.configure(state=DISABLED)
    txtPremium_Paneer_Burger.configure(state=DISABLED)
    txtVeggie_Delight_Footlong.configure(state=DISABLED)
    txtCheese_Footlong.configure(state=DISABLED)
    txtPaneer_Tikka_FootLong.configure(state=DISABLED)
    txtCombo.configure(state=DISABLED)
    txtVeg_Special_Burger.configure(state=DISABLED)

    txtCoffee_Cake.configure(state=DISABLED)
    txtMargherita_Pizza.configure(state=DISABLED)
    txtVeggie_Delight_Pizza.configure(state=DISABLED)
    txtPaneer_Tikka_Pizza.configure(state=DISABLED)
    txtTeekha_Paneer.configure(state=DISABLED)
    txtDeluxe_Veggie_Pizza.configure(state=DISABLED)
    txtMushroom_Corn_Delight.configure(state=DISABLED)
    txtCranBerry.configure(state=DISABLED)

############3checkButton#################
def check_Button():
    if (var1.get()==1):
        txtAloo_Tikki_Burger.configure(state=NORMAL)
    elif(var1.get()==0):
        txtAloo_Tikki_Burger.configure(state=DISABLED)
        E_Aloo_Tikki_Burger.set('0')
    if (var2.get()==1):
        txtMaha_Veggie_Burger.configure(state=NORMAL)
    elif (var2.get()==0):
        txtMaha_Veggie_Burger.configure(state=DISABLED)
        E_Maha_Veggie_Burger.set('0')
    if (var3.get()==1):
        txtPremium_Paneer_Burger.configure(state=NORMAL)
    elif (var3.get()==0):
        txtPremium_Paneer_Burger.configure(state=DISABLED)
        E_Premium_Paneer_Burger.set('0')

    if (var4.get()==1):
        txtVeggie_Delight_Footlong.configure(state=NORMAL)
    elif (var4.get()==0):
        txtVeggie_Delight_Footlong.configure(state=DISABLED)
        E_Veggie_Delight_Footlong.set('0')

    if (var5.get()==1):
        txtCheese_Footlong.configure(state=NORMAL)
    elif (var5.get()==0):
        txtCheese_Footlong.configure(state=DISABLED)
        E_Cheese_Footlong.set('0')
    if (var6.get()==1):
        txtPaneer_Tikka_FootLong.configure(state=NORMAL)
    elif (var6.get()==0):
        txtPaneer_Tikka_FootLong.configure(state=DISABLED)
        E_Paneer_Tikka_FootLong.set('0')
    if (var7.get()==1):
        txtCombo.configure(state=NORMAL)
    elif (var7.get()==0):
        txtCombo.configure(state=DISABLED)
        E_Combo.set('0')
    if (var8.get()==1):
        txtVeg_Special_Burger.configure(state=NORMAL)
    elif (var8.get()==0):
        txtVeg_Special_Burger.configure(state=DISABLED)
        E_Veg_Special_Burger.set('0')
    if (var9.get()==1):
        txtCoffee_Cake.configure(state=NORMAL)
    elif (var9.get()==0):
        txtCoffee_Cake.configure(state=DISABLED)
        E_CoffeeCake.set('0')
    if (var10.get()==1):
        txtMargherita_Pizza.configure(state=NORMAL)
    elif (var10.get()==0):

        txtMargherita_Pizza.configure(state=DISABLED)
        E_Margherita_Pizza.set('0')
    if (var11.get()==1):
        txtVeggie_Delight_Pizza.configure(state=NORMAL)
    elif (var11.get()==0):
        txtVeggie_Delight_Pizza.configure(state=DISABLED)
        E_Veggie_Delight_Pizza.set('0')
    if (var12.get()==1):
        txtPaneer_Tikka_Pizza.configure(state=NORMAL)

    elif (var12.get()==0):
        txtPaneer_Tikka_Pizza.configure(state=DISABLED)
        E_Paneer_Tikka_Pizza.set('0')
    if (var13.get()==1):
        txtTeekha_Paneer.configure(state=NORMAL)
    elif (var13.get()==0):
        txtTeekha_Paneer.configure(state=DISABLED)
        E_Teekha_Paneer.set('0')
    if (var14.get()==1):
        txtDeluxe_Veggie_Pizza.configure(state=NORMAL)
    elif (var14.get()==0):
        txtDeluxe_Veggie_Pizza.configure(state=DISABLED)
        E_Deluxe_Veggie_Pizza.set('0')
    if (var15.get()==1):
        txtMushroom_Corn_Delight.configure(state=NORMAL)
    elif (var15.get()==0):
        txtMushroom_Corn_Delight.configure(state=DISABLED)
        E_Mushroom_Corn_Delight.set('0')
    if (var16.get()==1):
        txtCranBerry.configure(state=NORMAL)
    elif (var16.get()==0):
        txtCranBerry.configure(state=DISABLED)
        E_CranBerry.set('0')


    #########################################VARIABLE###
a=16
b=22
c=2




##############Var###############
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()

var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()


DateofOrder=StringVar()
Reciept_Ref=StringVar()
Tax=StringVar()
SubTotal=StringVar()
Total=StringVar()
CostofCake=StringVar()
CostofDrinks=StringVar()
ServiceCharge=StringVar()


E_Aloo_Tikki_Burger=StringVar()
E_Maha_Veggie_Burger=StringVar()
E_Premium_Paneer_Burger=StringVar()
E_Veggie_Delight_Footlong=StringVar()
E_Cheese_Footlong=StringVar()
E_Paneer_Tikka_FootLong=StringVar()
E_Combo=StringVar()
E_Veg_Special_Burger=StringVar()

E_CoffeeCake=StringVar()
E_Margherita_Pizza=StringVar()
E_Veggie_Delight_Pizza=StringVar()
E_Paneer_Tikka_Pizza=StringVar()
E_Teekha_Paneer=StringVar()
E_Deluxe_Veggie_Pizza=StringVar()
E_Mushroom_Corn_Delight=StringVar()
E_CranBerry=StringVar()

E_Aloo_Tikki_Burger.set('0')
E_Maha_Veggie_Burger.set('0')
E_Premium_Paneer_Burger.set('0')
E_Veggie_Delight_Footlong.set('0')
E_Cheese_Footlong.set('0')
E_Paneer_Tikka_FootLong.set('0')
E_Combo.set('0')
E_Veg_Special_Burger.set('0')

E_CoffeeCake.set('0')
E_Margherita_Pizza.set('0')
E_Veggie_Delight_Pizza.set('0')
E_Paneer_Tikka_Pizza.set('0')
E_Teekha_Paneer.set('0')
E_Deluxe_Veggie_Pizza.set('0')
E_Mushroom_Corn_Delight.set('0')
E_CranBerry.set('0')

DateofOrder.set(time.strftime('%d/%m/%Y'))

##################################################Drinks###################################
Aloo_Tikki_Burger = Checkbutton(f1aa,text='Aloo Tikki Burger \t',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button).grid(row=0,sticky=W)

Maha_Veggie_Burger = Checkbutton(f1aa,text='Maha Veggie Burger \t',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button).grid(row=1,sticky=W)

Premium_Paneer_Burger = Checkbutton(f1aa,text='Premium Paneer Burger \t',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=2,sticky=W)
Veggie_Delight_Footlong = Checkbutton(f1aa,text='Veggie Delight FootLong \t',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button ).grid(row=3,sticky=W)
Cheese_Footlong = Checkbutton(f1aa,text='Cheese FootLong \t',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=4,sticky=W)
Paneer_Tikka_FootLong = Checkbutton(f1aa,text='Paneer Tikka FootLong \t',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button ).grid(row=5,sticky=W)
Combo = Checkbutton(f1aa,text='Aloo Tikki+fries+coke \t',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=6,sticky=W)
Veg_Special_Burger = Checkbutton(f1aa,text='Veg Surprise Burger+coke+fries    \t',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=7,sticky=W)

####################################################Cakes#########################################

CoffeeCake = Checkbutton(f1ab,text='Margherita Pizza \t',variable=var9,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button ).grid(row=1,sticky=W)

Margherita_Pizza = Checkbutton(f1ab,text='Veggie Delight Pizza \t',variable=var10,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button ).grid(row=2,sticky=W)
Veggie_Delight_Pizza = Checkbutton(f1ab,text='Paneer Tikka Pizza\t',variable=var11,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=3,sticky=W)
Paneer_Tikka_Pizza = Checkbutton(f1ab,text='Teekha Paneer Tikka \t',variable=var12,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=4,sticky=W)
Teekha_Paneer = Checkbutton(f1ab,text='Deluxe Veggie Pizza \t',variable=var13,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button ).grid(row=5,sticky=W)
Deluxe_Veggie_Pizza = Checkbutton(f1ab,text='Mushroom Corn Delight \t',variable=var14,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=6,sticky=W)
Mushroom_Corn_Delight = Checkbutton(f1ab,text='Veg Extravaganza \t',variable=var15,onvalue=1,offvalue=0,font=('arial',18,'bold'),command=check_Button ).grid(row=7,sticky=W)

CranBerry = Checkbutton(f1ab,text='Mushroom Pizza\t',variable=var16,onvalue=1,offvalue=0,font=('arial',18,'bold') ,command=check_Button).grid(row=0,sticky=W)
##########################################Entry widgets Drinks################################
txtAloo_Tikki_Burger= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                justify='left',textvariable=E_Aloo_Tikki_Burger,state= DISABLED)
txtAloo_Tikki_Burger.grid(row=0,column=1)
txtMaha_Veggie_Burger= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                justify='left',textvariable=E_Maha_Veggie_Burger,state= DISABLED)
txtMaha_Veggie_Burger.grid(row=1,column=1)
txtPremium_Paneer_Burger= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                     justify='left',textvariable=E_Premium_Paneer_Burger,state= DISABLED)
txtPremium_Paneer_Burger.grid(row=2,column=1)
txtVeggie_Delight_Footlong= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                      justify='left',textvariable=E_Veggie_Delight_Footlong,state= DISABLED)
txtVeggie_Delight_Footlong.grid(row=3,column=1)
txtCheese_Footlong= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                     justify='left',textvariable=E_Cheese_Footlong,state= DISABLED)
txtCheese_Footlong.grid(row=4,column=1)
txtPaneer_Tikka_FootLong= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                         justify='left',textvariable=E_Paneer_Tikka_FootLong,state= DISABLED)
txtPaneer_Tikka_FootLong.grid(row=5,column=1)
txtCombo= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                          justify='left',textvariable=E_Combo,state= DISABLED)
txtCombo.grid(row=6,column=1)
txtVeg_Special_Burger= Entry(f1aa,font=('arial',18,'bold'),bd=8,width=6,\
                          justify='left',textvariable=E_Veg_Special_Burger,state= DISABLED)
txtVeg_Special_Burger.grid(row=7,column=1)
#####################################Entry widget Cake#####################################
txtCoffee_Cake= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,\
                      justify='left',textvariable=E_CoffeeCake,state= DISABLED)
txtCoffee_Cake.grid(row=1,column=1)
txtMargherita_Pizza= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,\
                          justify='left',textvariable=E_Margherita_Pizza,state= DISABLED)
txtMargherita_Pizza.grid(row=2,column=1)
txtVeggie_Delight_Pizza= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,
                            justify='left',textvariable=E_Veggie_Delight_Pizza,state= DISABLED)
txtVeggie_Delight_Pizza.grid(row=3,column=1)
txtPaneer_Tikka_Pizza= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,
                            justify='left',textvariable=E_Paneer_Tikka_Pizza,state= DISABLED)
txtPaneer_Tikka_Pizza.grid(row=4,column=1)
txtTeekha_Paneer= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,
                               justify='left',textvariable=E_Teekha_Paneer,state= DISABLED)
txtTeekha_Paneer.grid(row=5,column=1)
txtDeluxe_Veggie_Pizza= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,
                                 justify='left',textvariable=E_Deluxe_Veggie_Pizza,state= DISABLED)
txtDeluxe_Veggie_Pizza.grid(row=6,column=1)
txtMushroom_Corn_Delight= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,\
                           justify='left',textvariable=E_Mushroom_Corn_Delight,state= DISABLED)
txtMushroom_Corn_Delight.grid(row=7,column=1)
txtCranBerry= Entry(f1ab,font=('arial',18,'bold'),bd=8,width=6,\
                    justify='left',textvariable=E_CranBerry,state= DISABLED)
txtCranBerry.grid(row=0,column=1)
##########################################################Info##########################################################
lblReceipt = Label(ft2,font=('arial',b,'bold'),text='Receipt',bd=c).grid(row=0,column=0,sticky=W)
txtReceipt = Text(ft2,font=('arial',11,'bold'),bd=c,width=90)
txtReceipt.grid(row=1,column=0)
###############Item Info#####################
lblCostofDrinks=Label(f2aa,font=('arial',a,'bold'),text='Cost of Burgers',bd=c)
lblCostofDrinks.grid(row=1,column=0,sticky=W)
txtCostofDrinks=Entry(f2aa,font=('arial',b,'bold'),bd=c,
                      justify='left',textvariable=CostofDrinks)
txtCostofDrinks.grid(row=1,column=1,sticky=W)

lblCostofCakes=Label(f2aa,font=('arial',a,'bold'),text='Cost of Pizzas',bd=8)
lblCostofCakes.grid(row=2,column=0,sticky=W)
txtCostofCakes=Entry(f2aa,font=('arial',b,'bold'),bd=c,
                     justify='left',textvariable=CostofCake)
txtCostofCakes.grid(row=2,column=1,sticky=W)

lblServiceCharge=Label(f2aa,font=('arial',a,'bold'),text='Service Charge',bd=8)
lblServiceCharge.grid(row=3,column=0,sticky=W)
txtServiceCharge=Entry(f2aa,font=('arial',b,'bold'),bd=c,
                      justify='left',textvariable=ServiceCharge)
txtServiceCharge.grid(row=3,column=1,sticky=W)
##########################Payment info###############
lblTax=Label(f2ab,font=('arial',a,'bold'),text='Tax',bd=c)
lblTax.grid(row=0,column=0,sticky=W)
txtTax=Entry(f2ab,font=('arial',b,'bold'),bd=c,
             justify='left',textvariable=Tax)
txtTax.grid(row=0,column=1,sticky=W)

lblSubTotal=Label(f2ab,font=('arial',a,'bold'),text='SubTotal',bd=c)
lblSubTotal.grid(row=1,column=0,sticky=W)
txtSubTotal=Entry(f2ab,font=('arial',b,'bold'),bd=c,
                  justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=1,column=1,sticky=W)

lblTotal=Label(f2ab,font=('arial',a,'bold'),text=' Total      ',bd=c)
lblTotal.grid(row=2,column=0,sticky=W)
txtTotal=Entry(f2ab,font=('arial',b,'bold'),bd=c,
               justify='left',textvariable=Total)
txtTotal.grid(row=2,column=1,sticky=W)

##########Button##################
btnTotal=Button(fb2,padx=b-4,pady=2,bd=3,fg=fil,font=('arial',16,'bold'),
                width=c,text='Total',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(fb2,padx=b+4,pady=2,bd=3,fg=fil,font=('arial',16,'bold'),
                  width=c,text='Receipt',command=Reciept).grid(row=0,column=1)
btnReset=Button(fb2,padx=b-4,pady=2,bd=3,fg=fil,font=('arial',16,'bold'),
                width=c,text='Reset',command=Reset).grid(row=0,column=2)
btnExit=Button(fb2,padx=b-4,pady=2,bd=3,fg=fil,font=('arial',16,'bold'),
               width=c,text='Exit',command=qExit).grid(row=0,column=3)


root.mainloop()
