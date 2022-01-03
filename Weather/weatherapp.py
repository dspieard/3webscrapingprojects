from bs4 import BeautifulSoup
import requests

def main():
	url = "https://weather.com/weather/today/l/NLXX0003:1:NL"
	conditions_list =[]
	file = "conditions.txt"

	result = requests.get(url)
	full_site = BeautifulSoup(result.content, "html.parser")
	current_conditions = full_site.find(class_="CurrentConditions--phraseValue--2Z18W")

	def append_to_list():
		with open(file, "r") as g:
			for line in g:
				conditions_list.append(line[:-1])

	def appent_to_file():
		with open(file, "a") as f:
			if current_conditions.text not in conditions_list:
				f.write(f"{current_conditions.text}\n")

	try: 
		append_to_list()
		appent_to_file()
	except:
		appent_to_file()


if __name__ == "__main__":
	main()