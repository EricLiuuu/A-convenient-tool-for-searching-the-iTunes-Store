# A Convenient Program for Searching the iTunes Store

Highlights: Interactive command line tool, Class Inheritance, iTunes Store API

## Description

It's a small but fun Python program that make use of the iTunes Store API to display the searching results to users. 

This tool will first ask users for the search query (keywords) and fetch data from the iTunes Store. When it receives the data, the results will be displayed in a short but informative way in the terminal. The results will be divided into three categories: SONGS, MOVIES and OTHER MEDIA. Inside the code, there are three classes as well. The Media class is the parent class and the Song and the Movie classes are inherited from the Media class. Thus those two child classes contains more information compared to their parent class.

After that, users have three choices: 
* choose the id for different results for more details
* start a new search
* exit the program

If users choose to display the details for one result, the program will then open a corresponding iTunes Store webpage that shows more detailed information.

## Usage

Let's run the program first!

```
$ python3 Tool.py
```
The program will ask for the search query first. Now enter the keywords that you want to search for, such as 'Adam Lambert'.

```
Enter a search term, or "exit" to quit: Adam Lambert
```
Hit the ENTER! The program will display the searching results to the terminal like this: 
```
SONGS
1 Adam Lambert by Sin Synthetic (2009) [Alternative]
2 Whataya Want from Me by Adam Lambert (2009) [Pop]
3 Marry the Night (Glee Cast Version) [feat. Adam Lambert] by Glee Cast (2013) [Pop]       
4 If I Had You by Adam Lambert (2009) [Pop]
5 Gloria (Glee Cast Version) [feat. Adam Lambert] by Glee Cast (2014) [Pop]
...
48 Another Lonely Night by Adam Lambert (2015) [Pop]
49 Whataya Want from Me by Adam Lambert (2009) [Pop]
50 Pick U Up by Adam Lambert (2009) [Pop]

MOVIES

OTHER MEDIA

Enter a number for more info, or another search term, or exit:
```
There are only songs in the searching results in this case (of course). The iTunes Store API will return 50 results by default, and the available range is from 1 to 200. These short one-line results are consrtructed from the comprehensive JSON data fetched from the API. Each of them is labeled with a unique id, which can be used in the following steps.

Now, three choices: 

1. Choose a result and see more information about it
2. Continue searching for new contents
3. Quit the program

If you choose to see more information about one result, simply type the id of that result. For example:
```
Enter a number for more info, or another search term, or exit: 2
```
Then the program will automaticlly open the webpage for that specific result and display the following information in the terminal:
```
Launching
https://music.apple.com/us/album/whataya-want-from-me/340086422?i=340086791&uo=4
in web browser...
```
Enjoy the music!


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
