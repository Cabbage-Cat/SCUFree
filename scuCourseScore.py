import requests
import json
import scucas

def getCourseScoreJson(sess: requests.Session) -> bytes:
    res = sess.get('http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/thisTermScores/data')
    scoreLst = list(res.json()[0]['list'])
    jsonLst = list()
    for a in scoreLst:
        dct = dict(a)
        if dct.get('avgcj') != '':
            newDct = dict()
            newDct['课程名'] = dct['courseName']
            newDct['属性'] = dct['coursePropertyName']
            newDct['学分'] = dct['credit']
            newDct['成绩'] = dct['courseScore']
            newDct['绩点'] = dct['gradePoint']
            newDct['排名'] = dct['rank']
            newDct['最高成绩'] = dct['maxcj']
            newDct['最低成绩'] = dct['mincj']
            newDct['平均成绩'] = dct['avgcj']
            jsonLst.append(newDct)
    return json.dumps(jsonLst, ensure_ascii=False).encode('utf-8')