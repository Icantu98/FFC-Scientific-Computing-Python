class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        n = '\n'
        s = ''
        sep = ('{:*>'+str(self.width)+'}').format('')
        for i in range(self.height):
            s = s + sep + n
        return s

    def get_amount_inside(self, shape):
        x_w = int(self.width/ shape.width)
        y_h = int(self.height/ shape.height)
        return x_w * y_h
    
    def __str__(self):
        return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"




class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length
    
    def set_side(self, length):
        self.width = length
        self.height = length
    

    def __str__(self):
        return "Square(side="+str(self.width)+")"