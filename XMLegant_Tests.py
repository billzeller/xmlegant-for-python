
from XMLegant import XMLegant


class XMLegant_Tests(XMLegant):

    def test_simple(self):
        x = XMLegant();
        
        x.a.b.c = 'd';
        assert x.toXML(False) == '<a><b><c>d</c></b></a>', x.toXML(False)

        x.a.b.c = 'e'
        assert x.toXML(False) == '<a><b><c>e</c></b></a>', x.toXML(False)
        
        x.a.b = 'c'
        assert x.toXML(False) == '<a><b>c</b></a>', x.toXML(False)
        
        x.a = 'b'
        assert x.toXML(False) == '<a>b</a>', x.toXML(False)
        
        x.a.b = 'c'
        assert x.toXML(False) == '<a><b>c</b></a>', x.toXML(False)
        
    def test_multipleChildren(self):
        x = XMLegant()
        
        x.a.b = 'c'
        assert x.toXML(False) == '<a><b>c</b></a>', x.toXML(False)
        
        x.a.b = 'e'
        assert x.toXML(False) == '<a><b>e</b></a>', x.toXML(False)
        
        x.a.b().c = 'e'
        assert x.toXML(False) == '<a><b>e</b><b><c>e</c></b></a>', x.toXML(False)


        x.a.b('f')
        assert x.toXML(False) == '<a><b>e</b><b><c>e</c></b><b>f</b></a>', x.toXML(False)
        
        x.a.b = 'g'
        assert x.toXML(False) == '<a><b>e</b><b><c>e</c></b><b>g</b></a>', x.toXML(False)

        x.a.deleteChildren()
        assert x.toXML(False) == '<a />', x.toXML(False)

        x.a.b().c = 'd';
        assert x.toXML(False) == '<a><b><c>d</c></b></a>', x.toXML(False)

        x.a.b().c = 'e';
        assert x.toXML(False) == '<a><b><c>d</c></b><b><c>e</c></b></a>', x.toXML(False)

        x.a.deleteChildren();
        assert x.toXML(False) == '<a />', x.toXML(False)

        x.a.b.c = 'd';
        assert x.toXML(False) == '<a><b><c>d</c></b></a>', x.toXML(False)
        
        x.a.b().c = 'e';
        assert x.toXML(False) == '<a><b><c>d</c></b><b><c>e</c></b></a>', x.toXML(False)


    def test_attributes(self):
        x = XMLegant();
        
        x.a = {'b':'c', 'd':'e'};
        assert x.toXML(False) == '<a b="c" d="e" />', x.toXML(False)

        x.a['f'] = 'g';
        assert x.toXML(False) == '<a b="c" d="e" f="g" />', x.toXML(False)
        
        
        assert  x.a['f'] == 'g', x.a['f']
        
    
    def test_vars(self):
        x = XMLegant();
        
        x.a.b.c = 'z';
        c_obj = x.a.b.c;
        assert x.toXML(False) == '<a><b><c>z</c></b></a>', x.toXML(False)



        # Note: This adds an additional 'c' child to c_obj's parent
        c_obj('d');
        assert x.toXML(False) == '<a><b><c>z</c><c>d</c></b></a>', x.toXML(False)

        c_obj.e = 'f';
        assert x.toXML(False) == '<a><b><c><e>f</e></c><c>d</c></b></a>', x.toXML(False)
        
        """
            Note: The following may not work as expected. The value is:
                <a><b><c>x</c><c>y</c><c>z</c></b></a>
            instead of:
                <a><b><c></c><c>x</c><c>y</c><c>z</c></b></a>
            (missing the fisrt <c></c> element)
            
            because () will overwrite an initial element if is it empty. This is
            done so:
                x = new XMLegant();
                x.a.b('c');
            works correctly. Without this adjustment, the above would equal:
                <a><b><b><b>c</b></a>
            ...because the call to 'x.a.b' would create one element
            and the call to '()' would create an additional one.
        """
        
        x = XMLegant()
        c_obj = x.a.b.c
        c_obj('x')
        c_obj('y')
        c_obj('z')
        assert x.toXML(False) == '<a><b><c>x</c><c>y</c><c>z</c></b></a>', x.toXML(False)
        
        """
            If you need to get around this, simply initialize the element.
        """
        

        x = XMLegant()
        x.a.b.c = ''
        c_obj = x.a.b.c
        c_obj('x')
        c_obj('y')
        c_obj('z')
        assert x.toXML(False) == '<a><b><c /><c>x</c><c>y</c><c>z</c></b></a>', x.toXML(False)
    
    
    def test_childObjs(self):
        x1 = XMLegant()

        x1.d.e = 'f'      
        assert x1.toXML(False) == '<d><e>f</e></d>', x1.toXML(False)
            
        x2 = XMLegant()
        
        x2.a.b
        assert x2.toXML(False) == '<a><b /></a>', x2.toXML(False)
        
        x2.a.b = x1
        assert x2.toXML(False) == '<a><b><d><e>f</e></d></b></a>', x2.toXML(False)

        
        x2.a.b(x1)
        assert x2.toXML(False) == '<a><b><d><e>f</e></d></b><b><d><e>f</e></d></b></a>', x2.toXML(False)


    def test_childObjRef(self):
        
        x = XMLegant()
        
        x.a.b.c = 'd';
        assert x.toXML(False) == '<a><b><c>d</c></b></a>', x.toXML(False)

        x.a.b().e = 'f';
        assert x.toXML(False) == '<a><b><c>d</c></b><b><e>f</e></b></a>', x.toXML(False)

        x.a.b().g = 'h';
        assert x.toXML(False) == '<a><b><c>d</c></b><b><e>f</e></b><b><g>h</g></b></a>', x.toXML(False)
        
        x.a.b[1] = 'i';
        assert x.toXML(False) == '<a><b><c>d</c></b><b>i</b><b><g>h</g></b></a>', x.toXML(False)


    def test_addingBulkChildren(self):
        
        """
            Suppose you want to easily create the structure
                <books>
                    <book>
                        <title>Title 1</title>
                        <author>Author 1</author>
                        <isbn>isbn1</isbn>
                    </book>
                    <book>
                        <title>Title 2</title>
                        <author>Author 2</author>
                        <isbn>isbn2</isbn>
                    </book>
                    <book>
                        <title>Title 2</title>
                        <author>Author 2</author>
                        <isbn>isbn2</isbn>
                    </book>
                    ...
                </books>
        
        """
        
        book_data = XMLegant()
        
        x = XMLegant()
        
        for i in xrange(5):
            book_data.title = "Title "+str(i)
            book_data.author = "Author "+str(i)
            book_data.isbn = "isbn "+str(i)
            x.books.book(book_data)
        
        assert x.toXML(False) == '<books><book><title>Title 0</title><author>Author 0</author><isbn>isbn 0</isbn></book><book><title>Title 1</title><author>Author 1</author><isbn>isbn 1</isbn></book><book><title>Title 2</title><author>Author 2</author><isbn>isbn 2</isbn></book><book><title>Title 3</title><author>Author 3</author><isbn>isbn 3</isbn></book><book><title>Title 4</title><author>Author 4</author><isbn>isbn 4</isbn></book></books>', x.toXML(False)
        
        
    def test_multRootChildren(self):
        # XXX ElementTree doesn't appear to support multiple root elements
        # (probably because it's invalid XML)
        pass
        
    
    def test_functional(self):
        x = XMLegant()


        x.media('type', 'documentary') \
          .media \
            .movie.title('PHP2: More Parser Stories') \
                   .plot('This is all about the people who make it work.') \
                   .characters() \
                      .character() \
                        .name('Mr. Parser') \
                        .actor('John Doe') \
                        .getParent() \
                      .character() \
                        .name('Mr. Parser2') \
                        .actor('John Doe2') \
                        .getParent() \
                      .getParent() \
                   .rating(5)
    
        """
        <media type="documentary">
            <movie>
                <title>PHP2: More Parser Stories</title>
                <plot>This is all about the people who make it work.</plot>
                <characters>
                    <character>
                        <name>Mr. Parser</name>
                        <actor>John Doe</actor>
                    </character>
                    <character>
                        <name>Mr. Parser2</name>
                        <actor>John Doe2</actor>
                    </character>
                </characters>
                <rating>5</rating>
            </movie>
        </media>
        """

    def test_underscores(self):
        x = XMLegant()
        
        x.foo_bar
        
        assert x.toXML(False) == '<foo:bar />', x.toXML(False)
        
        x.foo_bar['a_b'] = 'c'
        
        assert x.toXML(False) == '<foo:bar a:b="c" />', x.toXML(False)

        x.SetReplaceUnderscores(False)
        
        assert x.toXML(False) == '<foo_bar a_b="c" />', x.toXML(False)


    def test_bookFunc(self):
        x = XMLegant()

        for i in xrange(5):
            x.books.book().title("Title %d " % i) \
                          .author("Author %d " % i) \
                          .isbn("isbn %d " % i)

        #print x.toXML()
        
    def test_encoding(self):
        x = XMLegant()
        
        x.a
        assert x.toXML() == '<a />', x.toXML()
        
        x['encoding'] = 'UTF-8';
        assert x.toXML() == "<?xml version='1.0' encoding='UTF-8'?>\n<a />", x.toXML()        
        


xmlTests = XMLegant_Tests()

for method in dir(xmlTests):
    if method.startswith('test_'):
        getattr(xmlTests, method)()
