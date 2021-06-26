import statistics
import plotly.figure_factory as pf
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('StudentsPerformance.csv')
readingScore = df["reading score"].to_list()

mean1 = statistics.mean(readingScore)
median1 = statistics.median(readingScore)
mode1 = statistics.mode(readingScore)
stand1 = statistics.stdev(readingScore)

print("Mean : ", mean1)
print("Median : ", median1)
print('Mode: ', mode1)
print("Standard Deviation : " , stand1)


#WITHIIN ONE ITERATION:
start1 = stand1 - mean1
end1 = stand1 + mean1
n1 = []

for i in readingScore:
    if i > start1 and i < end1:
        n1.append(i)

print(len(n1)/len(readingScore)*100, '% of the data lies within one standard deviation.')


#WITHIIN TWO ITERATIONS:
start2 = stand1 - 2*mean1
end2 = stand1 + 2*mean1
n2 = []

for i in readingScore:
    if i > start2 and i < end2:
        n2.append(i)

print(len(n2)*100/len(readingScore), '% of the data lies within two standard deviations.')

#WITHIIN THREE ITERATION:
start3 = stand1 - 3*mean1
end3 = stand1 + 3*mean1
n3 = []

for i in readingScore:
    if i > start3 and i < end3:
        n3.append(i)

print(len(n3)/len(readingScore)*100, '% of the data lies within three standard deviations.')

graph = pf.create_distplot([readingScore], ['Reading Score'], show_hist=False)
graph.add_trace(go.Scatter(x = [mean1,mean1], y = [0,1], 
    mode = "lines", name = "Orignal Standard Deviation 1"))
graph.add_trace(go.Scatter(x = [statistics.mean(n1),statistics.mean(n1)], y = [0,1], 
    mode = "lines", name = "St Dev 1"))
graph.add_trace(go.Scatter(x = [statistics.mean(n2),statistics.mean(n2)], y = [0,1], 
    mode = "lines", name = "St Dev 2"))
graph.add_trace(go.Scatter(x = [statistics.mean(n3),statistics.mean(n3)], y = [0,1], 
    mode = "lines", name = "St Dev 2"))
graph.show()
