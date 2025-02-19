class Solution:


    def get_all_string_list(self, s: str, n: int, mylist: list) -> None:
        if len(s)==n:
            mylist.append(s)
            return
        if s[-1]=='a':
            self.get_all_string_list(s+'b',n,mylist)
            self.get_all_string_list(s+'c',n,mylist)
        elif s[-1]=='b':
            self.get_all_string_list(s+'a',n,mylist)
            self.get_all_string_list(s+'c',n,mylist)
        else:
            self.get_all_string_list(s+'a',n,mylist)
            self.get_all_string_list(s+'b',n,mylist)
        return
        




    def getHappyString(self, n: int, k: int) -> str:
        mylist=[]
        self.get_all_string_list('a',n,mylist)
        self.get_all_string_list('b',n,mylist)
        self.get_all_string_list('c',n,mylist)
        if len(mylist)<k:
            return ""
        return mylist[k-1]

