from cbpricechecker import CBPriceChecker

# Variables (change this!)
url = "https://www.coolblue.nl/product/837297/logitech-g915-lightspeed-wireless-rgb-mechanical-gaming-toetsenbord-gl-tactile-qwerty.html" # link to MM product
filename = "L915.csv" # File where it stores the values (run the script every day to keep up-to-date info)
htmlname = "L915.html" # The html path + name which you can use in a Dashticz frame
name = "Logitech 915"


product = CBPriceChecker(name,url,filename,htmlname)
product.writetofile()
product.creategraph()
product.createhtml()
