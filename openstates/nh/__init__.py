import lxml.html

metadata = {
    'abbreviation': 'nh',
    'name': 'New Hampshire',
    'capitol_timezone': 'America/New_York',
    'legislature_name': 'New Hampshire General Court',
    'chambers': {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    'terms': [
        {'name': '2011-2012', 'sessions': ['2011', '2012'],
         'start_year': 2011, 'end_year': 2012}
    ],
    'session_details': {
        '2011': {'display_name': '2011 Regular Session',
                 'zip_url': 'http://gencourt.state.nh.us/downloads/2011%20Session%20Bill%20Status%20Tables.zip',
                 '_scraped_name': '2011 Session',
                },
        '2012': {'display_name': '2012 Regular Session',
                 'zip_url': 'http://gencourt.state.nh.us/downloads/2012%20Session%20Bill%20Status%20Tables.zip',
                 '_scraped_name': '2012 Session',
                },
    },
    'feature_flags': ['influenceexplorer'],
}

def session_list():
    from billy.scrape.utils import url_xpath
    zips = url_xpath('http://gencourt.state.nh.us/downloads/',
                     '//a[contains(@href, "Bill%20Status")]/text()')
    return [zip.replace(' Bill Status Tables.zip', '') for zip in zips]

def extract_text(doc, data):
    doc = lxml.html.fromstring(data)
    return doc.xpath('//html')[0].text_content()
