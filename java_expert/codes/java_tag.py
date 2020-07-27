# Parse input file and print fields relevant to questions (post id).

import sys
import xml.sax
import os

# To extract posts that are questions
questionId = "1"

class StackContentHandler(xml.sax.ContentHandler):

    def __init__(self, tag):
        xml.sax.ContentHandler.__init__(self)
        self.tag = "<" + tag + ">"

    def startElement(self, name, attrs):

        if name != "row":
            return

        # Get post type from the input file
        ptype = "__none__"
        if "PostTypeId" in attrs:
            ptype = attrs.getValue("PostTypeId")

        # Check if the posts types are answers or not. If not answers, then skip.
        if ptype != questionId:
            return

        # Get post id and tags
        id = "__none__"
        if "Id" in attrs:
            id = attrs.getValue("Id")
        tags = "__none__"
        if "Tags" in attrs:
            tags = attrs.getValue("Tags")

        # Skip posts without a matching tag
        if not self.tag in tags:
            return

        line = []
        line.append(id)
        print ("\t".join(line))

        # Write output in file
        with open("java_tag.txt", "a") as output:
            for row in line:
                output.write(str(row)+'\t')
            output.write('\n')

if __name__ == '__main__':

    # Delete previous output file "java_tag.txt", if it exists
    if os.path.exists("java_tag.txt"):
        os.remove("java_tag.txt")

    if len(sys.argv) < 3:
        print ("Usage: " + sys.argv[0] + " <file> <tag>")
        sys.exit(1)



    fname = sys.argv[1]
    tag = sys.argv[2]

    f = open(fname, encoding = 'utf-8')
    xml.sax.parse(f, StackContentHandler(tag))
