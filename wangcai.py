# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, web

def main(wf):
    url = "http://www.91wangcai.com/mobile/borrows"
    r = web.get(url)
    r.raise_for_status()

    root = r.json()
    for ele in root["data"]:
        try:
            title = ele["name"]
            nid = ele["borrow_nid"]
            apr = ele["borrow_apr"]
            period = ele["borrow_period"]
            progress = ele["borrow_account_scale"]
            href = "http://www.91wangcai.com/view/borrow/%s" % nid
            subtitle = u"年化 %s%% 期限 %s个月 投标进度 %s%%" % (apr, period, progress)
            wf.add_item(title = title,
                subtitle = subtitle,
                arg = href,
                valid = True,
                icon = ICON_WEB)
        except:
            print "failed", ele
    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
