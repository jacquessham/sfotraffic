suppressMessages(library(tidyverse))
suppressMessages(library(magrittr))
suppressMessages(library(zoo))
suppressMessages(library(ggplot2))
suppressMessages(library(treemapify))
suppressMessages(library(scales))

# Load Data into dataframe
path <- "/Users/jacquessham/Documents/GitHub/sfotraffic/Data"
setwd(path)
cargotraffic <- read.csv("Air_Traffic_Cargo_Statistics_2024.csv")

# Change the column names for the convenience
names(cargotraffic) <- c("date","period_startdate","op_airlines","op_code","pub_airlines",
                       "pub_code","geo_summ","geo_region","activity_type","cargo_type",
                       "aircraft_type","weight_lbs","weight_tons","data_asof","data_loaded_at")
cargotraffic$year <- as.integer(substr(cargotraffic$date, 1, 4))
cargotraffic$month <- substr(cargotraffic$date, 5, 6) %>% factor(labels = month.name)


# Data Cleansing
unique(cargotraffic$pub_airlines)
unique(cargotraffic$cargo_type)
unique(cargotraffic$aircraft_type)
# Merge "United Airlines - Pre 07/01/2013" to "United Airlines"
cargotraffic$pub_airlines %<>% recode("United Airlines - Pre 07/01/2013" = "United Airlines")
# Merge "Northwest Airlines (became Delta)" to "Delta Air Lines"
cargotraffic$pub_airlines %<>% recode("Northwest Airlines (became Delta)" = "Delta Air Lines")

####################### EDA #######################
# Look at the annual cargo tonnage
cargo_year <- cargotraffic %>% group_by(year) %>% summarise(sumcargo = sum(weight_tons))


# Line Graph for cargo tonnage
cargo_year[cargo_year$year < 2024,] %>% group_by(year) %>% ggplot() +
  geom_line(aes(x = ts(year), y = sumcargo/1000, group = 1, color = "red")) +
  ggtitle("SFO Cargo Tonnage between 1999 and 2023") +
  theme_minimal() + theme(legend.position="none") +
  scale_x_continuous(name = "Year", breaks= pretty_breaks()) +
  scale_y_continuous(name = "Cargo (1,000 Tons)", breaks= pretty_breaks())

# Pie Chart for Cargo type
filter_year <- 2010
total_tonnage <- cargotraffic[cargotraffic$year >= filter_year,] %>% summarise(total_tonnage = sum(weight_tons)) %>% as.integer()
cargotype_traffic <- cargotraffic[cargotraffic$year >= filter_year,]


cargotype_traffic %>% group_by(cargo_type) %>%
  summarise(type_traffic = sum(weight_tons)) %>%
  ggplot(aes(x = "", y = type_traffic, fill = cargo_type)) +
  geom_bar(width = 1 , stat = "identity") +
  coord_polar(theta = "y") +
  theme_void() +
  scale_fill_brewer(palette = "Set2", name = "Cargo Type", label = c("Cargo", "Express", "Mail")) +
  ggtitle("Percentage of Cargo Type") +
  geom_text(aes(x = 1, label = percent(type_traffic / total_tonnage)), position = position_stack(vjust = .5))
