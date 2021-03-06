'''
@ author: jiarun Cao

Example of Indexing with PyLucene 3.0

'''

import os, sys, glob
import lucene
#from org.apache.lucene.store import SimpleFSDirectory
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version




# index all the file with pylucene
def luceneIndexer(docdir, indir):
    """frpFile
    IndexDocuments from a directory

    para:{
        docdir: the path of the txt file
        indir: the path of the index file which is generated by the following code
        }
    """

    lucene.initVM()
    DIRTOINDEX = docdir
    INDEXIDR = indir
    indexdir = SimpleFSDirectory(File(INDEXIDR))
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    index_writer = IndexWriter(indexdir, analyzer, True, \
                               IndexWriter.MaxFieldLength(512))
    #for tfile in glob.glob(os.path.join(DIRTOINDEX, '*.txt')):
    list = os.listdir(DIRTOINDEX)
    for i in range(len(list)):
        tfile = os.path.join(DIRTOINDEX, list[i])
        if os.path.isfile(tfile):
            print ("Indexing: ", tfile)
            print ('okokokook')
            document = Document()
            content = open(tfile, 'r').read()
            document.add(Field("text", content, Field.Store.YES, \
                               Field.Index.ANALYZED))
            document.add(Field("title",str(tfile.strip('.txt')),Field.Store.YES,\
                               Field.Index.ANALYZED))
            index_writer.addDocument(document)
            #print (document)
            print ("Done: ", tfile)
    index_writer.optimize()
    print (index_writer.numDocs())
    index_writer.close()

luceneIndexer('/home/cjr/data/txt/','/home/cjr/data/index/')