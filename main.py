import pandas as pd
from random import randrange

class RandomProblemExtractor:
    def __init__(self):
        self.problems = []

    def extract_problems(self,filename):
        df = pd.read_excel(filename)  # sheetname is optional

        i = 0
        while i < len(df):
            num = int(df['번호'][i])
            prob = str(df['문제'][i])
            answer = str(df['답'][i])
            next_i = i + 1
            while next_i < len(df) and df['번호'][next_i] != df['번호'][next_i]:
                if df['문제'][next_i] == df['문제'][next_i] :
                    prob += ('\n' + str(df['문제'][next_i])) 
                if df['답'][next_i] == df['답'][next_i]:
                    answer += ('\n' + str(df['답'][next_i])) 
                next_i += 1
            i = next_i
            self.problems.append((num, prob, answer))

    def problem_set(self):
        print(self.problems)

    def extract_ramdom_problems(self, number_of_problems):
        new_problems = []
        for i in range(0, number_of_problems):
            index = randrange(len(self.problems))
            prob = self.problems[index][1]
            ans = self.problems[index][2]
            new_problems.append((i + 1, prob, ans))
            self.problems.remove(self.problems[index])

        return new_problems

    def save_to_csv(self, samples):
        df = pd.DataFrame(samples, columns=['번호', '문제', '답'])
        print(samples)
        print(df['답'])
        #df.to_csv('problems.csv', index=False)  # index=False prevents pandas to write row index
        df.to_excel('problems.xlsx')

def main():
    p = RandomProblemExtractor()
    p.extract_problems('chap1.xlsx')
    p.extract_problems('chap2.xlsx')
    samples = p.extract_ramdom_problems(20)
    #print(samples)
    p.save_to_csv(samples)
    #p.problem_set()

if __name__ == '__main__':
    main()
