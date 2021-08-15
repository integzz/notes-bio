library(ggplot2)
library(readr)
library(dplyr)
library(patchwork)

adv = read_csv('https://raw.githubusercontent.com/gitony0101/X4DS/main/data/Advertising.csv')

p1 <- ggplot(data = adv, mapping = aes(x = TV, y = sales)) +
  geom_point(color = 'red') + 
  geom_smooth(method = "lm")

p2 <- ggplot(data = adv, mapping = aes(x = radio, y = sales)) +
  geom_point(color = 'red') + 
  geom_smooth(method = "lm")

p3 <- ggplot(data = adv, mapping = aes(x = newspaper, y = sales)) +
  geom_point(color = 'red') + 
  geom_smooth(method = "lm")

p1 + p2 + p3
