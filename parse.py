def parseCommentLabels(commentLabels):
    commentsLabel = {}
    for label in commentLabels:
        commentsLabel[label.get('name')]= int(label.get('count'))
    return commentsLabel

def parseCookie(Cookie):
    cookie_dic = {}
    for i in Cookie.split('; '):
        cookie_dic[i.split('=')[0]] = i.split('=')[1]
    return cookie_dic