# Parse input file and print fields relevant to questions
# (post id, owner id and accepted answer id) in TSV format.

import sys
import xml.sax
import os

# To extract posts that are answers
answerId = "2"

class StackContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):

        if name != "row":
            return

        # Get post type from the input file
        ptype = "__none__"
        # if attrs.has_key("PostTypeId"):
        if "PostTypeId" in attrs:
            ptype = attrs.getValue("PostTypeId")

        # only answers are relevant, skip elements with PostTypeId != answerId
        if ptype != answerId:
            return

        # extract post id and owner
        id = "__none__"
        # if attrs.has_key("Id"):
        if "Id" in attrs:
            id = attrs.getValue("Id")
        owner = "__none__"
        # if attrs.has_key("OwnerUserId"):
        if "OwnerUserId" in attrs:
            owner = attrs.getValue("OwnerUserId")

        line = []
        line.append(id)
        line.append(owner)
        print ("\t".join(line))

        #--Ahuti:
        with open("ans.txt", "a") as output:
            for row in line:
                output.write(str(row)+'\t')
            output.write('\n')

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print ("Usage: " + sys.argv[0] + " <file>")
        sys.exit(1)

    if os.path.exists("ans.txt"):
        os.remove("ques.txt")

    fname = sys.argv[1]
    #print fname

    # f = open(fname)
    f = open(fname, encoding = 'utf-8')
    xml.sax.parse(f, StackContentHandler())
