import lxml.html

settings = dict(SCRAPELIB_RPM = 20)

metadata = dict(
    name='Connecticut',
    capitol_timezone='America/New_York',
    abbreviation='ct',
    legislature_name='Connecticut General Assembly',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    terms=[
        {'name': '2011-2012',
         'sessions': ['2011', '2012'],
         'start_year': 2011, 'end_year': 2012},
    ],
    session_details={
        '2011': {
            'display_name': '2011 Regular Session',
            '_scraped_name': '2011',
        },
        '2012': {
            'display_name': '2012 Regular Session',
            '_scraped_name': '2012',
        }
    },
    feature_flags=['subjects', 'events', 'influenceexplorer'],
    _ignored_scraped_sessions=['2005', '2006', '2007', '2008', '2009', '2010',
                               ]
)

def session_list():
    import scrapelib
    text = scrapelib.urlopen('ftp://ftp.cga.ct.gov')
    sessions = [line.split()[-1] for line in text.splitlines()]
    sessions.remove('incoming')
    sessions.remove('pub')
    return sessions

def extract_text(doc, data):
    doc = lxml.html.fromstring(data)
    text = ' '.join(p.text_content() for p in doc.xpath('//body/p'))
    return text
