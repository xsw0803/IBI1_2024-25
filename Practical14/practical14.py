import xml.dom.minidom
import xml.sax
from datetime import datetime

ontologies = ['molecular_function', 'biological_process', 'cellular_component']
xml_file = 'go_obo.xml'

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ''
        self.current_namespace = ''
        self.current_id = ''
        self.current_name = ''
        self.is_a_count = 0
        self.max_terms = {}
        for ontology in ontologies:
            self.max_terms[ontology] = ('', '', 0)

    def startElement(self, tag, attributes):
        self.current_element = tag

    def characters(self, content):
        if self.current_element == 'namespace':
            self.current_namespace += content
        elif self.current_element == 'id':
            self.current_id += content
        elif self.current_element == 'name':
            self.current_name += content
        elif self.current_element == 'is_a':
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == 'term':
            if self.current_namespace in self.max_terms:
                if self.is_a_count > self.max_terms[self.current_namespace][2]:
                    self.max_terms[self.current_namespace] = (self.current_id, self.current_name, self.is_a_count)
            self.current_namespace = ''
            self.current_id = ''
            self.current_name = ''
            self.is_a_count = 0
        self.current_element = ''


print("Parsing with DOM...")
start_time = datetime.now()

dom_tree = xml.dom.minidom.parse('go_obo.xml')
terms = dom_tree.getElementsByTagName('term')
max_terms = {}
for ontology in ontologies:
    max_terms[ontology] = ('', '', 0)

for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue
    term_name = term.getElementsByTagName('name')[0].firstChild.nodeValue
    is_a_count = len(term.getElementsByTagName('is_a'))

    if namespace in max_terms and is_a_count > max_terms[namespace][2]:
        max_terms[namespace] = (term_id, term_name, is_a_count)

end_time = datetime.now()
dom_time = end_time - start_time
for ontology, (term_id, term_name, count) in max_terms.items():
    print(f'[DOM] {ontology}:\n {term_id} <{term_name}> Max number:{count} is_a.')

print(f'DOM parsing time: {dom_time.total_seconds():.4f} seconds.\n')

print("Parsing with SAX...")
start_time = datetime.now()
handler = GOHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(xml_file)
end_time = datetime.now()
sax_time = end_time - start_time
for ontology, (term_id, term_name, count) in handler.max_terms.items():
    print(f'[SAX] {ontology}:\nID: {term_id} Name:<{term_name}> Max number:{count} is_a.')

print(f'SAX parsing time: {sax_time.total_seconds():.4f} seconds.\n')

# SAX method is faster.
if dom_time < sax_time:
    print('DOM method is faster.')
elif sax_time < dom_time:
    print('SAX method is faster.')
else:
    print('Both methods are the same.')
# SAX method is faster.