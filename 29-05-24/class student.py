class student:
    
    def __init__(self,roll,name,phone,address):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.address = address
    
    def displayInfo(self):
        print("Name:",self.name,"Address:",self.address)
        
st1=student(2160,'kranthi',34567890,'wgl')
st1.displayInfo()

