from itertools import combinations
from py_timer import py_timer

class find_combo:
    def __init__(self, lst, num):
        self.lst=lst
        self.num=num

    def combo(self):
        return combinations(self.lst,self.num)

    def sum_combo(self):
        result={}
        for item in self.combo():
            if sum(item) not in result:
                result[sum(item)]=[item]
            else:
                result[sum(item)].append(item)
        return result

    def diff_combo(self):
        result={}
        for item in self.combo():
            if abs(item[0]-item[1]) not in result:
                result[abs(item[0]-item[1])]=[item]
            else:
                result[abs(item[0]-item[1])].append(item)
        return result
    
    @py_timer
    def show_me_result(self, num):
        summy=self.sum_combo()
        diffy=self.diff_combo()
        return {'sum':summy.get(num),'diff':diffy.get(num)}

    @py_timer
    def summarize(self, threshold):
        sum_key=list(filter(lambda x: x<=threshold, self.sum_combo().keys()))
        diff_key=list(filter(lambda x: x<=threshold, self.diff_combo().keys()))
        common_key=list(filter(lambda x: x in diff_key, sum_key))
        return sum_key, diff_key, common_key
