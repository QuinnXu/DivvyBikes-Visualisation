library(jpeg)
library(ggplot2)
library(plyr)
library(dplyr)
library(gtable)
library(grid)
library(lubridate)

#load station data
station <- read.csv("Divvy_Stations_2017_Q1Q2.csv",header=T,sep=",")
trip <- read.csv("Divvy_Trips_2017_Q2.csv",header=T,sep=",")

#station frequency
frequency_start<- trip[c("from_station_id")]
colnames(frequency_start) <- 'a'
frequency_end <- trip[c("to_station_id")]
colnames(frequency_end) <- 'a'
frequency <- rbind(frequency_end,frequency_start)
frequency <- data.frame(table(frequency))
names(frequency) <- c('id','totaltrips')

#trip time
time <- trip$start_time
time <- mdy_hms(time)
timeby1minute <- floor_date(time,'minute')
byminute <- as.numeric(timeby1minute)
timefrequency <- data.frame(table(byminute))
timeby1hour <- floor_date(time,'hour')
byhour <- as.numeric(timeby1hour)
timefrequency <- data.frame(table(byhour))
####write.csv(timefrequency,file="tripsbyhour.csv")

#top10 
#Streeter Dr & Grand Ave
#Lake Shore Dr & Monroe St
#Lake Shore Dr & North Blvd
#Theater on the Lake
#Clinton St & Washington Blvd
#Clinton St & Madison St
#Michigan Ave & Oak St
#Millennium Park
#Canal St & Adams St
#Michigan Ave & Washington St

#station trip duration
nrow(trip %>% select(from_station_name,start_time,tripduration)%>%
                  filter(from_station_name=='Michigan Ave & Washington St')%>% 
                  filter(tripduration < 900))

nrow(trip %>% select(from_station_name,start_time,tripduration)%>%
       filter(from_station_name=='Michigan Ave & Washington St')%>% 
       filter(tripduration >= 900) %>% filter(tripduration <1800))

nrow(trip %>% select(from_station_name,start_time,tripduration)%>%
       filter(from_station_name=='Michigan Ave & Washington St')%>% 
       filter(tripduration >= 1800) %>% filter(tripduration <3600))

nrow(trip %>% select(from_station_name,start_time,tripduration)%>%
       filter(from_station_name=='Michigan Ave & Washington St')%>% 
       filter(tripduration >= 3600))

#station trip by day
text = 'Michigan Ave & Washington St'
byhour <- (trip %>% select(from_station_name,start_time)%>%
filter(from_station_name==text))
byhour$start_time <- floor_date(mdy_hms(byhour$start_time),'hour')
nrow(subset(byhour,format(start_time,'%H')=='00'))


#station online time
stationtotalinfo <-read.csv("station_totalinfo.csv",header=T,sep=",")
stationtotalinfo$online_date <- as.numeric(floor_date(mdy_hms(stationtotalinfo$online_date),'day'))
###write.csv(stationtotalinfo,file="onlinetime.csv")

#bike analysis
bikeid <- trip$bikeid
bikefrequency <- data.frame(table(bikeid))
bikeusedtimesfrequency <- data.frame(table(round(bikefrequency$Freq,-1)))
a <- as.data.frame(table(bikefrequency$Freq))
write.csv(a,file="bikeusedfreqency.csv")

#user: user type
usertype <- trip$usertype
typefrequency <-data.frame(table(usertype))

gender_ <- (trip %>% select(gender,usertype,birthyear) %>% filter(usertype=='Subscriber'))$gender
genderfrequency <-data.frame(table(gender_))

birthyear <- (trip %>% select(usertype,birthyear,gender) %>% filter(usertype=='Subscriber') %>% filter(gender==''))$birthyear
unknowbirthyearfrequency <-data.frame(table(birthyear))

birthyear <- (trip %>% select(usertype,birthyear,gender) %>% filter(usertype=='Subscriber') %>% filter(gender=='Male'))$birthyear
malebirthyearfrequency <-data.frame(table(birthyear))


birthyear <- (trip %>% select(usertype,birthyear,gender) %>% filter(usertype=='Subscriber') %>% filter(gender=='Female'))$birthyear
femalebirthyearfrequency <-data.frame(table(birthyear))

#user: relation between usertype&duration
duration_sub <- (trip %>% select(tripduration,usertype) %>% filter(usertype=='Subscriber'))$tripduration
durationfreq_sub <-data.frame(table(duration_sub))

duration_cus <- (trip %>% select(tripduration,usertype) %>% filter(usertype=='Customer'))$tripduration
durationfreq_cus <-data.frame(table(duration_cus))