 


class Evaluate:
    def totalmarks(self,maths,physics,chemistry,computer):
        total=int(maths)+int(physics)+int(chemistry)+int(computer)
        return total



    def cutoff(self,maths,physics,chemistry):
        maths=int(maths)/2
        physics=int(physics)/4
        chemistry=int(chemistry)/4
        cutoff=maths+physics+chemistry
        return cutoff

    def findgrade(self,average):
        if average<=40:
            grade='D'
            return grade
        if average>40 and average <=60:
            grade='C'
            return grade
        if average>60 and average<=80:
            grade='B'
            return grade
        if average>80 and average<=100:
            grade='A'
            return grade
        else:
            return False

    
