from mmpricechecker import MMPriceChecker

# Variables (change this!)
url = "https://www.mediamarkt.nl/nl/product/_logitech-g-g915-wireless-rgb-gaming-keyboard-1636088.html" # link to MM product
filename = "L915.csv" # File where it stores the values (run the script every day to keep up-to-date info)
htmlname = "L915.html" # The html path + name which you can use in a Dashticz frame
name = "Logitech 915"


product = MMPriceChecker(name,url,filename,htmlname)
product.writetofile()
product.creategraph()
product.createhtml()
