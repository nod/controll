from tornado.web import UIModule
from .. import models
from urllib import quote

class SurveyPie(UIModule):
    def render(self, surveykey, answer):
        col =  models.SurveyResponse._collection
        key = 'answers.%s'%answer

        grouped = col.group(
            key = { key : 1 },
            condition =  { },
            reduce = 'function(obj,prev) { prev.count += 1; }',
            initial =  { 'count': 0 },
            )
        lbls, vals = [],[]

        for x in grouped:
            lbls.append(x[key])
            vals.append(x['count'])

        # now clean up labels
        total = sum(vals)
        for i in xrange(0,len(lbls)):
            L = lbls[i]
            lbls[i] = "%s %0.0f%%" % (L, vals[i]/total*100)

        return ("<div class='little-box'>"
            "<h3> %s </h3>"
            '<img src="'
            "https://chart.googleapis.com/chart?cht=p3"
            "&chd=t:%s"
            "&chs=280x100"
            "&chl=%s"
            "&chf=bg,s,ffffff00&chdls=ffffff,12"
            '"/></div>'
            )% ( answer, ",".join(map(str,vals)), "|".join(map(quote,lbls)) )


