from compressor import *
import logging

def test_js_compress():
    snippets = \
        [
            # 注意：所有源代码最后一行应为空行
            ( '''//comment\n''', ''),

            ('''/**
              * comment
              */''', ''),

            ('''
              /**
               * this is a multi-line comment
               */
              var a = 1;
              /**
               * this is b multi-line comment
               */
          ''', 'var a = 1;'),

            ('''//this is a comment
             var i = 0;
             \t//this is b comment
             \tvar j = 1;''', 'var i = 0;var j = 1;'),

            ('''/**
              * this is a multi-line comment
              */
             var a = 1;
             // single line comment
          ''', 'var a = 1;'),

            ('''/**
              * this is a multi-line comment
              * http://127.0.0.1/index.html
              * with a url in it
              */
          ''', ''),

            ('''///*
            */
           ''', '*/' ),

            ('/*/', '/*/' ),

            ('''/*
            //*/''', ''),

            ('a+/*c+*/b==0 //def\n', 'a+b==0'),

        ]
    for snippet in snippets:
        print(snippet[0])
        print(JsCompressor.compress(snippet[0]))
        assert snippet[1] == JsCompressor.compress(snippet[0])

def test_php_compress():
    snippets = \
        [
            # 注意：所有源代码最后一行应为空行
            ( '''//comment\n''', ''),
            ( '''#comment\n''', ''),
        ]
    for snippet in snippets:
        assert snippet[1] == PhpCompressor.compress(snippet[0])
