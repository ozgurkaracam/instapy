
class Test:

    def __init__(self):
        self.a = ["a", "b"]
        self.b = ["a","c"]
        print(self.Diff(self.a,self.b))

    def Diff(self,li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif

if __name__ == '__main__':
    # f=open('notfollowers.txt')
    # w=0
    # for i in f:
    #     w=w+1
    # print(w)
    testt=["özgür","karaçam","www"]
    f=open('notfollowers.txt',"w")
    for i in testt:
        f.write(i+"\n")
    f.close()
