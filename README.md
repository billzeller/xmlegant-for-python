## XMLElegant (for Python)

### (c) 2009 Bill Zeller
#### [http://from.bz](http://from.bz)
#### (A PHP version of this class can be found [here](http://github.com/billzeller/xmlegant-for-php/tree/master))

XMLElegant is a Python class that allows easy generation of XML.

As a quick example, the following XML:

    <books>
        <book>
            <title>Title 1</title>
            <author>Author 1</author>
            <isbn>isbn 1</isbn>
        </book>
        <book>
            <title>Title 2</title>
            <author>Author 2</author>
            <isbn>isbn 2</isbn>
        </book>
        <book>
            <title>Title 3</title>
            <author>Author 3</author>
            <isbn>isbn 3</isbn>
        </book>
        ...
    </books>    

can be generated by:

    x = XMLegant()

    for i in xrange(5):
        x.books.book(XMLegant().title("Title %d" % i) \
                               .author("Author %d" % i) \
                               .isbn("isbn %d" % i))
    
The following XML:
    <a>
        <b>c</b>
        <b>d</b>
        <e>f</e>
        <b>g</b>
        <h>
            <i j="k"/>
            <l>
                <m/>
            </l>
            <n>o</n>
        </h>
    <a>

can be generated by either:

    x = XMLegant()

    x.a.b('c') 
    x.a.b('d')
    x.a.e('f')
    x.a.b('g')
    x.a.h.i['j'] = 'k'
    x.a.h.l.m
    x.a.h.n = 'o'


or:

    x = XMLegant()

    x.a() \
        .b('c') \
        .b('d') \
        .e('f') \
        .b('g') \
        .h() \
          .i('j', 'k') \
          .l() \
            .m('') \
            .getParent() \
          .n('o')

Many more examples are available in demo.py. Also, XMLegant_Tests.py consists of a number of unit tests that may be useful as a guide.

