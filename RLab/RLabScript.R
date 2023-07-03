#To see the working directory
# To run the R command just goto command line and press Ctrl=Enter
# or Press Run menu on the top-right.
getwd()

#This will set my workin directory to c:/Courses/CompFunda
#You should choose your own folder, where your data file is located
setwd("C:/Courses/compFunda")

#Reading the csv file from the working directory, storing the table/data
#frame into data object

data = read.csv(file="dataNW2.csv", header=T)
#After Running this command, see on the top-right panel, where data object 
#or dataframe in R lingo, with 807 rows and 11 variables are loaded into RAM
#You can click on the data df to see the loaded data in grid view, if you want

#This will show you the first 6 rows of data object

head(data)

#This will show you the structure of each variable, data type etc.

str(data)

#This will help to pick the individual varaible name without attaching it to Data
#otherwise, you need to write,e.g., data$UnitPrice to work with UnitPrice variable.

attach(data)
#Converting ShipCity and Country variable into Factor or categorical data
data$ShipCity=as.factor(ShipCity)
data$Country=as.factor(Country)

#Different types of plots examples
plot(data)
plot(Unitprice,Qty)
boxplot(Stock~ShipCity)
boxplot(Stock~Country, col=c(1:21))

unique(Country)

#Checking for correlation between unitprice and stock
plot(Unitprice,Stock)
cor(Unitprice,Stock)


summary(data)
summary(Country)

by(data, Country, summary)

mean(Unitprice)
sd(Unitprice)

help(mean)

table(Country,ShipCity)

#Adding new fielw in the DF to separate the sales region between US and the Rest
data$Region <- ifelse(data$Country=="USA", 1, 0)

#Running regression model
reg.res<-lm(Qty~Unitprice+Stock+Region, data = data)

summary(reg.res)
coef(reg.res)
