from bs4 import BeautifulSoup

with open("file.html", "r") as f:
    improve = f.read()

soup = BeautifulSoup(improve, "html.parser")

#returns the entire html file in a beautifuly indented and structured manner
print(soup.prettify()) 

''' print soup.prettify is a must use command otherwise generates bugs '''

#all commands regarding TITLE


#returns the title of the website with title tag 
print(soup.title)       

#returns the title of the website with title tag 
print(soup.title.text)

#there is one more method to retrieve name of the website
print(soup.title.name)

#get the name of the title tag
print("Title tag name:", soup.title.name)

#get the string within the title tag (if any string present there)
print("Title tag string:", soup.title.string) 

#get the name of the parent tag of title   
print("Parent tag of title:", soup.title.parent.name)



#all commanda regarding paragraph


#accessing the first paragraph tag  
print("First paragraph tag:", soup.p)

#accessing the class attribute of the first paragraph
print("Class of First paragraph:", soup.p['class'])

#accessing frist anchor tag
print("First anchor tag:", soup.a)

#searching all the anchor tags
print("All anchor tags:", soup.find_all('a'))

#finding the tag using id leftie
print("Tag with id leftie", soup.find(id="leftie"))

#there are multiple commands, above are the majority of the commands used while accessing data with scraping 