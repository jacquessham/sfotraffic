suppressMessages(library(tidyverse))
suppressMessages(library(magrittr))
suppressMessages(library(zoo))
suppressMessages(library(ggplot2))
suppressMessages(library(treemapify))
suppressMessages(library(scales))

path <- "/Users/jacquessham/Documents/SelfProjects/SFOTraffic"
setwd(path)
# Load Data into dataframe
airtraffic <- read.csv("Air_Traffic_Passenger_Statistics.csv")

####################### Data Cleaning #######################

# Change the column names for the convenience
names(airtraffic) <- c("date","op_airlines","op_code","pub_airlines",
                          "pub_code","geo_summ","geo_region","type",
                          "price","terminal","boarding_area","pax_count")
airtraffic$year <- as.integer(substr(airtraffic$date, 1, 4))
airtraffic$month <- substr(airtraffic$date, 5, 6) %>% factor(labels = month.name)

# Look at the published airlines name first
unique(airtraffic$pub_airlines)
# Notice we want to convert "United Airlines - Pre 07/01/2013" to United Airlines

## Let's do some data cleaning
# Merge "United Airlines - Pre 07/01/2013" to "United Airlines"
airtraffic$pub_airlines %<>% recode("United Airlines - Pre 07/01/2013" = "United Airlines")
# Remove the strip of "Emirates "
airtraffic$pub_airlines %<>% recode("Emirates " = "Emirates")
# Change "Other" in price column to "Full Service" to differentiate with Low Cost Carrier
airtraffic$price %<>% recode("Other" = "Full Service") 
# Some airlines were wrongly identified in category
# Convert the below airlines to full service/Low Fare
full_svc_airline <- c("Air China", "Air India Limited", "Air New Zealand", "Air Pacific Limited dba Fiji Airways",
                      "Emirates", "United Airlines", "Virgin America", "Volaris Airlines", "Delta Air Lines",
                      "US Airways")

lcc_svc_airline <- c("XL Airways France", "WOW Air", "WestJet Airlines")
# Convert price type to full service and low fare(LCC)
airtraffic %<>%
  mutate(cat_temp = ifelse(pub_airlines %in% full_svc_airline, "Full Service", 
                           ifelse(pub_airlines %in% lcc_svc_airline, "Low Fare", as.character(price)))) %>% 
  mutate(price = as.factor(cat_temp))

####################### EDA #######################
pax_year <- airtraffic %>% 
  group_by(year) %>% 
  summarise(sumpax = sum(pax_count))
pax_year %<>% slice(2:n()) 

# Line Graph for passenger count
pax_year %>% group_by(year) %>% ggplot() +
  geom_line(aes(x = year, y = sumpax/1000000, group = 1, color = "red")) +
  ggtitle("SFO Passenger Count between 2005 and 2017") +
  theme_minimal() + theme(legend.position="none") +
  scale_x_discrete(name = "Year") +
  scale_y_discrete(name = "Passengers (Millions)")

growth_rate <- function(x){
  rate <- x / lag(x) - 1
  return (rate)
}
growth_rate_year <- pax_year %>% 
  mutate(growth = growth_rate(sumpax))

growth_rate_year %<>% slice(3:n())

# Bar Chart for passengers year by year
airtraffic %>%
  group_by(geo_summ, month) %>%
  summarise(avg_pax = round(mean(pax_count), digit = 0)) %>% 
  ggplot(aes(x = factor(month, labels = month.abb), y = avg_pax, fill = geo_summ)) +
  geom_bar(stat = "identity", alpha = 0.8) +
  theme_minimal() +
  scale_y_continuous(labels = comma) + 
  scale_fill_discrete(name = "Destination", label = c("Domestic","International")) +
  labs(x = "Month", y = "Passengers") +
  ggtitle("Monthly Average Passengers Count") +
  geom_text(aes(label = format(avg_pax, big.mark = ",")), size = 2.75,
            position = position_stack(vjust = 0.5), colour = "white")


# Line Graph for growth rate
growth_rate_year %>% group_by(year) %>% ggplot() +
  geom_line(aes(x = year, y = growth, group = 1, color = "blue")) +
  ggtitle("SFO Passenger Count between 2005 and 2017") +
  theme_minimal() + theme(legend.position="none") +
  scale_x_discrete(name = "Year") +
  scale_y_continuous(name = "Growth Rate (%)", labels = scales::percent)

