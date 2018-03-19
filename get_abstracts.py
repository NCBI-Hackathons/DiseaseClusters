import urllib2, json
from Bio import Entrez
from Bio import Medline
import re

Entrez.email = "trivneel211@gmail.com"
max_res = 100
format = 'PubTator'
bioconcept = "Disease" # can be "Gene,Mutation,Disease"
accep_pub_types = ["Journal Article", "Clinical Trial"] #add more if needed
hallmark_queries = ['proliferation receptor',#add fuzzy matching
                    'growth factor',
                    'cell cycle',
                    'contact inhibition',
                    'apoptosis',
                    'necrosis',
                    'autophagy',
                    'senescence',
                    'immortalization',
                    'angiogenesis',
                    'angiogenic factor',
                    'metastasis',
                    'mutation',
                    'DNA repair',
                    'adducts',
                    'DNA damage',
                    'inflammation',
                    'oxidative stress',
                    'warburg effect',
                    'growth',
                    'activation',
                    'immune system']
test_queries = ['Autistic behavior',
                'Restrictive behavior',
                'Impaired social interactions',
                'Poor eye contact',
                'Impaired ability to form peer relationships',
                'No social interaction',
                'Impaired use of nonverbal behaviors',
                'Lack of peer relationships',
                'Stereotypy']


def fetch_medline_records(idlist, type):
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode=type)
    records = Medline.parse(handle)

    records = list(records)
    return records


def pubmed_query(max_res, query=""):
    handle = Entrez.esearch(db="pubmed", term=query, rettype="medline", retmode="text", retmax=max_res)
    record = Entrez.read(handle)
    handle.close()
    idlist = record["IdList"]
    return idlist


def read_url(url, as_str=True):
    if as_str:
        urllib_result = urllib2.urlopen(url)
        res = urllib_result.read()
        return res
    else:
        return urllib2.urlopen(url)

def get_records(query):
    handle = Entrez.esearch(db="pubmed", term=query, rettype="medline", retmode="text", retmax=max_res)
    record = Entrez.read(handle)
    handle.close()
    idList = record['IdList']
    records = fetch_medline_records(idList, "text")#this is a Python list
    return records
    #for record in records:
        #print(record.get("AB", "?"))
        #print("\n")

def get_pmids(query):
    handle = Entrez.esearch(db="pubmed", term=query, rettype="medline", retmode="text", retmax=max_res)
    record = Entrez.read(handle)
    handle.close()
    idList = record['IdList']
    return idList


def disease_extract(records):# uses PubTator (MEDIC disease dictionary)
    disease_pattern = re.compile(r"Disease\tD\w\w\w\w\w\w")
    for record in records:
        #if record.get("PT", "?") in accep_pub_types:
        pmid = record.get("PMID", "?")
        url_Submit = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/" + bioconcept + "/" + pmid + "/" + format + "/"
        url_result = urllib2.urlopen(url_Submit)
        res = url_result.read()
        raw_mesh = re.findall(disease_pattern, res)
        cooked_mesh = [mention.replace("Disease\t", "") for mention in raw_mesh]  # this is called a list comprehension
        cooked_mesh = list(set(cooked_mesh))  # only keep unique disease ids
        print(cooked_mesh)



def rsid_extract(records):
    rsid_pattern = re.compile(r"rs\d+ Mutation")
    for record in records:
        pmid = record.get("PMID", "?")
        url_Submit = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/" + "Mutation" + "/" + pmid + "/" + format + "/"
        url_result = urllib2.urlopen(url_Submit)
        res = url_result.read()
        raw_mesh = re.findall(rsid_pattern, res)
        cooked_mesh = [mention.replace("rs", "") for mention in raw_mesh]
        cooked_mesh = [mention.replace("Mutation", "") for mention in raw_mesh]
        cooked_mesh = list(set(cooked_mesh))
        print(cooked_mesh)

#Test Code
for query in test_queries:
    print(query)
    records = get_records(query)
    for record in records:
        print(record.get("PMID", "?"))