import urllib.request as Request
import urllib.error as Error
import xml.etree.ElementTree as ET

def get():
    # Get the RSS URL
    print('<<<<<Terminal RSS Feed Reader>>>>>')
    news_url = input('Please enter your feed URL (Leave blank to cancel): ')
    print()
    return news_url

def parse(news_url):
    """Read and output the RSS feed from {url}"""
    try:
        # Reading the URL Response
        with Request.urlopen(news_url) as response:
            xml = response.read()
    except (ValueError, Error.URLError) as e:
        print('An Error Occured:\n',e,'\n')
    else:
        try:
            # Parsing the read response
            root = ET.fromstring(xml)
        except ET.ParseError:
            print('An Error Occured:\nIt is not a valid XML file.')
        else:
            # Displaying the news feed
            for item in root.findall('./channel/item'):
                title = item.find('title').text
                description = item.find('description').text
                link = item.find('link').text
                print('Title:',title)
                print('Description:',description)
                print('Link:',link)
                print('\n')

def main():
    url=get()
    while url != '':
        parse(url)
        url=get()

if __name__ == "__main__":
  
    # calling main function
    main()
