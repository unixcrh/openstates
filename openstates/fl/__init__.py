from billy.utils.fulltext import text_after_line_numbers
import lxml.html


metadata = dict(
    name='Florida',
    abbreviation='fl',
    capitol_timezone='America/New_York',
    legislature_name='Florida Legislature',
    chambers = {
        'upper': {'name': 'Senate', 'title': 'Senator'},
        'lower': {'name': 'House', 'title': 'Representative'},
    },
    terms=[
        {'name': '2011-2012',
         'sessions': ['2011', '2012', '2012B'],
         'start_year': 2011, 'end_year': 2012}],
    session_details={
        '2011': {'display_name': '2011 Regular Session',
                 '_scraped_name': '2011',
                },
        '2012': {'display_name': '2012 Regular Session',
                 '_scraped_name': '2012',
                },
        '2012B': {'display_name': '2012 Extraordinary Apportionment Session',
                 '_scraped_name': '2012B',
                },
    },
    feature_flags=['influenceexplorer'],
    _ignored_scraped_sessions=['2010O', '2010A', '2012O', '2013'],
)


def session_list():
    from billy.scrape.utils import url_xpath
    return url_xpath('http://flsenate.gov', '//option/text()')


def extract_text(doc, data):
    doc = lxml.html.fromstring(data)
    pre = doc.xpath('//pre')
    if pre:
        text = pre[0].text_content().encode('ascii', 'replace')
        return text_after_line_numbers(text)
    else:
        return '\n'.join(x.text_content() for x in doc.xpath('//tr/td[2]'))
