
library("ggplot2")

setwd("/Users/pushkarsawant/Desktop/R programming")
data<-read.csv("P2-Movie-Ratings.csv")
head(data)

str(data)
summary(data)


data[,"film"]=as.integer(data[,"film"])
data$Year.of.release=factor(data$Year.of.release)
summary(data)
colnames(data)<-c("film","genre","critics_rating","audience_rating","budget_million","year")

ggplot(data=data,aes(x=critics_rating,y=audience_rating,
                     color=genre,size=budget_million)) +
  geom_point()+labs(x = "Critics Rating", y = "Audience Rating") +
  ggtitle("Relationship between Critics Rating And Audience Rating")


w<-ggplot(data=data,aes(x=critics_rating,y=audience_rating,color=genre))
w+geom_point(size=3)+
  facet_grid(genre~year)+labs(x = "Critics Rating", y = "Audience Rating") +
  ggtitle("Relationship on the basis of Genre and Year of Release")



nrow(data)
#linear regeression model y=mx+c --> (y=18.1237+0.5436*x)
#model 1
models<-lm(budget_million~audience_rating,data=data)
models

ggplot(data=data,aes(x=audience_rating,y=budget_million))+geom_point()+
  geom_smooth(method="lm")+labs(x = "Audience Rating", y = "Budget Million") +
  ggtitle("Audience Rating VS Movie Budget (Million)")+
  annotate("text", x = 3, y = 250, label = "italic(r) ==  0.1880778", parse = T, size = 6.5)
plot(models)
summary(models) 

#prediction
predict(models)
#y=mx+c      y= 18.1237 +(0.5436) *X   
estimated_budget<-0.5436*(88)+18.1237 
estimated_budget
audience_rat=data.frame(audience_rating=44.78)
predict(models,audience_rat)



#correlation
cor(data$budget_million,data$audience_rating)

cor(data$budget_million,data$critics_rating)





v<-ggplot(data=data,aes(x=budget_million))
v+geom_histogram(binwidth = 10,aes(fill=genre),color="Black")+
  facet_grid(genre~.,scale='free')+labs(x = "Movie Budget", y = "Count of Movies") +
  ggtitle("Count of Movies on the basis of budget")


sum(is.na(data))


#model 2
linear_model=lm(budget_million~critics_rating,data=data)
linear_model

ggplot(data=data,aes(x=critics_rating,y=budget_million,color="Red"))+geom_point(color="Blue")+
  geom_smooth(method="lm")+ggtitle("Critics Rating VS Movie Budget (Million)")+
  labs(x = "Critics Rating", y = "Movie Budget (Million)")+
  annotate("text", x = 3, y = 250, label = "italic(r) ==  0.01175477", parse = T, size = 6.5)
summary(linear_model)

install.packages("dplyr")
library(dplyr)
head(data)
df1<-group_by(data,genre,year)
newdf<-summarise(df1,cor(critics_rating,audience_rating),cor(budget_million,critics_rating),cor(budget_million,audience_rating))
newdf[,]

df2<-group_by(data,genre,year)
newdf_<-summarise(df2,mean(budget_million),mean(critics_rating),mean(audience_rating),max(budget_million),max(critics_rating),max(audience_rating),sum(budget_million))
newdf_[,]
mean(data$audience_rating)
mean(data$critics_rating)
filter(data,audience_rating<mean(audience_rating) & budget_million>mean(budget_million) & critics_rating<mean(critics_rating))$film
filter(data,audience_rating>mean(audience_rating) & budget_million<mean(budget_million) & critics_rating>mean(critics_rating))$film



#linear_model=lm(budget_million~critics_rating,data=data)
linear_model




summary(data)