# Pie Chart for passenger type
total_traffic <- airtraffic %>%
  summarise(total_traffic = sum(pax_count)) %>% 
  as.numeric()

airtraffic %>%
  group_by(type) %>%
  summarise(traffic = sum(pax_count)) %>% 
  ggplot(aes(x = "", y = traffic, fill = type)) +
  geom_bar(width = 1 , stat = "identity") +
  geom_text(aes(x = 1, y = cumsum(traffic) - traffic / 2, label = percent(traffic / total_traffic))) +
  coord_polar(theta = "y") +
  theme_void() +
  scale_fill_brewer(palette = "Set2", name = "Activity Type", label = c("Arrival", "Departure", "Transit")) +
  ggtitle("Percentage of Airplane Activities") 

# Aggregate the number for domestic
top5_dom_list <- airtraffic %>%
  filter(geo_summ == "Domestic") %>%
  group_by(pub_airlines) %>%
  summarise(total_pax = sum(pax_count)) %>%
  top_n(5, total_pax) %>%
  arrange(total_pax) %>% 
  select(-total_pax)
# SW, VA, DL, AA, UA

# Aggregate the number for international
top5_intl_list <- airtraffic %>%
  filter(geo_summ == "International") %>%
  group_by(pub_airlines) %>%
  summarise(total_pax = sum(pax_count)) %>%
  top_n(5, total_pax) %>%
  arrange(total_pax) %>% 
  select(-total_pax)
# CX, BA, LH, AC, UA

# Look at the domestic lcc
dom_lcc_plot <- airtraffic %>% 
  filter(geo_summ == "Domestic" & 
           price =="Low Fare" &
           pub_airlines != "ATA Airlines" &
           pub_airlines != "Servisair" &
           pub_airlines != "Sun Country Airlines" &
           pub_airlines != "Trego Dugan Aviation") %>% 
  group_by(year,pub_airlines) %>% 
  summarise(sumpax = sum(pax_count)) %>% 
  arrange(desc(sumpax))

# Look at the international lcc
intl_lcc_plot <- airtraffic %>% 
  filter(geo_summ == "International" & 
           price =="Low Fare" &
           pub_airlines != "ATA Airlines" &
           pub_airlines != "Servisair" &
           pub_airlines != "Sun Country Airlines") %>% 
  group_by(year,pub_airlines) %>% 
  summarise(sumpax = sum(pax_count)) %>% 
  arrange(desc(sumpax))

intl_lcc_plot %>% ggplot(aes(x = year, y = sumpax, fill = pub_airlines)) +
  scale_fill_brewer(name = "Airline", palette = "Spectral") +
  geom_bar(stat = "identity") + 
  scale_x_discrete(name = "Year",
                     breaks = seq(min(airtraffic$year), max(airtraffic$year), by = 1)) +
  scale_y_continuous(name = "Passengers", breaks = seq(0, 500000, by = 50000), labels = comma)+
  ggtitle("The Annual Passengers Count on International Low Cost Carrier")+
  theme_minimal()

# Terminal Traffic
airtraffic %>%
  filter(geo_summ == "Domestic", !is.na(pub_code) & year == 2017) %>%
  group_by(terminal, pub_airlines, pub_code) %>%
  summarise(all_pax = sum(pax_count)) %>% 
  ggplot(aes(area = all_pax, fill = terminal, label = pub_code, group = pub_airlines)) +
  geom_treemap() +
  geom_treemap_text(colour = "white", place = "centre") +
  scale_fill_brewer(name = "Terminal", palette = "Set2") +
  ggtitle("Domestic Passengers Count by Airline and Terminal")

# United Passenger count
airtraffic %>%
  filter(pub_code == "UA" & year >= 2007) %>%
  group_by(month, year) %>%
  summarise(Passengers = sum(pax_count)) %>%
  ggplot(aes(x = factor(month, labels = month.abb), y = year)) +
  geom_tile(aes(fill = Passengers)) + 
  scale_x_discrete(name = "Month") +
  scale_y_continuous(expand = c(0, 0), name = "Year", breaks = seq(min(airtraffic$year), max(airtraffic$year), by = 1)) +
  scale_fill_gradientn(colours = rev(heat.colors(10)), labels = comma) +
  theme_minimal() +
  ggtitle("United Airlines Passengers Count")