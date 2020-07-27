# Parse input file and print fields relevant to questions
# (post id, owner id and accepted answer id) in TSV format.

import sys
import xml.sax
import os

# To extract posts that are questions
questionId = "1"

class StackContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):

        if name != "row":
            return

        # Get post type from the input file
        ptype = "__none__"
        if "PostTypeId" in attrs:
            ptype = attrs.getValue("PostTypeId")

        # Check if the posts types are questions or not. If not questions, then skip.
        if ptype != questionId:
            return

        # Get post id, owner id and accepted answer id
        id = "__none__"
        if "Id" in attrs:
            id = attrs.getValue("Id")
        owner = "__none__"
        if "OwnerUserId" in attrs:
            owner = attrs.getValue("OwnerUserId")
        accepted = "__none__"
        if "AcceptedAnswerId" in attrs:
            accepted = attrs.getValue("AcceptedAnswerId")

        line = []
        line.append(id)
        line.append(owner)
        line.append(accepted)
        print ("\t".join(line))

        # Write output in file
        with open("ques.txt", "a") as output:
            for row in line:
                output.write(str(row)+'\t')
            output.write('\n')

if __name__ == '__main__':

    # Delete previous output file "ques.txt", if it exists
    if os.path.exists("ques.txt"):
        os.remove("ques.txt")

    if len(sys.argv) < 2:
        print ("Usage: ", sys.argv[0])
        print("<file>")
        sys.exit(1)

    fname = sys.argv[1]

    f = open(fname, encoding = 'utf-8')
    xml.sax.parse(f, StackContentHandler())
